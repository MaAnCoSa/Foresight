import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.utils.class_weight import compute_class_weight

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score


df = pd.read_csv("../../data/raw/combat_results_lvl_5.csv")

combats_df = df.drop([
    "Unnamed: 0",

    "monster1_name",
    "monster2_name",
    "monster3_name",
    "monster4_name",
    "monster5_name",
    "monster6_name",
    "monster7_name",

    "winner",
    "not_conscious_players_ratio",
    "party_hp_ratio"
], axis=1)

pc1_hp_max_scaler = StandardScaler()
pc2_hp_max_scaler = StandardScaler()
pc3_hp_max_scaler = StandardScaler()
pc4_hp_max_scaler = StandardScaler()
pc5_hp_max_scaler = StandardScaler()
pc6_hp_max_scaler = StandardScaler()
pc7_hp_max_scaler = StandardScaler()

monster1_hp_max_scaler = StandardScaler()
monster2_hp_max_scaler = StandardScaler()
monster3_hp_max_scaler = StandardScaler()
monster4_hp_max_scaler = StandardScaler()
monster5_hp_max_scaler = StandardScaler()
monster6_hp_max_scaler = StandardScaler()
monster7_hp_max_scaler = StandardScaler()

pc1_ac_scaler = StandardScaler()
pc2_ac_scaler = StandardScaler()
pc3_ac_scaler = StandardScaler()
pc4_ac_scaler = StandardScaler()
pc5_ac_scaler = StandardScaler()
pc6_ac_scaler = StandardScaler()
pc7_ac_scaler = StandardScaler()

monster1_ac_scaler = StandardScaler()
monster2_ac_scaler = StandardScaler()
monster3_ac_scaler = StandardScaler()
monster4_ac_scaler = StandardScaler()
monster5_ac_scaler = StandardScaler()
monster6_ac_scaler = StandardScaler()
monster7_ac_scaler = StandardScaler()

combats_df["pc1_hp_max"] = pc1_hp_max_scaler.fit_transform(combats_df[["pc1_hp_max"]])
combats_df["pc2_hp_max"] = pc2_hp_max_scaler.fit_transform(combats_df[["pc2_hp_max"]])
combats_df["pc3_hp_max"] = pc3_hp_max_scaler.fit_transform(combats_df[["pc3_hp_max"]])
combats_df["pc4_hp_max"] = pc4_hp_max_scaler.fit_transform(combats_df[["pc4_hp_max"]])
combats_df["pc5_hp_max"] = pc5_hp_max_scaler.fit_transform(combats_df[["pc5_hp_max"]])
combats_df["pc6_hp_max"] = pc6_hp_max_scaler.fit_transform(combats_df[["pc6_hp_max"]])
combats_df["pc7_hp_max"] = pc7_hp_max_scaler.fit_transform(combats_df[["pc7_hp_max"]])

combats_df["monster1_hp_max"] = monster1_hp_max_scaler.fit_transform(combats_df[["monster1_hp_max"]])
combats_df["monster2_hp_max"] = monster2_hp_max_scaler.fit_transform(combats_df[["monster2_hp_max"]])
combats_df["monster3_hp_max"] = monster3_hp_max_scaler.fit_transform(combats_df[["monster3_hp_max"]])
combats_df["monster4_hp_max"] = monster4_hp_max_scaler.fit_transform(combats_df[["monster4_hp_max"]])
combats_df["monster5_hp_max"] = monster5_hp_max_scaler.fit_transform(combats_df[["monster5_hp_max"]])
combats_df["monster6_hp_max"] = monster6_hp_max_scaler.fit_transform(combats_df[["monster6_hp_max"]])
combats_df["monster7_hp_max"] = monster7_hp_max_scaler.fit_transform(combats_df[["monster7_hp_max"]])

combats_df["pc1_ac"] = pc1_ac_scaler.fit_transform(combats_df[["pc1_ac"]])
combats_df["pc2_ac"] = pc2_ac_scaler.fit_transform(combats_df[["pc2_ac"]])
combats_df["pc3_ac"] = pc3_ac_scaler.fit_transform(combats_df[["pc3_ac"]])
combats_df["pc4_ac"] = pc4_ac_scaler.fit_transform(combats_df[["pc4_ac"]])
combats_df["pc5_ac"] = pc5_ac_scaler.fit_transform(combats_df[["pc5_ac"]])
combats_df["pc6_ac"] = pc6_ac_scaler.fit_transform(combats_df[["pc6_ac"]])
combats_df["pc7_ac"] = pc7_ac_scaler.fit_transform(combats_df[["pc7_ac"]])

