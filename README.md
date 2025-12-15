# End-to-End Customer Churn Predictor 🚀

A production-grade Machine Learning pipeline that predicts customer churn. Built with modular code, tracked with MLflow, served via FastAPI, and containerized with Docker.

## 🛠️ Tech Stack
* **Model:** Random Forest / XGBoost
* **Tracking:** MLflow
* **API:** FastAPI
* **Containerization:** Docker

## 📂 Project Structure
* `src/`: Modular code for training and inference.
* `models/`: Serialized model files.
* `notebooks/`: EDA and experiments.

## 🚀 How to Run
1.  Install dependencies: `pip install -r requirements.txt`
2.  Train model: `python src/train.py`
3.  Start API: `uvicorn src.app:app --reload`
