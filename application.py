from fastapi import FastAPI
from fastapi.responses import JSONResponse

import pickle
import pandas as pd

from schema.user_input import UserInput 

with open (r"C:\Users\Prithviraj\Desktop\all project\project_for_fast\loan_approval.pkl","rb") as f:
    model=pickle.load(f)

app=FastAPI()


    
@app.post("/predict")
def predict_premium(data:UserInput):
    input_df=pd.DataFrame([{"income":data.income,
                   "age":data.age,
                   "loan":data.loan
                   }])
    prediction=model.predict(input_df)[0]
    return JSONResponse(status_code=200,content={"prediction_category":int(prediction)})


