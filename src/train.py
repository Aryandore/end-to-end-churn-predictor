import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import LabelEncoder
import mlflow
import mlflow.sklearn
from load_data import load_data 

def train_model(data_path):
    # 1. Load Data
    df = load_data(data_path)
    
    # 2. Preprocess (Same as before)
    le = LabelEncoder()
    df['Churn'] = le.fit_transform(df['Churn'])
    X = df.select_dtypes(include=['number']).drop('Churn', axis=1)
    y = df['Churn']
    
    # 3. Splitc  
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # --- MLFLOW STARTS HERE ---
    # Set the experiment name (creates it if it doesn't exist)
    mlflow.set_experiment("Telco_Churn_Experiment")

    # Start a "Run" (like starting a stopwatch for this specific attempt)
    with mlflow.start_run():
        
        # Define Hyperparameters
        n_estimators = 100
        max_depth = 10
        
        # Log the Hyperparameters (Inputs)
        mlflow.log_param("n_estimators", n_estimators)
        mlflow.log_param("max_depth", max_depth)
        
        print("Training model...")
        clf = RandomForestClassifier(n_estimators=n_estimators, max_depth=max_depth)
        clf.fit(X_train, y_train)
        
        # Predictions
        y_pred = clf.predict(X_test)
        
        # Calculate Metrics
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        
        # Log the Metrics (Outputs)
        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", prec)
        
        # Log the actual Model
        mlflow.sklearn.log_model(clf, "random_forest_model")
        
        print(f"✅ Run Complete. Accuracy: {acc}")

if __name__ == "__main__":
    DATA_PATH = "data/Telco-Customer-Churn.csv"
    train_model(DATA_PATH)