combats_df["monster1_ac"] = monster1_ac_scaler.fit_transform(combats_df[["monster1_ac"]])
combats_df["monster2_ac"] = monster2_ac_scaler.fit_transform(combats_df[["monster2_ac"]])
combats_df["monster3_ac"] = monster3_ac_scaler.fit_transform(combats_df[["monster3_ac"]])
combats_df["monster4_ac"] = monster4_ac_scaler.fit_transform(combats_df[["monster4_ac"]])
combats_df["monster5_ac"] = monster5_ac_scaler.fit_transform(combats_df[["monster5_ac"]])
combats_df["monster6_ac"] = monster6_ac_scaler.fit_transform(combats_df[["monster6_ac"]])
combats_df["monster7_ac"] = monster7_ac_scaler.fit_transform(combats_df[["monster7_ac"]])

pc1_STR_scaler = StandardScaler()
pc1_DEX_scaler = StandardScaler()
pc1_CON_scaler = StandardScaler()
pc1_INT_scaler = StandardScaler()
pc1_WIS_scaler = StandardScaler()
pc1_CHA_scaler = StandardScaler()

pc2_STR_scaler = StandardScaler()
pc2_DEX_scaler = StandardScaler()
pc2_CON_scaler = StandardScaler()
pc2_INT_scaler = StandardScaler()
pc2_WIS_scaler = StandardScaler()
pc2_CHA_scaler = StandardScaler()

pc3_STR_scaler = StandardScaler()
pc3_DEX_scaler = StandardScaler()
pc3_CON_scaler = StandardScaler()
pc3_INT_scaler = StandardScaler()
pc3_WIS_scaler = StandardScaler()
pc3_CHA_scaler = StandardScaler()

pc4_STR_scaler = StandardScaler()
pc4_DEX_scaler = StandardScaler()
pc4_CON_scaler = StandardScaler()
pc4_INT_scaler = StandardScaler()
pc4_WIS_scaler = StandardScaler()
pc4_CHA_scaler = StandardScaler()

pc5_STR_scaler = StandardScaler()
pc5_DEX_scaler = StandardScaler()
pc5_CON_scaler = StandardScaler()
pc5_INT_scaler = StandardScaler()
pc5_WIS_scaler = StandardScaler()
pc5_CHA_scaler = StandardScaler()

pc6_STR_scaler = StandardScaler()
pc6_DEX_scaler = StandardScaler()
pc6_CON_scaler = StandardScaler()
pc6_INT_scaler = StandardScaler()
pc6_WIS_scaler = StandardScaler()
pc6_CHA_scaler = StandardScaler()

pc7_STR_scaler = StandardScaler()
pc7_DEX_scaler = StandardScaler()
pc7_CON_scaler = StandardScaler()
pc7_INT_scaler = StandardScaler()
pc7_WIS_scaler = StandardScaler()
pc7_CHA_scaler = StandardScaler()

monster1_STR_scaler = StandardScaler()
monster1_DEX_scaler = StandardScaler()
monster1_CON_scaler = StandardScaler()
monster1_INT_scaler = StandardScaler()
monster1_WIS_scaler = StandardScaler()
monster1_CHA_scaler = StandardScaler()

monster2_STR_scaler = StandardScaler()
monster2_DEX_scaler = StandardScaler()
monster2_CON_scaler = StandardScaler()
monster2_INT_scaler = StandardScaler()
monster2_WIS_scaler = StandardScaler()
monster2_CHA_scaler = StandardScaler()

monster3_STR_scaler = StandardScaler()
monster3_DEX_scaler = StandardScaler()
monster3_CON_scaler = StandardScaler()
monster3_INT_scaler = StandardScaler()
monster3_WIS_scaler = StandardScaler()
monster3_CHA_scaler = StandardScaler()

monster4_STR_scaler = StandardScaler()
monster4_DEX_scaler = StandardScaler()
monster4_CON_scaler = StandardScaler()
monster4_INT_scaler = StandardScaler()
monster4_WIS_scaler = StandardScaler()
monster4_CHA_scaler = StandardScaler()

monster5_STR_scaler = StandardScaler()
monster5_DEX_scaler = StandardScaler()
monster5_CON_scaler = StandardScaler()
monster5_INT_scaler = StandardScaler()
monster5_WIS_scaler = StandardScaler()
monster5_CHA_scaler = StandardScaler()

monster6_STR_scaler = StandardScaler()
monster6_DEX_scaler = StandardScaler()
monster6_CON_scaler = StandardScaler()
monster6_INT_scaler = StandardScaler()
monster6_WIS_scaler = StandardScaler()
monster6_CHA_scaler = StandardScaler()

