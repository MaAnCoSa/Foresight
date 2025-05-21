# Champion Model: CatBoost Classifier (v3)

This document summarizes the details of the best-performing model in the **Foresight** experiment, registered as `CatBoost_Classifier` version `v3` in MLflow/DagsHub.

---

## General Experiment Info

| Attribute           | Value                                             |
|---------------------|---------------------------------------------------|
| **Run ID**          | `e802fd552cdf46ada7a7cafdf1941f0d`               |
| **Experiment Name** | `foresight_catboost`                              |
| **Script**          | `foresight_cbc.py`                                |
| **Duration**        | 2.3 hours                                         |
| **Created At**      | 05/19/2025, 06:09:36 PM                          |
| **Author**          | `jesolis14`                                       |
| **Registered Model**| `CatBoost_Classifier` (version `v3`)              |

---

## Optimal Hyperparameters (RandomizedSearchCV)

| Parameter          | Value                                  |
|--------------------|-----------------------------------------|
| `learning_rate`    | 0.1                                     |
| `l2_leaf_reg`      | 7                                       |
| `iterations`       | 500                                     |
| `depth`            | 8                                       |
| `cv`               | StratifiedKFold (3 folds, shuffle=True) |
| `scoring`          | `f1_macro`                              |
| `n_iter`           | 20                                      |

---

## Model Metrics

### Validation Performance (`X_test`)

| Metric              | Value    |
|---------------------|----------|
| **Accuracy**        | 0.7749   |
| **F1 Macro**        | 0.6555   |

### Performance on Resampled Data (`X_resample`)

| Metric              | Value    |
|---------------------|----------|
| **Accuracy**        | 0.7897   |
| **F1 Score**        | 0.7881   |
| **Precision**       | 0.8031   |
| **Recall**          | 0.7897   |
| **Log Loss**        | 0.5309   |
| **ROC AUC**         | 0.9632   |

### Cross-Validation

| Metric              | Value    |
|---------------------|----------|
| **Best CV F1 Macro**| 0.7755   |

---

## Logged Artifacts

- `best_model_catboost.pkl` — serialized model (joblib)
- `confusion_matrix.jpg` — unnormalized confusion matrix
- `confusion_matrix_normalized.jpg` — normalized confusion matrix
- `classification_report.md` — detailed per-class report
- `classification_report.json` — report in JSON format
- `pca_explained_variance.jpg` — PCA explained variance chart (if used)

---

## Dataset Info

- `dataset (14d9460a)`  
- Train/Test: `../../data/processed/combats_train.csv` and `combats_test.csv`
- Labels were balanced using **SMOTE**
- **Class weights** were manually adjusted, especially for class `2`

---

## Script Verification

| Attribute     | Value                             |
|---------------|------------------------------------|
| `script_md5`  | `61ff332b4f4214d77b7601685b935dd6` |

---

## Final Notes

This model was optimized for **macro F1 score**, aiming to balance performance across all classes in a multi-class imbalanced classification problem. Techniques like SMOTE and manual `class_weights` adjustments played a key role in improving performance.

For full reproducibility and detailed tracking, visit the MLflow dashboard hosted on [DagsHub](https://dagshub.com/MaAnCoSa/Foresight.mlflow).
