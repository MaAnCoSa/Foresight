import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import f1_score, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import mlflow
import mlflow.sklearn
from dotenv import load_dotenv
import os

# -------------------- MLFLOW CONFIG --------------------
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("foresight_knn")

# -------------------- LOAD DATA --------------------
print("-------------------------------------------------------")
print("                    LOADING DATA")
print("-------------------------------------------------------")

train_df = pd.read_csv("../../data/processed/combats_train.csv")
test_df = pd.read_csv("../../data/processed/combats_test.csv")

X_train = train_df.drop("difficulty", axis=1)
y_train = train_df["difficulty"]
X_test = test_df.drop("difficulty", axis=1)
y_test = test_df["difficulty"]

# -------------------- PCA --------------------
print("-------------------------------------------------------")
print("                    PCA TRANSFORM")
print("-------------------------------------------------------")

pca = PCA(n_components=10)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# -------------------- ENTRENAMIENTO --------------------
with mlflow.start_run():
    mlflow.sklearn.autolog()

    print("-------------------------------------------------------")
    print("                    TRAINING KNN")
    print("-------------------------------------------------------")

    param_grid = {
        'n_neighbors': [3, 5, 7, 9, 11, 13],
        'weights': ['uniform', 'distance'],
        'algorithm': ['auto', 'kd_tree', 'ball_tree'],
        'leaf_size': [20, 30, 40, 50],
        'p': [1, 2],
        'metric': ['euclidean', 'manhattan', 'minkowski']
    }

    search = RandomizedSearchCV(
        estimator=KNeighborsClassifier(),
        param_distributions=param_grid,
        n_iter=100,
        scoring='f1_macro',
        cv=3,
        verbose=2,
        n_jobs=2,
        random_state=42
    )

    search.fit(X_train_pca, y_train)
    best_knn = search.best_estimator_

    y_pred = best_knn.predict(X_test_pca)
    f1 = f1_score(y_test, y_pred, average='macro')
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("-------------------------------------------------------")
    print("                      BEST PARAMS")
    print("-------------------------------------------------------")
    for name, value in search.best_params_.items():
        print(f"{name} = {value}")

    print("\n-------------------------------------------------------")
    print("                         SCORES")
    print("-------------------------------------------------------")
    print(f"F1 Macro:   {f1:.4f}")
    print(f"Accuracy:   {acc:.4f}")

    # -------------------- CONFUSION MATRIX --------------------
    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_test))
    disp.plot(ax=ax, cmap=plt.cm.Blues)
    ax.set_title("Confusion Matrix")
    fig.tight_layout()
    fig.savefig("confusion_matrix.jpg")
    mlflow.log_artifact("confusion_matrix.jpg")
    plt.close(fig)

    # -------------------- MODEL REGISTRATION --------------------
    mlflow.sklearn.log_model(
        best_knn,
        artifact_path="knn_model",
        registered_model_name="KNN_Classifier"
    )

print("----------------------- FIN ---------------------")