monster7_STR_scaler = StandardScaler()
monster7_DEX_scaler = StandardScaler()
monster7_CON_scaler = StandardScaler()
monster7_INT_scaler = StandardScaler()
monster7_WIS_scaler = StandardScaler()
monster7_CHA_scaler = StandardScaler()

combats_df["pc1_STR"] = pc1_STR_scaler.fit_transform(combats_df[["pc1_STR"]])
combats_df["pc1_DEX"] = pc1_DEX_scaler.fit_transform(combats_df[["pc1_DEX"]])
combats_df["pc1_CON"] = pc1_CON_scaler.fit_transform(combats_df[["pc1_CON"]])
combats_df["pc1_INT"] = pc1_INT_scaler.fit_transform(combats_df[["pc1_INT"]])
combats_df["pc1_WIS"] = pc1_WIS_scaler.fit_transform(combats_df[["pc1_WIS"]])
combats_df["pc1_CHA"] = pc1_CHA_scaler.fit_transform(combats_df[["pc1_CHA"]])

combats_df["pc2_STR"] = pc2_STR_scaler.fit_transform(combats_df[["pc2_STR"]])
combats_df["pc2_DEX"] = pc2_DEX_scaler.fit_transform(combats_df[["pc2_DEX"]])
combats_df["pc2_CON"] = pc2_CON_scaler.fit_transform(combats_df[["pc2_CON"]])
combats_df["pc2_INT"] = pc2_INT_scaler.fit_transform(combats_df[["pc2_INT"]])
combats_df["pc2_WIS"] = pc2_WIS_scaler.fit_transform(combats_df[["pc2_WIS"]])
combats_df["pc2_CHA"] = pc2_CHA_scaler.fit_transform(combats_df[["pc2_CHA"]])

combats_df["pc3_STR"] = pc3_STR_scaler.fit_transform(combats_df[["pc3_STR"]])
combats_df["pc3_DEX"] = pc3_DEX_scaler.fit_transform(combats_df[["pc3_DEX"]])
combats_df["pc3_CON"] = pc3_CON_scaler.fit_transform(combats_df[["pc3_CON"]])
combats_df["pc3_INT"] = pc3_INT_scaler.fit_transform(combats_df[["pc3_INT"]])
combats_df["pc3_WIS"] = pc3_WIS_scaler.fit_transform(combats_df[["pc3_WIS"]])
combats_df["pc3_CHA"] = pc3_CHA_scaler.fit_transform(combats_df[["pc3_CHA"]])

combats_df["pc4_STR"] = pc4_STR_scaler.fit_transform(combats_df[["pc4_STR"]])
combats_df["pc4_DEX"] = pc4_DEX_scaler.fit_transform(combats_df[["pc4_DEX"]])
combats_df["pc4_CON"] = pc4_CON_scaler.fit_transform(combats_df[["pc4_CON"]])
combats_df["pc4_INT"] = pc4_INT_scaler.fit_transform(combats_df[["pc4_INT"]])
combats_df["pc4_WIS"] = pc4_WIS_scaler.fit_transform(combats_df[["pc4_WIS"]])
combats_df["pc4_CHA"] = pc4_CHA_scaler.fit_transform(combats_df[["pc4_CHA"]])

combats_df["pc5_STR"] = pc5_STR_scaler.fit_transform(combats_df[["pc5_STR"]])
combats_df["pc5_DEX"] = pc5_DEX_scaler.fit_transform(combats_df[["pc5_DEX"]])
combats_df["pc5_CON"] = pc5_CON_scaler.fit_transform(combats_df[["pc5_CON"]])
combats_df["pc5_INT"] = pc5_INT_scaler.fit_transform(combats_df[["pc5_INT"]])
combats_df["pc5_WIS"] = pc5_WIS_scaler.fit_transform(combats_df[["pc5_WIS"]])
combats_df["pc5_CHA"] = pc5_CHA_scaler.fit_transform(combats_df[["pc5_CHA"]])

combats_df["pc6_STR"] = pc6_STR_scaler.fit_transform(combats_df[["pc6_STR"]])
combats_df["pc6_DEX"] = pc6_DEX_scaler.fit_transform(combats_df[["pc6_DEX"]])
combats_df["pc6_CON"] = pc6_CON_scaler.fit_transform(combats_df[["pc6_CON"]])
combats_df["pc6_INT"] = pc6_INT_scaler.fit_transform(combats_df[["pc6_INT"]])
combats_df["pc6_WIS"] = pc6_WIS_scaler.fit_transform(combats_df[["pc6_WIS"]])
combats_df["pc6_CHA"] = pc6_CHA_scaler.fit_transform(combats_df[["pc6_CHA"]])

