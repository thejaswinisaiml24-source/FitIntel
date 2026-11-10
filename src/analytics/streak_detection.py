class StreakDetector:

    STEP_GOAL = 10000

    @staticmethod
    def longest_streak(df):

        steps = df["TotalSteps"]

        streak = 0
        longest = 0

        for value in steps:

            if value >= StreakDetector.STEP_GOAL:
                streak += 1
                longest = max(longest, streak)
            else:
                streak = 0

        return longest