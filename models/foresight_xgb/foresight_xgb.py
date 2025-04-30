import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils.class_weight import compute_class_weight

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

import dagshub
import mlflow
import os
from dotenv import load_dotenv

load_dotenv()

print("-------------------------------------------------------")
print("                  CONNECTING TO MLFLOW")
print("-------------------------------------------------------")

mlflow.set_tracking_uri(f"https://dagshub.com/{os.getenv("MLFLOW_TRACKING_USERNAME")}/my-first-repo.mlflow")
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

print(Counter(y_resample))

# from imblearn.under_sampling import RandomUnderSampler
# from collections import Counter

# rus = RandomUnderSampler( random_state = 42 )
# X_resample, y_resample = rus.fit_resample(X_train, y_train)

# print(Counter(y_resample))




# # XGBoost

from xgboost import XGBClassifier

with mlflow.start_run():

    n_estimators = 200
    max_depth = 15
    lr = 0.00001
    colsample_bytree=0.5

    print("-------------------------------------------------------")
    print("                      PARAMETERS")
    print("-------------------------------------------------------")
    print("")
    print(f"\tn_estimators = {n_estimators}")
    print(f"\tmax_depth = {max_depth}")
    print(f"\tlr = {lr}")
    print(f"\tcolsample_bytree = {colsample_bytree}")
    print("")
    mlflow.log_param('n_estimators', n_estimators)
    mlflow.log_param('max_depth', max_depth)
    mlflow.log_param('lr', lr)
    mlflow.log_param('colsample_bytree', colsample_bytree)

    model = XGBClassifier(
        objective='multi:softmax',
        num_class=5,
        n_estimators=n_estimators,
        max_depth=max_depth,
        learning_rate=lr,
        subsample=0.8,
        colsample_bytree=colsample_bytree,
        random_state=42
    )

    print("-------------------------------------------------------")
    print("                    TRAINING CGBOOST")
    print("-------------------------------------------------------")

    model.fit(X_resample, y_resample)

    train_accuracy = model.score(X_resample, y_resample)

    y_pred = model.predict(X_test)

    val_accuracy = accuracy_score(y_test, y_pred)

    print("-------------------------------------------------------")
    print("                         SCORES")
    print("-------------------------------------------------------")
    print("")
    print(f"\tTrain Accuracy :\t{train_accuracy}")
    print(f"\tVal Accuracy: \t\t{val_accuracy}")
    print("")
    mlflow.log_metric('train_accuracy', train_accuracy)
    mlflow.log_metric('val_accuracy', val_accuracy)

    mlflow.xgboost.log_model(model, "xgboost_model")
    
    from sklearn.metrics import  ConfusionMatrixDisplay
    from sklearn.metrics import confusion_matrix

    fig = plt.figure(figsize=(16, 16))
    con = confusion_matrix( y_test , y_pred )
    disp = ConfusionMatrixDisplay( confusion_matrix = con,  display_labels = range(5) ).plot()
    plt.savefig("matriz.jpg")
    mlflow.log_artifact("matriz.jpg")

print("-------------------------------------------------------")
print("                          END")
print("-------------------------------------------------------")