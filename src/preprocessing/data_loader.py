import pandas as pd
from pathlib import Path

RAW_DATA = Path("data/raw")


class DataLoader:

    def load_daily_activity(self):
        return pd.read_csv(RAW_DATA / "dailyActivity_merged.csv")

    def load_sleep(self):
        return pd.read_csv(RAW_DATA / "sleepDay_merged.csv")

    def load_weight(self):
        return pd.read_csv(RAW_DATA / "weightLogInfo_merged.csv")

    def load_heart_rate(self):
        return pd.read_csv(RAW_DATA / "heartrate_seconds_merged.csv")

    def load_steps(self):
        return pd.read_csv(RAW_DATA / "dailySteps_merged.csv")