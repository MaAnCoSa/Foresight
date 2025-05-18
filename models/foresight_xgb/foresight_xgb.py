import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils.class_weight import compute_class_weight

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix, ConfusionMatrixDisplay
from xgboost import XGBClassifier
from sklearn.model_selection import RandomizedSearchCV
import dagshub
import mlflow
import mlflow.xgboost
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
mlflow.set_experiment("foresight_xgb")


print("-------------------------------------------------------")
print("                    SPLITTING DATA")
print("-------------------------------------------------------")

combats_df = pd.read_csv("../../data/processed/combats_df.csv")

from sklearn.model_selection import train_test_split

X = combats_df.drop("difficulty", axis=1)
y = combats_df["difficulty"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)

classes = np.unique(y_train)
weights = compute_class_weight('balanced', classes=classes, y=y_train)
class_weights = dict(zip(classes, weights))

print("-------------------------------------------------------")
print("                    RESAMPLING DATA")
print("-------------------------------------------------------")

from imblearn.over_sampling import SMOTE
from collections import Counter

ada = SMOTE (random_state=42)
print("Haciendo resampling...")
X_resample, y_resample  = ada.fit_resample( X_train, y_train )



    


# Define búsqueda aleatoria de hiperparámetros
param_dist = {
    "n_estimators": [50, 100, 200],
    "max_depth": [4, 6, 8, 10, 15],
    "learning_rate": [0.01, 0.05, 0.1, 0.3],
    "colsample_bytree": [0.3, 0.5, 0.7, 1.0],
    "subsample": [0.5, 0.8, 1.0]
}

model = XGBClassifier(
    objective="multi:softmax",
    num_class=5,
    random_state=42,
    verbosity=0
)

search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=10,
    scoring="accuracy",
    n_jobs=2,
    cv=3,
    verbose=2,
    random_state=42
)

with mlflow.start_run():
    mlflow.xgboost.autolog()
    # Entrenamiento con validación cruzada
    search.fit(X_resample, y_resample)

    best_model = search.best_estimator_
    y_pred = best_model.predict(X_test)

    acc_train = best_model.score(X_resample, y_resample)
    acc_test = accuracy_score(y_test, y_pred)

    print("Best parameters found:", search.best_params_)
    print(f"Train accuracy: {acc_train}")
    print(f"Test accuracy: {acc_test}")

    # Confusion matrix como artefacto
    fig, ax = plt.subplots(figsize=(6, 6))
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_resample))
    disp.plot(ax=ax, cmap="Blues")
    plt.title("Confusion Matrix")
    fig.tight_layout()
    plt.savefig("confusion_matrix.jpg")
    mlflow.log_artifact("confusion_matrix.jpg")
    plt.close()

    # Log manual si quieres añadir métricas adicionales
    mlflow.log_metric("train_accuracy", acc_train)
    mlflow.log_metric("val_accuracy", acc_test)

    # Registrar modelo (opcional)
    mlflow.xgboost.log_model(
        best_model,
        artifact_path="xgboost_model",
        registered_model_name="XGBoost_Classifier"
    )

print("-------------------------------------------------------")
print("                          END")
print("-------------------------------------------------------")