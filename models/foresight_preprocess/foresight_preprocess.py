import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils.class_weight import compute_class_weight

# Leer datos
df = pd.read_csv("../../data/raw/combat_results_lvl_5.csv")

# Eliminar columnas innecesarias
df.drop(columns=[
    "Unnamed: 0", "winner", "not_conscious_players_ratio", "party_hp_ratio",
    *[f"monster{i}_name" for i in range(1, 8)]
], inplace=True)

# Separar la variable objetivo y hacer copia de features
y = df["difficulty"].copy()
X = df.drop(columns=["difficulty"]).copy()

# Separar datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# --- Función general para escalar columnas numéricas ---
def scale_columns(df_train, df_test, col_names):
    scaler = StandardScaler()
    df_train[col_names] = scaler.fit_transform(df_train[col_names])
    df_test[col_names] = scaler.transform(df_test[col_names])
    return df_train, df_test

# Escalar columnas de HP y AC
hp_ac_cols = [col for col in X.columns if ("hp_max" in col or "_ac" in col)]
X_train, X_test = scale_columns(X_train, X_test, hp_ac_cols)

# Escalar columnas de atributos (STR, DEX, etc.)
attr_cols = [col for col in X.columns if any(stat in col for stat in ["_STR", "_DEX", "_CON", "_INT", "_WIS", "_CHA"])]
X_train, X_test = scale_columns(X_train, X_test, attr_cols)

# Crear columnas num_pcs y num_monsters
def contar_participantes(df):
    df = df.copy()
    df["num_pcs"] = df[[f"pc{i}_class" for i in range(1, 8)]].apply(lambda row: sum(row != "-"), axis=1)
    df["num_monsters"] = df[[f"monster{i}_cr" for i in range(1, 8)]].apply(lambda row: sum(row != 0.0), axis=1)
    return df

X_train = contar_participantes(X_train)
X_test = contar_participantes(X_test)

# Nivel promedio (usamos pc1_level)
X_train["pc_lvl"] = X_train["pc1_level"]
X_test["pc_lvl"] = X_test["pc1_level"]

# Codificar clases de personajes
def one_hot_classes(df):
    class_cols = [f"pc{i}_class" for i in range(1, 8)]
    df = pd.get_dummies(df, columns=class_cols, prefix=class_cols, dtype=int)
    return df

X_train = one_hot_classes(X_train)
X_test = one_hot_classes(X_test)

# Eliminar columnas de niveles de personajes
X_train.drop(columns=[f"pc{i}_level" for i in range(1, 8)], inplace=True)
X_test.drop(columns=[f"pc{i}_level" for i in range(1, 8)], inplace=True)

# Binning de dificultad
def bin_difficulty(d):
    if d in [0, 1]: return 0
    elif d in [2, 3]: return 1
    elif d in [4, 5]: return 2
    elif d in [6, 7]: return 3
    elif d in [8, 9]: return 4

y_train = y_train.apply(bin_difficulty)
y_test = y_test.apply(bin_difficulty)

# Visualización
plt.figure(figsize=(10, 5))
plt.hist(y, bins=10)
plt.title("Original difficulty")
plt.savefig("difficulty_original_hist.jpg")

plt.figure(figsize=(10, 5))
plt.hist(pd.concat([y_train, y_test]), bins=5)
plt.title("Binned difficulty")
plt.savefig("difficulty_binned_hist.jpg")

# Guardar datasets procesados
train_df = X_train.copy()
train_df["difficulty"] = y_train
train_df.to_csv("../../data/processed/combats_train.csv", index=False)

test_df = X_test.copy()
test_df["difficulty"] = y_test
test_df.to_csv("../../data/processed/combats_test.csv", index=False)

print("----------------------- FIN ---------------------")