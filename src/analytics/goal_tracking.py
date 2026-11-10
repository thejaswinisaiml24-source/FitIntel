class GoalTracker:

    STEP_GOAL = 10000
    CALORIE_GOAL = 2200

    @staticmethod
    def step_goal_percentage(df):

        achieved = (df["TotalSteps"] >= GoalTracker.STEP_GOAL).sum()

        return round((achieved / len(df)) * 100, 2)

    @staticmethod
    def calorie_goal_percentage(df):

        achieved = (df["Calories"] >= GoalTracker.CALORIE_GOAL).sum()

        return round((achieved / len(df)) * 100, 2)

    @staticmethod
    def total_goal_days(df):

        return (df["TotalSteps"] >= GoalTracker.STEP_GOAL).sum()

    @staticmethod
    def missed_goal_days(df):

        return (df["TotalSteps"] < GoalTracker.STEP_GOAL).sum()