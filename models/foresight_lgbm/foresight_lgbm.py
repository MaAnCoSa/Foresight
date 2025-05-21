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
    accuracy_score, confusion_matrix, ConfusionMatrixDisplay, classification_report, f1_score
)
from sklearn.model_selection import RandomizedSearchCV, StratifiedKFold
from lightgbm import LGBMClassifier
from imblearn.over_sampling import SMOTE
import mlflow

# -------------------- CONFIGURACIÓN --------------------
load_dotenv()
os.environ["MLFLOW_TRACKING_URI"] = "https://dagshub.com/MaAnCoSa/Foresight.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Jesolis14"
os.environ["MLFLOW_TRACKING_PASSWORD"] = os.getenv("MLFLOW_TRACKING_PASSWORD")
mlflow.set_tracking_uri(os.environ["MLFLOW_TRACKING_URI"])

mlflow.set_experiment("foresight_lgbm")
run_name = f"lgbm_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

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

# -------------------- ENTRENAMIENTO Y MLFLOW --------------------
with mlflow.start_run(run_name=run_name):
    mlflow.autolog()

    param_grid = {
        'num_leaves': [31, 63, 127],
        'learning_rate': [0.01, 0.05, 0.1],
        'n_estimators': [100, 300, 500],
        'max_depth': [5, 10, 15],
        'reg_alpha': [0, 0.1, 0.5],
        'reg_lambda': [0, 0.1, 0.5]
    }

    search = RandomizedSearchCV(
        LGBMClassifier(objective="multiclass", class_weight=None, random_state=42),
        param_distributions=param_grid,
        n_iter=20,
        scoring='f1_macro',
        cv=StratifiedKFold(n_splits=3, shuffle=True, random_state=42),
        n_jobs=-1,
        random_state=42
    )

    search.fit(X_resample, y_resample)

    model = search.best_estimator_

    y_pred = model.predict(X_test)

    acc_resample = model.score(X_resample, y_resample)
    acc_test = accuracy_score(y_test, y_pred)
    f1_macro = f1_score(y_test, y_pred, average="macro")

    mlflow.log_metric("train_accuracy_on_resampled", acc_resample)
    mlflow.log_metric("val_accuracy", acc_test)
    mlflow.log_metric("val_f1_macro", f1_macro)

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

    with open("classification_report.json", "w") as f:
        json.dump(report, f, indent=4)
    mlflow.log_artifact("classification_report.json")

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
    joblib.dump(model, "best_model_lgbm.pkl")
    mlflow.log_artifact("best_model_lgbm.pkl")

    try:
        with open(__file__, "rb") as f:
            code_hash = hashlib.md5(f.read()).hexdigest()
            mlflow.log_param("script_md5", code_hash)
    except:
        pass

print("-------------------------------------------------------")
print("                        END")
print("-------------------------------------------------------")
