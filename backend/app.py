from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))


class LoanData(BaseModel):
    RevolvingUtilizationOfUnsecuredLines: float
    age: int
    NumberOfTime3059DaysPastDueNotWorse: int
    DebtRatio: float
    MonthlyIncome: float
    NumberOfOpenCreditLinesAndLoans: int
    NumberOfTimes90DaysLate: int
    NumberRealEstateLoansOrLines: int
    NumberOfTime6089DaysPastDueNotWorse: int
    NumberOfDependents: float

@app.get("/")
def home():
    return {"message": "Welcome to CreditShield API!"}

@app.post("/predict")
def predict(loan_data: LoanData):
        input_data = np.array([
        [
            loan_data.RevolvingUtilizationOfUnsecuredLines,
            loan_data.age,
            loan_data.NumberOfTime3059DaysPastDueNotWorse,
            loan_data.DebtRatio,
            loan_data.MonthlyIncome,
            loan_data.NumberOfOpenCreditLinesAndLoans,
            loan_data.NumberOfTimes90DaysLate,
            loan_data.NumberRealEstateLoansOrLines,
            loan_data.NumberOfTime6089DaysPastDueNotWorse,
            loan_data.NumberOfDependents
        ]
        ])
        scaled_input = scaler.transform(input_data)
        probability = model.predict_proba(scaled_input)[0][1]
        return {"default_probability": float(probability)}

