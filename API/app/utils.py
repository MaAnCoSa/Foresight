from pydantic import BaseModel, Field
from fastapi import Request
import pandas as pd

class CombatInput (BaseModel):
    pc1_hp_max: float
    pc1_ac: float
    pc1_STR: float
    pc1_DEX: float
    pc1_CON: float
    pc1_INT: float
    pc1_WIS: float
    pc1_CHA: float
    pc2_hp_max: float
    pc2_ac: float
    pc2_STR: float
    pc2_DEX: float
    pc2_CON: float
    pc2_INT: float
    pc2_WIS: float
    pc2_CHA: float
    pc3_hp_max: float
    pc3_ac: float
    pc3_STR: float
    pc3_DEX: float
    pc3_CON: float
    pc3_INT: float
    pc3_WIS: float
    pc3_CHA: float
    pc4_hp_max: float
    pc4_ac: float
    pc4_STR: float
    pc4_DEX: float
    pc4_CON: float
    pc4_INT: float
    pc4_WIS: float
    pc4_CHA: float
    pc5_hp_max: float
    pc5_ac: float
    pc5_STR: float
    pc5_DEX: float
    pc5_CON: float
    pc5_INT: float
    pc5_WIS: float
    pc5_CHA: float
    pc6_hp_max: float
    pc6_ac: float
    pc6_STR: float
    pc6_DEX: float
    pc6_CON: float
    pc6_INT: float
    pc6_WIS: float
    pc6_CHA: float
    pc7_hp_max: float
    pc7_ac: float
    pc7_STR: float
    pc7_DEX: float
    pc7_CON: float
    pc7_INT: float
    pc7_WIS: float
    pc7_CHA: float
    monster1_cr: float
    monster1_hp_max: float
    monster1_ac: float
    monster1_STR: float
    monster1_DEX: float
    monster1_CON: float
    monster1_INT: float
    monster1_WIS: float
    monster1_CHA: float
    monster2_cr: float
    monster2_hp_max: float
    monster2_ac: float
    monster2_STR: float
    monster2_DEX: float
    monster2_CON: float
    monster2_INT: float
    monster2_WIS: float
    monster2_CHA: float
    monster3_cr: float
    monster3_hp_max: float
    monster3_ac: float
    monster3_STR: float
    monster3_DEX: float
    monster3_CON: float
    monster3_INT: float
    monster3_WIS: float
    monster3_CHA: float
    monster4_cr: float
    monster4_hp_max: float
    monster4_ac: float
    monster4_STR: float
    monster4_DEX: float
    monster4_CON: float
    monster4_INT: float
    monster4_WIS: float
    monster4_CHA: float
    monster5_cr: float
    monster5_hp_max: float
    monster5_ac: float
    monster5_STR: float
    monster5_DEX: float
    monster5_CON: float
    monster5_INT: float
    monster5_WIS: float
    monster5_CHA: float
    monster6_cr: float
    monster6_hp_max: float
    monster6_ac: float
    monster6_STR: float
    monster6_DEX: float
    monster6_CON: float
    monster6_INT: float
    monster6_WIS: float
    monster6_CHA: float
    monster7_cr: float
    monster7_hp_max: float
    monster7_ac: float
    monster7_STR: float
    monster7_DEX: float
    monster7_CON: float
    monster7_INT: float
    monster7_WIS: float
    monster7_CHA: float
    num_pcs: int
    num_monsters: int
    pc_lvl: int
    pc1_class_Barbarian: int
    pc1_class_Bard: int
    pc1_class_FighterStr: int
    pc2_class_none : int = Field(alias="pc2_class_-")
    pc2_class_Barbarian: int
    pc2_class_Bard : int
    pc2_class_FighterStr : int
    pc3_class_none: int = Field(alias="pc3_class_-")
    pc3_class_Barbarian : int
    pc3_class_Bard : int
    pc3_class_FighterStr : int
    pc4_class_none : int = Field(alias="pc4_class_-")
    pc4_class_Barbarian: int
    pc4_class_Bard: int
    pc4_class_FighterStr: int
    pc5_class_none : int = Field(alias="pc5_class_-")
    pc5_class_Barbarian : int
    pc5_class_Bard: int
    pc5_class_FighterStr: int
    pc6_class_none : int = Field(alias="pc6_class_-")
    pc6_class_Barbarian: int
    pc6_class_Bard: int
    pc6_class_FighterStr: int
    pc7_class_none: int = Field(alias="pc7_class_-")
    pc7_class_Barbarian: int
    pc7_class_Bard: int
    pc7_class_FighterStr: int

def predict_with_model(request: Request, input_data: CombatInput):
    if isinstance(input_data, CombatInput):
        combat_dict = input_data.model_dump()
    else:
        raise ValueError("Input debe ser de tipo CombatInput")
    
    df = pd.DataFrame([combat_dict])
    df.columns = [col.replace('_class_none', '_class_-') for col in df.columns]

    model = request.app.state.model

    if ( request.app.state.model_name == 'CatBoost_Classifier' ):
        df = standar_scaler(df, estandarizar_catboost)

    prediction = model.predict(df)

    return { "prediccion": int(prediction[0]) }

