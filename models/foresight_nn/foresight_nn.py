
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils.class_weight import compute_class_weight

import dagshub
import mlflow
import mlflow.tensorflow
import os
from dotenv import load_dotenv

load_dotenv()

print("-------------------------------------------------------")
print("                  CONNECTING TO MLFLOW")
print("-------------------------------------------------------")

os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")

mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

mlflow.set_experiment("foresight_nn")

print("-------------------------------------------------------")
print("                    SPLITTING DATA")
print("-------------------------------------------------------")

combats_df = pd.read_csv("../../data/processed/combats_df.csv")


from sklearn.model_selection import train_test_split
from collections import Counter

X = combats_df.drop("difficulty", axis=1)
y = combats_df["difficulty"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classes = np.unique(y_train)
weights = compute_class_weight('balanced', classes=classes, y=y_train)
class_weights = dict(zip(classes, weights))

# from keras.utils import to_categorical

# y_train_onehot = to_categorical(y_train, num_classes=5)
# y_test_onehot = to_categorical(y_test, num_classes=5)

print("-------------------------------------------------------")
print("                    RESAMPLING DATA")
print("-------------------------------------------------------")

# from imblearn.over_sampling import SMOTE

# ada = SMOTE (random_state=42)
# print("Haciendo resampling...")
# X_resample, y_resample  = ada.fit_resample( X_train, y_train )

# print(Counter(y_resample))


from imblearn.under_sampling import RandomUnderSampler

rus = RandomUnderSampler( random_state = 42 )
X_resample, y_resample = rus.fit_resample(X_train, y_train)

print(Counter(y_resample))



# # Red Neuronal

import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Input, Dropout, BatchNormalization

import keras_tuner as kt

def build_model(hp):
    model = Sequential()
    model.add( Input(  shape=(X_resample.shape[1],)) )


    for i in range(hp.Int("num_layers", 1, 2)):  # Tune the number of layers.
        model.add(
            Dense(
                units      = hp.Int   (f'units_{i}', min_value=20, max_value=50, step=2 ), # <--- [1..15]
                activation = hp.Choice(f"activation_{i}", ["relu","leaky_relu"]),
            )
        )
        model.add(Dropout(0.5))
        model.add(BatchNormalization())

    model.add( Dense( 5, activation = 'softmax', name = "predictions" ) ) # <---- capa de salida

    lr = hp.Choice( 'lr', values=[1e-2, 1e-3, 1e-4] )
    optimizers_dict = {
        "Adam":    keras.optimizers.Adam(learning_rate=lr),
        "SGD":     keras.optimizers.SGD(learning_rate=lr),
        "Adagrad": keras.optimizers.Adagrad(learning_rate=lr)
        }

    hp_optimizers = hp.Choice(
        'optimizer',
        values=[ "SGD", "Adam", "Adagrad"]
        )

    model.compile( optimizer    = optimizers_dict[hp_optimizers],
                    loss      = "sparse_categorical_crossentropy",
                    metrics   = ["accuracy", tf.keras.metrics.AUC(name="AUC", multi_label = True)]
                    )

    return model

build_model(kt.HyperParameters())


# tuner = kt.RandomSearch( # https://keras.io/api/keras_tuner/tuners/hyperband/
#     build_model,
#     objective            = kt.Objective('val_accuracy', direction='max'),
#     executions_per_trial = 1,
#   # max_epochs           = 50,
#     max_trials           = 5,
#   # factor               = 3,
#     directory            = 'salida',
#     project_name         = 'foresight_nn',
#     overwrite            = True
# )

tuner = kt.Hyperband(
    build_model,
    objective            = kt.Objective("val_accuracy", direction="max"),
    max_epochs           = 10,
    factor               = 3,
    directory            = 'salida',
    project_name         = 'foresight_nn',
    overwrite            = True
)

with mlflow.start_run():
    mlflow.tensorflow.autolog()
    hist = tuner.search(X_resample, y_resample, validation_split=0.2, class_weight=class_weights, verbose=1 )

    best_hps = tuner.get_best_hyperparameters()[0]
    print(f"BEST PARAMETERS:")
    print(best_hps.values)

    for param, value in best_hps.values.items():
        print(param, value)
        mlflow.log_param(param, value)


    mi_mejor_modelo = tuner.hypermodel.build(best_hps)

    mlflow.tensorflow.log_model(
        mi_mejor_modelo,
        artifact_path="nn_model",
        registered_model_name="NN_Classifier"
    )


    historial = mi_mejor_modelo.fit(X_resample, y_resample, validation_split=0.2,  epochs=20,  verbose=1 )


    def plot_hist(hist):
        plt.figure(figsize=(16,6))
        plt.plot(historial.history["accuracy"])
        plt.plot(historial.history["val_accuracy"])
        plt.title("model accuracy")
        plt.ylabel("accuracy")
        plt.xlabel("epoch")
        plt.legend(["train", "validation"], loc="upper left")
        #plt.ylim((0,1))
        plt.grid()
        plt.savefig("accuracy.jpg")
        mlflow.log_artifact("accuracy.jpg")

    plot_hist(historial)

    def plot_hist_auc(hist):
        plt.figure(figsize=(16,6))
        plt.plot(historial.history["AUC"])
        plt.plot(historial.history["val_AUC"])
        plt.title("model AUC")
        plt.ylabel("AUC")
        plt.xlabel("epoch")
        plt.legend(["train", "validation"], loc="upper left")
        #plt.ylim((0,1))
        plt.grid()
        plt.savefig("AUC.jpg")
        mlflow.log_artifact("AUC.jpg")

    plot_hist_auc(historial)

    def plot_hist_loss(hist):
        plt.figure(figsize=(16,6))
        plt.plot(historial.history["loss"],'.r')
        plt.plot(historial.history["val_loss"],'*b')
        plt.title("model loss")
        plt.ylabel("loss")
        plt.xlabel("epoch")
        plt.legend(["train", "validation"], loc="upper left")
        #plt.ylim((0,1))
        plt.grid()
        plt.savefig("loss.jpg")
        mlflow.log_artifact("loss.jpg")

    plot_hist_loss(historial)

    mi_mejor_modelo.evaluate(X_test, y_test)

    prediccion_test = mi_mejor_modelo.predict(X_test)
    predicted_classes = np.argmax(prediccion_test, axis=1)  # Gets class indices (0-4)

    unique_elements, count_elements = np.unique(predicted_classes,return_counts=True)
    print(unique_elements)
    print(count_elements)

    # prediccion_test=prediccion_test.ravel()

    # pred_test = np.argmax(predictions, axis=1)  # Gets class indices (0-4)

    from sklearn.metrics import  ConfusionMatrixDisplay
    from sklearn.metrics import confusion_matrix

    plt.figure(figsize=(16, 16))
    fig, ax = plt.subplots(2, 1)
    ax[0].hist(y_test) #row=0, col=0
    ax[0].set_title("y_test")
    ax[1].hist(predicted_classes) #row=1, col=0
    ax[1].set_title("predictions")  # Correct way to set title
    plt.tight_layout()  # Adjusts spacing between subplots
    plt.savefig("y_hist.jpg")
    mlflow.log_artifact("y_hist.jpg")

    plt.figure(figsize=(16, 16))
    con = confusion_matrix( y_test , predicted_classes )
    disp = ConfusionMatrixDisplay( confusion_matrix = con,  display_labels = range(5) ).plot()
    plt.savefig("matriz.jpg")
    mlflow.log_artifact("matriz.jpg")

print("----------------------- FIN ---------------------")