import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import os
import json
import mlflow
import mlflow.tensorflow
from dotenv import load_dotenv
from imblearn.combine import SMOTEENN

from sklearn.utils.class_weight import compute_class_weight
from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
)

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout, BatchNormalization
import keras_tuner as kt

# ---------------------- CONFIGURACIÓN ----------------------
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("foresight_nn")

# ---------------------- CARGA DE DATOS ----------------------
print("-------------------------------------------------------")
print("                    LOADING DATA")
print("-------------------------------------------------------")

train_df = pd.read_csv("../../data/processed/combats_train.csv")
test_df = pd.read_csv("../../data/processed/combats_test.csv")

X_train = train_df.drop("difficulty", axis=1)
y_train = train_df["difficulty"]
X_test = test_df.drop("difficulty", axis=1)
y_test = test_df["difficulty"]

# ---------------------- SMOTEENN ----------------------
print("-------------------------------------------------------")
print("                RESAMPLING WITH SMOTEENN")
print("-------------------------------------------------------")

smoteenn = SMOTEENN(random_state=42)
X_resample, y_resample = smoteenn.fit_resample(X_train, y_train)

print("Después de SMOTEENN:", Counter(y_resample))

# Nuevos class weights tras SMOTEENN
classes = np.unique(y_resample)
weights = compute_class_weight('balanced', classes=classes, y=y_resample)
class_weights = dict(zip(classes, weights))

# ---------------------- MODELO ----------------------
def build_model(hp):
    model = Sequential()
    model.add(Input(shape=(X_resample.shape[1],)))

    for i in range(hp.Int("num_layers", 1, 2)):
        model.add(
            Dense(
                units=hp.Int(f'units_{i}', min_value=20, max_value=50, step=2),
                activation=hp.Choice(f"activation_{i}", ["relu", "leaky_relu"]),
            )
        )
        model.add(Dropout(0.5))
        model.add(BatchNormalization())

    model.add(Dense(5, activation="softmax", name="predictions"))

    lr = hp.Choice("lr", values=[1e-2, 1e-3, 1e-4])
    optimizers_dict = {
        "Adam": tf.keras.optimizers.Adam(learning_rate=lr),
        "SGD": tf.keras.optimizers.SGD(learning_rate=lr),
        "Adagrad": tf.keras.optimizers.Adagrad(learning_rate=lr)
    }
    optimizer = hp.Choice("optimizer", values=["SGD", "Adam", "Adagrad"])
    model.compile(
        optimizer=optimizers_dict[optimizer],
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy", tf.keras.metrics.AUC(name="AUC", multi_label=True)]
    )
    return model

# ---------------------- TUNING Y ENTRENAMIENTO ----------------------
tuner = kt.Hyperband(
    build_model,
    objective=kt.Objective("val_accuracy", direction="max"),
    max_epochs=10,
    factor=3,
    directory="salida",
    project_name="foresight_nn",
    overwrite=True
)

with mlflow.start_run():
    mlflow.tensorflow.autolog()

    tuner.search(
        X_resample, y_resample,
        validation_split=0.2,
        class_weight=class_weights,
        verbose=1
    )

    best_hps = tuner.get_best_hyperparameters()[0]
    print("BEST PARAMETERS:", best_hps.values)

    for param, value in best_hps.values.items():
        mlflow.log_param(param, value)

    model = tuner.hypermodel.build(best_hps)
    history = model.fit(
        X_resample, y_resample,
        validation_split=0.2,
        class_weight=class_weights,
        epochs=20,
        verbose=1
    )

    mlflow.tensorflow.log_model(
        model,
        artifact_path="nn_model",
        registered_model_name="NN_Classifier"
    )

    # ---------------------- GRÁFICAS ----------------------
    def plot_metric(metric_name, title):
        plt.figure(figsize=(12, 5))
        plt.plot(history.history[metric_name])
        plt.plot(history.history[f"val_{metric_name}"])
        plt.title(title)
        plt.xlabel("Epoch")
        plt.ylabel(metric_name)
        plt.legend(["Train", "Validation"])
        plt.grid()
        filename = f"{metric_name}.jpg"
        plt.savefig(filename)
        mlflow.log_artifact(filename)
        plt.close()

    plot_metric("accuracy", "Model Accuracy")
    plot_metric("loss", "Model Loss")
    plot_metric("AUC", "Model AUC")

    # ---------------------- EVALUACIÓN ----------------------
    model.evaluate(X_test, y_test, verbose=0)

    y_pred_probs = model.predict(X_test)
    y_pred = np.argmax(y_pred_probs, axis=1)

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_test))
    disp.plot(ax=ax, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.jpg")
    mlflow.log_artifact("confusion_matrix.jpg")
    plt.close()

    # Histograma y distribución
    fig, ax = plt.subplots(2, 1, figsize=(8, 6))
    ax[0].hist(y_test, bins=5, rwidth=0.8)
    ax[0].set_title("y_test")
    ax[1].hist(y_pred, bins=5, rwidth=0.8)
    ax[1].set_title("Predictions")
    plt.tight_layout()
    plt.savefig("y_distribution.jpg")
    mlflow.log_artifact("y_distribution.jpg")
    plt.close()

    # Classification Report JSON
    report = classification_report(y_test, y_pred, output_dict=True)
    with open("classification_report.json", "w") as f:
        json.dump(report, f, indent=4)
    mlflow.log_artifact("classification_report.json")

print("-------------------------------------------------------")
print("                          END")
print("-------------------------------------------------------")

