import pandas as pd
import os

def load_data(filepath):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at {filepath}")
    
    df = pd.read_csv(filepath)
    print(f"✅ Data loaded successfully. Shape: {df.shape}")
    return df

if __name__ == "__main__":

    data = load_data("data\Telco-Customer-Churn.csv")
    