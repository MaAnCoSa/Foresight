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
    prediction = model.predict(df)

    return { "prediccion": int(prediction[0]) }