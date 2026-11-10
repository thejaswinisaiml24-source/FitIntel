import pandas as pd


class TrendAnalyzer:

    @staticmethod
    def daily_steps(df):
        return (
            df.groupby("ActivityDate")["TotalSteps"]
            .sum()
            .reset_index()
            .sort_values("ActivityDate")
        )

    @staticmethod
    def daily_calories(df):
        return (
            df.groupby("ActivityDate")["Calories"]
            .sum()
            .reset_index()
            .sort_values("ActivityDate")
        )

    @staticmethod
    def daily_distance(df):
        return (
            df.groupby("ActivityDate")["TotalDistance"]
            .sum()
            .reset_index()
            .sort_values("ActivityDate")
        )

    @staticmethod
    def daily_fitness_score(df):
        return (
            df.groupby("ActivityDate")["FitnessScore"]
            .mean()
            .reset_index()
            .sort_values("ActivityDate")
        )