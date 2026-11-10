import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline


class GoalAchievementModel:

    def train(self):

        loader = DataLoader()
        cleaner = DataCleaner()
        validator = DataValidator()
        pipeline = FeaturePipeline()

        df = loader.load_daily_activity()
        df = cleaner.clean_activity(df)
        validator.validate_activity(df)
        df = pipeline.run(df)

        df["GoalAchieved"] = (df["TotalSteps"] >= 10000).astype(int)

        X = df[
            [
                "TotalDistance",
                "VeryActiveMinutes",
                "FairlyActiveMinutes",
                "LightlyActiveMinutes",
                "SedentaryMinutes",
                "Calories",
            ]
        ]

        y = df["GoalAchieved"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42
        )

        model = RandomForestClassifier(
            n_estimators=100,
            random_state=42
        )

        model.fit(X_train, y_train)

        os.makedirs("models/goal_achievement", exist_ok=True)

        joblib.dump(
            model,
            "models/goal_achievement/goal_model.pkl"
        )

        return model, X_test, y_test