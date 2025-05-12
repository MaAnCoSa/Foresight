
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.model_selection import RandomizedSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import dagshub
import mlflow
import os
from dotenv import load_dotenv

load_dotenv()

print("-------------------------------------------------------")
print("                  CONNECTING TO MLFLOW")
print("-------------------------------------------------------")

mlflow.set_tracking_uri(os.getenv("MLFLOW_TRACKING_URI"))
mlflow.set_experiment("foresight_knn")

print("-------------------------------------------------------")
print("                    SPLITTING DATA")
print("-------------------------------------------------------")

combats_df = pd.read_csv("../../data/processed/combats_df.csv")


from sklearn.model_selection import train_test_split
from collections import Counter

X = combats_df.drop("difficulty", axis=1)
y = combats_df["difficulty"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y)



print("-------------------------------------------------------")
print("                    RESAMPLING DATA")
print("-------------------------------------------------------")


pca = PCA()
pca.fit(X_train)

pca = PCA(n_components=10)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)


# Definir el modelo base


# Usar el mejor modelo


with mlflow.start_run():  # aquí podrías pasar experiment_id=123 si ya existe
    print("-------------------------------------------------------")
    print("                    TRAINING KNN")
    print("-------------------------------------------------------")

    # 1) Definir modelo y grid
    knn = KNeighborsClassifier()
    param_grid = {
        'n_neighbors': [3, 5, 7, 9, 11, 13],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'kd_tree', 'ball_tree'],
        'leaf_size': [20, 30, 40, 50],
        'p': [1, 2],
        'metric': ['euclidean', 'manhattan', 'minkowski']
    }

    # 2) RandomizedSearchCV
    grid_search = RandomizedSearchCV(
        estimator=knn,
        param_distributions=param_grid,
        n_iter=500,
        scoring='f1_macro',
        cv=3,
        verbose=2,
        n_jobs=-1,
        random_state=42
    )
    grid_search.fit(X_train_pca, y_train)

    # 3) Obtención del mejor modelo y predicción
    best_knn = grid_search.best_estimator_
    y_pred = best_knn.predict(X_test_pca)

    # 4) Cálculo de métricas
    f1 = f1_score(y_test, y_pred, average='macro')
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("-------------------------------------------------------")
    print("                      PARAMETERS")
    print("-------------------------------------------------------")
    for name, value in grid_search.best_params_.items():
        print(f"{name} = {value}")

    print("\n-------------------------------------------------------")
    print("                         SCORES")
    print("-------------------------------------------------------")
    print(f"F1 Macro:   {f1:.4f}")
    print(f"Accuracy:   {acc:.4f}")

    # 5) Registro en MLflow
    # 5a) Hiperparámetros
    mlflow.log_params(grid_search.best_params_)

    # 5b) Métricas
    mlflow.log_metric("f1_macro", f1)
    mlflow.log_metric("accuracy", acc)

    # 5c) Matriz de confusión como artefacto
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm,
                                  display_labels=best_knn.classes_)
    disp.plot(ax=ax, cmap=plt.cm.Blues)
    ax.set_title("Matriz de Confusión")
    fig.tight_layout()
    # Guardar y subir
    fig.savefig("confusion_matrix.jpg")
    mlflow.log_artifact("confusion_matrix.jpg")
    plt.close(fig)

    # 5c) Modelo
    mlflow.sklearn.log_model(best_knn, "knn_model")

print("----------------------- FIN ---------------------")