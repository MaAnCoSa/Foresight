
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils.class_weight import compute_class_weight

df = pd.read_csv("../data/raw/combat_results_lvl_5.csv")
df.head()

combats_df = df.drop([
    "Unnamed: 0",

    "pc1_hp_max",
    "pc1_ac",
    "pc1_STR",
    "pc1_DEX",
    "pc1_CON",
    "pc1_INT",
    "pc1_WIS",
    "pc1_CHA",

    "pc2_hp_max",
    "pc2_ac",
    "pc2_STR",
    "pc2_DEX",
    "pc2_CON",
    "pc2_INT",
    "pc2_WIS",
    "pc2_CHA",

    "pc3_hp_max",
    "pc3_ac",
    "pc3_STR",
    "pc3_DEX",
    "pc3_CON",
    "pc3_INT",
    "pc3_WIS",
    "pc3_CHA",

    "pc4_hp_max",
    "pc4_ac",
    "pc4_STR",
    "pc4_DEX",
    "pc4_CON",
    "pc4_INT",
    "pc4_WIS",
    "pc4_CHA",

    "pc5_hp_max",
    "pc5_ac",
    "pc5_STR",
    "pc5_DEX",
    "pc5_CON",
    "pc5_INT",
    "pc5_WIS",
    "pc5_CHA",

    "pc6_hp_max",
    "pc6_ac",
    "pc6_STR",
    "pc6_DEX",
    "pc6_CON",
    "pc6_INT",
    "pc6_WIS",
    "pc6_CHA",

    "pc7_hp_max",
    "pc7_ac",
    "pc7_STR",
    "pc7_DEX",
    "pc7_CON",
    "pc7_INT",
    "pc7_WIS",
    "pc7_CHA",

    "monster1_name",
    "monster1_hp_max",
    "monster1_ac",
    "monster1_STR",
    "monster1_DEX",
    "monster1_CON",
    "monster1_INT",
    "monster1_WIS",
    "monster1_CHA",

    "monster2_name",
    "monster2_hp_max",
    "monster2_ac",
    "monster2_STR",
    "monster2_DEX",
    "monster2_CON",
    "monster2_INT",
    "monster2_WIS",
    "monster2_CHA",

    "monster3_name",
    "monster3_hp_max",
    "monster3_ac",
    "monster3_STR",
    "monster3_DEX",
    "monster3_CON",
    "monster3_INT",
    "monster3_WIS",
    "monster3_CHA",

    "monster4_name",
    "monster4_hp_max",
    "monster4_ac",
    "monster4_STR",
    "monster4_DEX",
    "monster4_CON",
    "monster4_INT",
    "monster4_WIS",
    "monster4_CHA",

    "monster5_name",
    "monster5_hp_max",
    "monster5_ac",
    "monster5_STR",
    "monster5_DEX",
    "monster5_CON",
    "monster5_INT",
    "monster5_WIS",
    "monster5_CHA",

    "monster6_name",
    "monster6_hp_max",
    "monster6_ac",
    "monster6_STR",
    "monster6_DEX",
    "monster6_CON",
    "monster6_INT",
    "monster6_WIS",
    "monster6_CHA",

    "monster7_name",
    "monster7_hp_max",
    "monster7_ac",
    "monster7_STR",
    "monster7_DEX",
    "monster7_CON",
    "monster7_INT",
    "monster7_WIS",
    "monster7_CHA",

    "winner",
    "not_conscious_players_ratio",
    "party_hp_ratio"
], axis=1)

combats_df.head()

combats_df["pc_lvl"] = combats_df["pc1_level"]

combats_df = combats_df.drop([
    "pc1_level",
    "pc2_level",
    "pc3_level",
    "pc4_level",
    "pc5_level",
    "pc6_level",
    "pc7_level"
], axis=1)

combats_df.head()

num_pcs_col = []
pc_aux_df = combats_df.drop([
    "difficulty",
    "pc_lvl",
    "monster1_cr",
    "monster2_cr",
    "monster3_cr",
    "monster4_cr",
    "monster5_cr",
    "monster6_cr",
    "monster7_cr",
], axis=1)

for i in range(len(pc_aux_df)):
    num_pcs = 0

    row = pd.DataFrame(pc_aux_df.iloc[i])
    row.columns = ["col"]

    for i in row["col"]:
        if i == "-":
            continue
        num_pcs += 1

    num_pcs_col.append(num_pcs)


num_monsters_col = []
monsters_aux_df = combats_df.drop([
    "difficulty",
    "pc_lvl",
    "pc1_class",
    "pc2_class",
    "pc3_class",
    "pc4_class",
    "pc5_class",
    "pc6_class",
    "pc7_class"
], axis=1)

