import pandas as pd


class DataCleaner:

    def clean_activity(self, df):

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Convert date column
        df["ActivityDate"] = pd.to_datetime(df["ActivityDate"])

        # Remove rows with missing values
        df = df.dropna()

        return df