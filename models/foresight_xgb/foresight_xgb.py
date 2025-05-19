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

from sklearn.metrics import (
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report
)
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from xgboost import XGBClassifier
from imblearn.over_sampling import SMOTE
import mlflow
import mlflow.xgboost

# -------------------- CONFIGURACIÓN --------------------
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])
mlflow.set_experiment("foresight_xgb")
run_name = f"xgb_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

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

# -------------------- CONFIGURACIÓN DEL MODELO --------------------
param_dist = {
    "n_estimators": [50, 100, 200],
    "max_depth": [4, 6, 8, 10],
    "learning_rate": [0.01, 0.05, 0.1, 0.3],
    "colsample_bytree": [0.3, 0.5, 0.7, 1.0],
    "subsample": [0.5, 0.8, 1.0],
    "reg_alpha": [0, 0.1, 0.5],
    "reg_lambda": [1.0, 1.5, 2.0]
}

model = XGBClassifier(
    objective="multi:softmax",
    num_class=5,
    random_state=42,
    verbosity=0
)

cv = StratifiedKFold(n_splits=3, shuffle=True, random_state=42)

search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_dist,
    n_iter=10,
    scoring="accuracy",
    n_jobs=2,
    cv=cv,
    verbose=2,
    random_state=42
)

# -------------------- ENTRENAMIENTO Y MLFLOW --------------------
with mlflow.start_run(run_name=run_name):
    mlflow.xgboost.autolog()

    search.fit(X_resample, y_resample)
    best_model = search.best_estimator_
    y_pred = best_model.predict(X_test)

    acc_resample = best_model.score(X_resample, y_resample)
    acc_test = accuracy_score(y_test, y_pred)

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

    # -------------------- REPORTE DE CLASIFICACIÓN --------------------
    report = classification_report(y_test, y_pred, output_dict=True)

    # JSON
    with open("classification_report.json", "w") as f:
        json.dump(report, f, indent=4)
    mlflow.log_artifact("classification_report.json")

    # Markdown
    with open("classification_report.md", "w") as f:
        f.write("# Clasification Report\n\n")
        for label, scores in report.items():
            if isinstance(scores, dict):
                f.write(f"## Class {label}\n")
                for metric, val in scores.items():
                    f.write(f"- **{metric}**: {val:.4f}\n")
                f.write("\n")
    mlflow.log_artifact("classification_report.md")

    # -------------------- GUARDADO DE MODELO --------------------
    joblib.dump(best_model, "best_model_xgb.pkl")
    mlflow.log_artifact("best_model_xgb.pkl")

    joblib.dump(search, "random_search_object.pkl")
    mlflow.log_artifact("random_search_object.pkl")

    # -------------------- HASH DEL SCRIPT (opcional) --------------------
    try:
        with open(__file__, "rb") as f:
            code_hash = hashlib.md5(f.read()).hexdigest()
            mlflow.log_param("script_md5", code_hash)
    except:
        pass  # Entorno interactivo no define __file__

print("-------------------------------------------------------")
print("                        END")
print("-------------------------------------------------------")