for i in range(len(monsters_aux_df)):
    num_monsters = 0

    row = pd.DataFrame(monsters_aux_df.iloc[i])
    row.columns = ["col"]

    for i in row["col"]:
        if i == 0.0:
            continue
        num_monsters += 1

    num_monsters_col.append(num_monsters)

combats_df["num_pcs"] = num_pcs_col
combats_df["num_monsters"] = num_monsters_col
combats_df.head()

combats_df = combats_df.drop([
    "pc1_class",
    "pc2_class",
    "pc3_class",
    "pc4_class",
    "pc5_class",
    "pc6_class",
    "pc7_class"
], axis=1)

combats_df.head()

plt.scatter(
    combats_df["num_pcs"],
    combats_df["difficulty"],
    alpha=0.2
)
plt.show()

plt.scatter(
    combats_df["num_monsters"],
    combats_df["difficulty"],
    alpha=0.1
)
plt.show()

plt.hist(combats_df["difficulty"])
plt.show()

from sklearn.model_selection import train_test_split

X = combats_df.drop("difficulty", axis=1)
y = combats_df["difficulty"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

classes = np.unique(y_train)
weights = compute_class_weight('balanced', classes=classes, y=y_train)
class_weights = dict(zip(classes, weights))


# # Red Neuronal

import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Input

import keras_tuner as kt

def build_model(hp):
    model = Sequential()
    model.add( Input(  shape=(X_train.shape[1],)) )


    for i in range(hp.Int("num_layers", 1, 2)):
        model.add(
            Dense(
                units      = hp.Int   (f'units_{i}', min_value=1, max_value=25, step=2 ),
                activation = hp.Choice(f"activation_{i}", ["relu", "selu","leaky_relu"]),
            )
        )

    model.add( Dense( 1, activation = 'linear', name = "predictions" ) ) # <---- capa de salida

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
                    loss      = "categorical_crossentropy",
                    metrics   = ['AUC', "accuracy"]
                    )

    return model

build_model(kt.HyperParameters())

tuner = kt.RandomSearch( # https://keras.io/api/keras_tuner/tuners/hyperband/
    build_model,
    objective            = kt.Objective('val_AUC', direction='max'),
    executions_per_trial = 1,
  # max_epochs           = 50,
    max_trials           = 10,
  # factor               = 3,
    directory            = 'salida',
    project_name         = 'foresight_nn',
    overwrite            = True
)

hist = tuner.search(X_train, y_train, validation_split=0.2, class_weight=class_weights, verbose=1 )

best_hps = tuner.get_best_hyperparameters()[0]
print(f"BEST PARAMETERS:")
print(f"Densa1: {best_hps['units_0']} - Activation: {best_hps['activation_0']}")
print(f"Learning Rate: {best_hps['lr']}")

best_hps = tuner.get_best_hyperparameters()[0]
mi_mejor_modelo = tuner.hypermodel.build(best_hps)

historial = mi_mejor_modelo.fit(X_train, y_train,validation_split=0.2,  epochs=20,  verbose=1 )

def plot_hist(hist):
    plt.figure(figsize=(16,6))
    plt.plot(hist.history["accuracy"])
    plt.plot(hist.history["val_accuracy"])
    plt.title("model accuracy")
    plt.ylabel("accuracy")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    #plt.ylim((0,1))
    plt.grid()
    plt.show()

plot_hist(historial)

def plot_hist_auc(hist):
    plt.figure(figsize=(16,6))
    plt.plot(hist.history["AUC"])
    plt.plot(hist.history["val_AUC"])
    plt.title("model AUC")
    plt.ylabel("AUC")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    #plt.ylim((0,1))
    plt.grid()
    plt.show()

plot_hist_auc(historial)

def plot_hist_loss(hist):
    plt.figure(figsize=(16,6))
    plt.plot(hist.history["loss"],'.r')
    plt.plot(hist.history["val_loss"],'*b')
    plt.title("model loss")
    plt.ylabel("loss")
    plt.xlabel("epoch")
    plt.legend(["train", "validation"], loc="upper left")
    #plt.ylim((0,1))
    plt.grid()
    plt.show()

plot_hist_loss(historial)

mi_mejor_modelo.evaluate(X_test, y_test)

prediccion_test = mi_mejor_modelo.predict(X_test)

unique_elements, count_elements = np.unique(np.round(prediccion_test),return_counts=True)
print(unique_elements)
print(count_elements)

prediccion_test=prediccion_test.ravel()

pred_test = np.zeros(X_test.shape[0])

for id in range(X_test.shape[0]):
    pred_test[id] = np.round( prediccion_test[id] )

from sklearn.metrics import  ConfusionMatrixDisplay
from sklearn.metrics import confusion_matrix

con = confusion_matrix( y_test , pred_test )
disp = ConfusionMatrixDisplay( confusion_matrix = con,  display_labels = range(10) ).plot()
plt.show()


