import pandas as pd


class DataValidator:

    REQUIRED_COLUMNS = [
        "Id",
        "ActivityDate",
        "TotalSteps",
        "Calories"
    ]

    def validate_activity(self, df):

        # Check required columns
        for column in self.REQUIRED_COLUMNS:
            if column not in df.columns:
                raise ValueError(f"Missing required column: {column}")

        # Check for missing values
        if df.isnull().sum().sum() > 0:
            raise ValueError("Dataset contains missing values.")

        # Check for negative values
        if (df["TotalSteps"] < 0).any():
            raise ValueError("Negative steps found.")

        if (df["Calories"] < 0).any():
            raise ValueError("Negative calories found.")

        print("✅ Dataset validation passed.")

        return True