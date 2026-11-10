import os
import joblib

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline


class CaloriePredictionModel:

    def train(self):

        # Load dataset
        loader = DataLoader()
        cleaner = DataCleaner()
        validator = DataValidator()
        pipeline = FeaturePipeline()

        df = loader.load_daily_activity()
        df = cleaner.clean_activity(df)
        validator.validate_activity(df)
        df = pipeline.run(df)

        # Features
        X = df[
            [
                "TotalSteps",
                "TotalDistance",
                "VeryActiveMinutes",
                "FairlyActiveMinutes",
                "LightlyActiveMinutes",
                "SedentaryMinutes"
            ]
        ]

        # Target
        y = df["Calories"]

        # Split dataset
        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        # Train model
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        # Save model
        os.makedirs("models/calorie_prediction", exist_ok=True)

        joblib.dump(
            model,
            "models/calorie_prediction/calorie_model.pkl"
        )

        # Evaluate
        predictions = model.predict(X_test)

        print("MAE:", mean_absolute_error(y_test, predictions))
        print("MSE:", mean_squared_error(y_test, predictions))
        print("R² Score:", r2_score(y_test, predictions))

        return model, X_test, y_test