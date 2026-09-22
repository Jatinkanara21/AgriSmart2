"""Training entry point for the AgriSmart crop recommendation model.

Expected dataset columns:
N, P, K, temperature, humidity, ph, rainfall, label
"""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
TARGET = "label"

def train(dataset_path: str, model_path: str):
    df = pd.read_csv(dataset_path)
    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return accuracy

if __name__ == "__main__":
    print("Provide a dataset path to train the crop recommendation model.")
