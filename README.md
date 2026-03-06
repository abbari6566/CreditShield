# CreditShield

CreditShield is a loan default risk predictor. It takes basic borrower credit features and returns the estimated probability that the borrower may default.
Note: Default means the borrower fails to make required loan payments on time.

## What the Project Does

The app lets a user enter credit-related inputs in a web form, then sends those values to a backend prediction API. The API runs a trained machine learning model and returns a default probability score.

Main use case:

- Quick risk estimation from structured financial/credit inputs

## How It Works

1. User fills in borrower features in the frontend form.
2. Frontend sends a `POST` request to `http://127.0.0.1:8000/predict`.
3. Backend loads a trained model and scaler (`model.pkl`, `scaler.pkl`).
4. Input is transformed and passed into the model.
5. Backend returns predicted default probability as JSON.
6. Frontend displays the percentage result.

## How It Is Built

Frontend:

- HTML (`frontend/index.html`)
- CSS (`frontend/style.css`)
- JavaScript (`frontend/script.js`)

Backend:

- Python (FastAPI)
- Model inference endpoint in `backend/app.py`
- Serialized ML artifacts: `backend/model.pkl`, `backend/scaler.pkl`
- ML model used is LogisticRegression

Data & training assets:

- Training data: `backend/training.csv`
- Notebook: `backend/train_model.ipynb`
- Dataset source: [Kaggle Give Me Some Credit](https://www.kaggle.com/c/GiveMeSomeCredit)

## Running the Project

Backend:

1. Open a terminal in `backend/`.
2. Activate your virtual environment.
3. Start the API server (example):
   - `uvicorn app:app --reload --port 8000`

Frontend:

1. Serve the `frontend/` folder (for example with VS Code Live Server).
2. Open `frontend/index.html` in the browser.

Make sure backend is running on `127.0.0.1:8000` before requesting predictions.

## Demo

![CreditShield Demo](docs/demo.png)

A result like `74.1% default` means the model estimates about a 74.1% chance that this borrower profile will default, and a 25.9% chance of not defaulting.