combats_df["pc7_STR"] = pc7_STR_scaler.fit_transform(combats_df[["pc7_STR"]])
combats_df["pc7_DEX"] = pc7_DEX_scaler.fit_transform(combats_df[["pc7_DEX"]])
combats_df["pc7_CON"] = pc7_CON_scaler.fit_transform(combats_df[["pc7_CON"]])
combats_df["pc7_INT"] = pc7_INT_scaler.fit_transform(combats_df[["pc7_INT"]])
combats_df["pc7_WIS"] = pc7_WIS_scaler.fit_transform(combats_df[["pc7_WIS"]])
combats_df["pc7_CHA"] = pc7_CHA_scaler.fit_transform(combats_df[["pc7_CHA"]])

combats_df["monster1_STR"] = monster1_STR_scaler.fit_transform(combats_df[["monster1_STR"]])
combats_df["monster1_DEX"] = monster1_DEX_scaler.fit_transform(combats_df[["monster1_DEX"]])
combats_df["monster1_CON"] = monster1_CON_scaler.fit_transform(combats_df[["monster1_CON"]])
combats_df["monster1_INT"] = monster1_INT_scaler.fit_transform(combats_df[["monster1_INT"]])
combats_df["monster1_WIS"] = monster1_WIS_scaler.fit_transform(combats_df[["monster1_WIS"]])
combats_df["monster1_CHA"] = monster1_CHA_scaler.fit_transform(combats_df[["monster1_CHA"]])

combats_df["monster2_STR"] = monster2_STR_scaler.fit_transform(combats_df[["monster2_STR"]])
combats_df["monster2_DEX"] = monster2_DEX_scaler.fit_transform(combats_df[["monster2_DEX"]])
combats_df["monster2_CON"] = monster2_CON_scaler.fit_transform(combats_df[["monster2_CON"]])
combats_df["monster2_INT"] = monster2_INT_scaler.fit_transform(combats_df[["monster2_INT"]])
combats_df["monster2_WIS"] = monster2_WIS_scaler.fit_transform(combats_df[["monster2_WIS"]])
combats_df["monster2_CHA"] = monster2_CHA_scaler.fit_transform(combats_df[["monster2_CHA"]])

combats_df["monster3_STR"] = monster3_STR_scaler.fit_transform(combats_df[["monster3_STR"]])
combats_df["monster3_DEX"] = monster3_DEX_scaler.fit_transform(combats_df[["monster3_DEX"]])
combats_df["monster3_CON"] = monster3_CON_scaler.fit_transform(combats_df[["monster3_CON"]])
combats_df["monster3_INT"] = monster3_INT_scaler.fit_transform(combats_df[["monster3_INT"]])
combats_df["monster3_WIS"] = monster3_WIS_scaler.fit_transform(combats_df[["monster3_WIS"]])
combats_df["monster3_CHA"] = monster3_CHA_scaler.fit_transform(combats_df[["monster3_CHA"]])

combats_df["monster4_STR"] = monster4_STR_scaler.fit_transform(combats_df[["monster4_STR"]])
combats_df["monster4_DEX"] = monster4_DEX_scaler.fit_transform(combats_df[["monster4_DEX"]])
combats_df["monster4_CON"] = monster4_CON_scaler.fit_transform(combats_df[["monster4_CON"]])
combats_df["monster4_INT"] = monster4_INT_scaler.fit_transform(combats_df[["monster4_INT"]])
combats_df["monster4_WIS"] = monster4_WIS_scaler.fit_transform(combats_df[["monster4_WIS"]])
combats_df["monster4_CHA"] = monster4_CHA_scaler.fit_transform(combats_df[["monster4_CHA"]])

combats_df["monster5_STR"] = monster5_STR_scaler.fit_transform(combats_df[["monster5_STR"]])
combats_df["monster5_DEX"] = monster5_DEX_scaler.fit_transform(combats_df[["monster5_DEX"]])
combats_df["monster5_CON"] = monster5_CON_scaler.fit_transform(combats_df[["monster5_CON"]])
combats_df["monster5_INT"] = monster5_INT_scaler.fit_transform(combats_df[["monster5_INT"]])
combats_df["monster5_WIS"] = monster5_WIS_scaler.fit_transform(combats_df[["monster5_WIS"]])
combats_df["monster5_CHA"] = monster5_CHA_scaler.fit_transform(combats_df[["monster5_CHA"]])

