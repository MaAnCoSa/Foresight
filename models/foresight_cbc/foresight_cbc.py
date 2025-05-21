import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import json
import hashlib
import os
from datetime import datetime
from dotenv import load_dotenv
from collections import Counter
from sklearn.decomposition import PCA
from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report, f1_score
)
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import mlflow
from catboost import CatBoostClassifier
import mlflow.catboost

def inicializar_mlflow(nombre_experimento: str, run_name: str):
    import mlflow

    # Cerrar cualquier run que esté activa (aunque no se muestre)
    try:
        while mlflow.active_run() is not None:
            mlflow.end_run()
    except Exception as e:
        print(f"⚠️ No se pudo cerrar una run activa: {e}")

    # Establecer experimento
    mlflow.set_experiment(nombre_experimento)

    # Iniciar nuevo run
    return mlflow.start_run(run_name=run_name)

# -------------------- CONFIGURACIÓN --------------------
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
run_name = f"catboost_{datetime.now().strftime('%Y%m%d_%H%M%S')}"


# -------------------- CARGA DE DATOS --------------------
print("-------------------------------------------------------")
print("                    LOADING DATA")
print("-------------------------------------------------------")

train_df = pd.read_csv("../../data/processed/combats_train.csv")
test_df = pd.read_csv("../../data/processed/combats_test.csv")

X_train = train_df.drop("difficulty", axis=1)
y_train = train_df["difficulty"]
X_test = test_df.drop("difficulty", axis=1)
y_test = test_df["difficulty"]

# -------------------- RESAMPLING --------------------
print("-------------------------------------------------------")
print("                    RESAMPLING DATA")
print("-------------------------------------------------------")

smote = SMOTE(random_state=42)
X_resample, y_resample = smote.fit_resample(X_train, y_train)

# -------------------- CLASS WEIGHTS --------------------
print("-------------------------------------------------------")
print("                    COMPUTING CLASS WEIGHTS")
print("-------------------------------------------------------")

counts = Counter(y_resample)
total = sum(counts.values())
class_weights = {cls: total / (len(counts) * count) for cls, count in counts.items()}
class_weights[2] *= 2  # Ajuste manual: más peso a clase 2
weights_list = [class_weights[i] for i in sorted(class_weights.keys())]

# -------------------- ENTRENAMIENTO Y MLFLOW --------------------
with inicializar_mlflow("foresight_catboost", run_name):
    mlflow.autolog()

    param_grid = {
        'depth': [4, 6, 8],
        'learning_rate': [0.01, 0.05, 0.1],
        'iterations': [200, 500, 800],
        'l2_leaf_reg': [1, 3, 5, 7]
    }

    search = RandomizedSearchCV(
        CatBoostClassifier(loss_function='MultiClass', verbose=0, class_weights=weights_list),
        param_distributions=param_grid,
        n_iter=20,
        scoring='f1_macro',
        cv=StratifiedKFold(n_splits=3, shuffle=True, random_state=42),
        n_jobs=-1,
        random_state=42
    )

    search.fit(X_resample, y_resample)

    model = search.best_estimator_
    y_pred = model.predict(X_test).flatten()

    acc_resample = model.score(X_resample, y_resample)
    acc_test = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average="macro")

    mlflow.log_metric("val_f1_macro", f1_macro)
    mlflow.log_metric("score_on_resampled_train", acc_resample)
    mlflow.log_metric("val_accuracy", acc_test)

    # -------------------- MATRICES DE CONFUSIÓN --------------------
    cm = confusion_matrix(y_test, y_pred)
    cm_norm = cm.astype("float") / cm.sum(axis=1)[:, np.newaxis]

    fig, ax = plt.subplots(figsize=(6, 6))
    sns.heatmap(cm_norm, annot=True, fmt=".2f", cmap="Blues", ax=ax)
    ax.set_title("Normalized Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix_normalized.jpg")
    mlflow.log_artifact("confusion_matrix_normalized.jpg")
    plt.close()

    fig, ax = plt.subplots(figsize=(6, 6))
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.unique(y_test))
    disp.plot(ax=ax, cmap="Blues")
    plt.title("Confusion Matrix")
    plt.tight_layout()
    plt.savefig("confusion_matrix.jpg")
    mlflow.log_artifact("confusion_matrix.jpg")
    plt.close()

    plt.figure(figsize=(8, 4))
    plt.plot(np.cumsum(pca.explained_variance_ratio_), marker='o')
    plt.xlabel('Número de componentes')
    plt.ylabel('Varianza acumulada')
    plt.title('Explained Variance por PCA')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("pca_explained_variance.jpg")
    mlflow.log_artifact("pca_explained_variance.jpg")
    plt.close()
    # -------------------- REPORTE DE CLASIFICACIÓN --------------------
    report = classification_report(y_test, y_pred, output_dict=True)

    with open("classification_report.json", "w") as f:
        json.dump(report, f, indent=4)
    mlflow.log_artifact("classification_report.json")

    with open("classification_report.md", "w") as f:
        f.write("# Classification Report\n\n")
        for label, scores in report.items():
            if isinstance(scores, dict):
                f.write(f"## Class {label}\n")
                for metric, val in scores.items():
                    f.write(f"- **{metric}**: {val:.4f}\n")
                f.write("\n")
    mlflow.log_artifact("classification_report.md")

    # -------------------- GUARDADO DE MODELO --------------------
    joblib.dump(model, "best_model_catboost.pkl")
    mlflow.log_artifact("best_model_catboost.pkl")

    # -------------------- HASH DEL SCRIPT --------------------
    try:
        with open(__file__, "rb") as f:
            code_hash = hashlib.md5(f.read()).hexdigest()
            mlflow.log_param("script_md5", code_hash)
    except:
        pass

print("-------------------------------------------------------")
print("                        END")
print("-------------------------------------------------------")
