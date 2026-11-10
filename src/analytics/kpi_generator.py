class KPIGenerator:

    @staticmethod
    def average_steps(df):
        return round(df["TotalSteps"].mean(), 2)

    @staticmethod
    def average_calories(df):
        return round(df["Calories"].mean(), 2)

    @staticmethod
    def average_distance(df):
        return round(df["TotalDistance"].mean(), 2)

    @staticmethod
    def average_sedentary_minutes(df):
        return round(df["SedentaryMinutes"].mean(), 2)

    @staticmethod
    def max_steps(df):
        return int(df["TotalSteps"].max())

    @staticmethod
    def min_steps(df):
        return int(df["TotalSteps"].min())