combats_df["monster6_STR"] = monster6_STR_scaler.fit_transform(combats_df[["monster6_STR"]])
combats_df["monster6_DEX"] = monster6_DEX_scaler.fit_transform(combats_df[["monster6_DEX"]])
combats_df["monster6_CON"] = monster6_CON_scaler.fit_transform(combats_df[["monster6_CON"]])
combats_df["monster6_INT"] = monster6_INT_scaler.fit_transform(combats_df[["monster6_INT"]])
combats_df["monster6_WIS"] = monster6_WIS_scaler.fit_transform(combats_df[["monster6_WIS"]])
combats_df["monster6_CHA"] = monster6_CHA_scaler.fit_transform(combats_df[["monster6_CHA"]])

combats_df["monster7_STR"] = monster7_STR_scaler.fit_transform(combats_df[["monster7_STR"]])
combats_df["monster7_DEX"] = monster7_DEX_scaler.fit_transform(combats_df[["monster7_DEX"]])
combats_df["monster7_CON"] = monster7_CON_scaler.fit_transform(combats_df[["monster7_CON"]])
combats_df["monster7_INT"] = monster7_INT_scaler.fit_transform(combats_df[["monster7_INT"]])
combats_df["monster7_WIS"] = monster7_WIS_scaler.fit_transform(combats_df[["monster7_WIS"]])
combats_df["monster7_CHA"] = monster7_CHA_scaler.fit_transform(combats_df[["monster7_CHA"]])



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



num_pcs_col = []
pc_aux_df = combats_df[[
    "pc1_class",
    "pc2_class",
    "pc3_class",
    "pc4_class",
    "pc5_class",
    "pc6_class",
    "pc7_class",
]]

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
monsters_aux_df = combats_df[[
    "monster1_cr",
    "monster2_cr",
    "monster3_cr",
    "monster4_cr",
    "monster5_cr",
    "monster6_cr",
    "monster7_cr"
]]

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



pc1_classes = pd.get_dummies(combats_df["pc1_class"], prefix="pc1", dtype=int)
pc2_classes = pd.get_dummies(combats_df["pc2_class"], prefix="pc2", dtype=int)
pc3_classes = pd.get_dummies(combats_df["pc3_class"], prefix="pc3", dtype=int)
pc4_classes = pd.get_dummies(combats_df["pc4_class"], prefix="pc4", dtype=int)
pc5_classes = pd.get_dummies(combats_df["pc5_class"], prefix="pc5", dtype=int)
pc6_classes = pd.get_dummies(combats_df["pc6_class"], prefix="pc6", dtype=int)
pc7_classes = pd.get_dummies(combats_df["pc7_class"], prefix="pc7", dtype=int)

combats_df = pd.concat([combats_df, pc1_classes], axis=1)
combats_df = pd.concat([combats_df, pc2_classes], axis=1)
combats_df = pd.concat([combats_df, pc3_classes], axis=1)
combats_df = pd.concat([combats_df, pc4_classes], axis=1)
combats_df = pd.concat([combats_df, pc5_classes], axis=1)
combats_df = pd.concat([combats_df, pc6_classes], axis=1)
combats_df = pd.concat([combats_df, pc7_classes], axis=1)



combats_df = combats_df.drop([
    "pc1_class",
    "pc2_class",
    "pc3_class",
    "pc4_class",
    "pc5_class",
    "pc6_class",
    "pc7_class"
], axis=1)


fig = plt.figure(figsize=(16, 16))
plt.hist(combats_df["difficulty"])
plt.savefig("difficulty_original_hist.jpg")


binned_difficulty = []

for i in range(len(combats_df["difficulty"])):
    if combats_df["difficulty"][i] in [0, 1]:
        binned_difficulty.append(0)
    elif combats_df["difficulty"][i] in [2, 3]:
        binned_difficulty.append(1)
    elif combats_df["difficulty"][i] in [4, 5]:
        binned_difficulty.append(2)
    elif combats_df["difficulty"][i] in [6, 7]:
        binned_difficulty.append(3)
    elif combats_df["difficulty"][i] in [8, 9]:
        binned_difficulty.append(4)

combats_df["difficulty"] = binned_difficulty

fig = plt.figure(figsize=(16, 16))
plt.hist(combats_df["difficulty"])
plt.savefig("difficulty_binned_hist.jpg")

combats_df.to_csv("../../data/processed/combats_df.csv")

print("----------------------- FIN ---------------------")