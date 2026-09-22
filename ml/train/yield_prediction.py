"""Train a baseline yield regression model."""
from pathlib import Path
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

FEATURES = ["area_acres", "rainfall", "temperature", "soil_ph"]
TARGET = "yield"

def train(dataset_path: str, model_path: str):
    df = pd.read_csv(dataset_path).dropna(subset=FEATURES + [TARGET])
    X = df[FEATURES]
    y = df[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=250, random_state=42)
    model.fit(X_train, y_train)
    mae = mean_absolute_error(y_test, model.predict(X_test))
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, model_path)
    return mae

if __name__ == "__main__":
    print("Use train(dataset_path, model_path) with an approved yield dataset.")