def standar_scaler (df, stats):
    for col, (mean, std) in stats.items():
        if col in df.columns:
            df[col] = (df[col] - mean) / std
    return df

estandarizar_catboost = {
    "pc1_hp_max": [
        27.285395833333332,
        13.967613336976333
    ],
    "pc1_ac": [
        11.823904166666667,
        1.886378188715933
    ],
    "pc2_hp_max": [
        23.425329166666668,
        16.08096858126233
    ],
    "pc2_ac": [
        10.160104166666667,
        4.487798767939544
    ],
    "pc3_hp_max": [
        19.52359166666667,
        17.104678174526683
    ],
    "pc3_ac": [
        8.454633333333334,
        5.577410017757862
    ],
    "pc4_hp_max": [
        15.667252083333333,
        17.19269105997055
    ],
    "pc4_ac": [
        6.775045833333333,
        6.025820865503991
    ],
    "pc5_hp_max": [
        11.721391666666667,
        16.341965037021247
    ],
    "pc5_ac": [
        5.07193125,
        5.985225429591655
    ],
    "pc6_hp_max": [
        7.8162416666666665,
        14.44589117359864
    ],
    "pc6_ac": [
        3.38420625,
        5.44311868614903
    ],
    "pc7_hp_max": [
        3.9436375,
        11.028354251043316
    ],
    "pc7_ac": [
        1.6944916666666667,
        4.208825734439064
    ],
    "monster1_hp_max": [
        38.87037083333333,
        32.972647547167725
    ],
    "monster1_ac": [
        12.761397916666667,
        2.3289024443682487
    ],
    "monster2_hp_max": [
        33.56585416666667,
        33.72384775792011
    ],
    "monster2_ac": [
        10.972204166666666,
        4.954747239077865
    ],
    "monster3_hp_max": [
        27.827677083333334,
        32.90160716140695
    ],
    "monster3_ac": [
        9.131816666666667,
        6.08443586747957
    ],
    "monster4_hp_max": [
        22.32014375,
        31.717998270615734
    ],
    "monster4_ac": [
        7.272479166666667,
        6.561018641815029
    ],
    "monster5_hp_max": [
        16.600264583333335,
        28.815168491045835
    ],
    "monster5_ac": [
        5.44805625,
        6.488944924653182
    ],
    "monster6_hp_max": [
        11.086983333333333,
        24.852054991174942
    ],
    "monster6_ac": [
        3.6402958333333335,
        5.89564404112094
    ],
    "monster7_hp_max": [
        5.678497916666666,
        18.766240669128145
    ],
    "monster7_ac": [
        1.83526875,
        4.5614558947343244
    ],
    "pc1_STR": [
        2.8937375,
        1.8375262761317497
    ],
    "pc1_DEX": [
        0.62634375,
        1.3377684099100517
    ],
    "pc1_CON": [
        2.044102083333333,
        1.4630515651639717
    ],
    "pc1_INT": [
        0.6294770833333333,
        1.3386645403556332
    ],
    "pc1_WIS": [
        0.6278833333333333,
        1.3370129931667412
    ],
    "pc1_CHA": [
        1.6096020833333333,
        1.9803397571205377
    ],
    "pc2_STR": [
        2.4832625,
        1.9759414608767603
    ],
    "pc2_DEX": [
        0.5392104166666667,
        1.2601038388177923
    ],
    "pc2_CON": [
        1.7499354166666667,
        1.5330782271889343
    ],
    "pc2_INT": [
        0.5395708333333333,
        1.2579646044194206
    ],
    "pc2_WIS": [
        0.54030625,
        1.2594623366958912
    ],
    "pc2_CHA": [
        1.3869166666666666,
        1.9210367898660297
    ],
    "pc3_STR": [
        2.0716520833333334,
        2.030315447616624
    ],
    "pc3_DEX": [
        0.4476291666666667,
        1.1641868203838495
    ],
    "pc3_CON": [
        1.4628104166666667,
        1.5437363439813108
    ],
    "pc3_INT": [
        0.44775625,
        1.166686230167529
    ],
    "pc3_WIS": [
        0.44710833333333333,
        1.164816279472532
    ],
    "pc3_CHA": [
        1.1537270833333333,
        1.8265364357183806
    ],
    "pc4_STR": [
        1.6635166666666668,
        1.9980896586015133
    ],
    "pc4_DEX": [
        0.3601958333333333,
        1.0595630233983517
    ],
    "pc4_CON": [
        1.1726958333333333,
        1.4997449788954873
    ],
    "pc4_INT": [
        0.35899375,
        1.0598952359384013
    ],
    "pc4_WIS": [
        0.3591083333333333,
        1.0577303700614924
    ],
    "pc4_CHA": [
        0.92095625,
        1.6961665590274477
    ],
    "pc5_STR": [
        1.2456083333333334,
        1.8732726774269004
    ],
    "pc5_DEX": [
        0.2724875,
        0.9296158863014067
    ],
    "pc5_CON": [
        0.8779020833333333,
        1.3937607622656074
    ],
    "pc5_INT": [
        0.26730208333333333,
        0.9278600683856545
    ],
    "pc5_WIS": [
        0.26809791666666666,
        0.9282949705524964
    ],
    "pc5_CHA": [
        0.6879604166666666,
        1.5184273174827925
    ],
    "pc6_STR": [
        0.8261791666666667,
        1.636565325446438
    ],
    "pc6_DEX": [
        0.17964375,
        0.7684821208693636
    ],
    "pc6_CON": [
        0.581575,
        1.2104624757706293
    ],
    "pc6_INT": [
        0.17874166666666666,
        0.770594026522478
    ],
    "pc6_WIS": [
        0.1808625,
        0.7703911295941018
    ],
    "pc6_CHA": [
        0.4660166666666667,
        1.2907405254008346
    ],
    "pc7_STR": [
        0.4175833333333333,
        1.2360008801615348
    ],
    "pc7_DEX": [
        0.09063958333333333,
        0.5531422541833725
    ],
    "pc7_CON": [
        0.29376875,
        0.9062603834337712
    ],
    "pc7_INT": [
        0.08874791666666666,
        0.5485904826033605
    ],
    "pc7_WIS": [
        0.08836666666666666,
        0.5481714679250782
    ],
    "pc7_CHA": [
        0.22696458333333333,
        0.9305371021812429
    ],
    "monster1_STR": [
        1.33130625,
        2.4586481744429936
    ],
    "monster1_DEX": [
        1.109825,
        1.5141380647046903
    ],
    "monster1_CON": [
        1.4352020833333334,
        1.265036388405307
    ],
    "monster1_INT": [
        -2.095475,
        2.2028700144812507
    ],
    "monster1_WIS": [
        0.21053125,
        1.155435613706929
    ],
    "monster1_CHA": [
        -1.3325104166666666,
        2.0795888013206176
    ],
    "monster2_STR": [
        1.13945,
        2.3307988649385094
    ],
    "monster2_DEX": [
        0.9623520833333333,
        1.4642409925876851
    ],
    "monster2_CON": [
        1.241475,
        1.277719932363428
    ],
    "monster2_INT": [
        -1.79395625,
        2.1746713335374857
    ],
    "monster2_WIS": [
        0.19090625,
        1.0859370809741098
    ],
    "monster2_CHA": [
        -1.1379895833333333,
        1.9934743716937957
    ],
    "monster3_STR": [
        0.9582833333333334,
        2.1606274810890103
    ],
    "monster3_DEX": [
        0.7875708333333333,
        1.3939791596134397
    ],
    "monster3_CON": [
        1.0321375,
        1.2452441172633508
    ],
    "monster3_INT": [
        -1.4961833333333334,
        2.0901392380596224
    ],
    "monster3_WIS": [
        0.15182083333333332,
        0.9930835761306964
    ],
    "monster3_CHA": [
        -0.9545083333333333,
        1.8597681882340766
    ],
    "monster4_STR": [
        0.7569770833333334,
        1.9672654476250244
    ],
    "monster4_DEX": [
        0.6323958333333334,
        1.2761252169549857
    ],
    "monster4_CON": [
        0.8243875,
        1.1976820967736361
    ],
    "monster4_INT": [
        -1.18808125,
        1.9557964266352978
    ],
    "monster4_WIS": [
        0.12243541666666667,
        0.8871001211162479
    ],
    "monster4_CHA": [
        -0.7561604166666667,
        1.698181728269177
    ],
    "monster5_STR": [
        0.564375,
        1.737378191763251
    ],
    "monster5_DEX": [
        0.47361875,
        1.1290346253828563
    ],
    "monster5_CON": [
        0.6122416666666667,
        1.0865101323263306
    ],
    "monster5_INT": [
        -0.8948854166666667,
        1.7739131593186228
    ],
    "monster5_WIS": [
        0.09152708333333333,
        0.76162726109408
    ],
    "monster5_CHA": [
        -0.5683270833333334,
        1.5113124543982541
    ],
    "monster6_STR": [
        0.3745125,
        1.4458802656850192
    ],
    "monster6_DEX": [
        0.3171833333333333,
        0.9671806183707957
    ],
    "monster6_CON": [
        0.410325,
        0.9359274647600228
    ],
    "monster6_INT": [
        -0.5994375,
        1.517938673732968
    ],
    "monster6_WIS": [
        0.058520833333333334,
        0.6318830144031978
    ],
    "monster6_CHA": [
        -0.38437083333333333,
        1.2669023533745276
    ],
    "monster7_STR": [
        0.189825,
        1.0515593689424474
    ],
    "monster7_DEX": [
        0.16019791666666666,
        0.7120818776928516
    ],
    "monster7_CON": [
        0.2086,
        0.6952933772769359
    ],
    "monster7_INT": [
        -0.29686666666666667,
        1.1057735887546254
    ],
    "monster7_WIS": [
        0.030964583333333334,
        0.4488294378291642
    ],
    "monster7_CHA": [
        -0.18822291666666666,
        0.9102980885293914
    ]
}