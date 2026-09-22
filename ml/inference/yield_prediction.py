import joblib

FEATURES = ["area_acres", "rainfall", "temperature", "soil_ph"]

class YieldPredictionModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, values: dict):
        row = [[values[name] for name in FEATURES]]
        return float(self.model.predict(row)[0])
