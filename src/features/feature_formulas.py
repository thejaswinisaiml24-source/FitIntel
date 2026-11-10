class FeatureFormulas:

    @staticmethod
    def calculate_fitness_score(steps):

        if steps >= 12000:
            return 100

        elif steps >= 10000:
            return 90

        elif steps >= 8000:
            return 75

        elif steps >= 6000:
            return 60

        elif steps >= 4000:
            return 40

        else:
            return 20


    @staticmethod
    def calculate_activity_level(steps):

        if steps < 5000:
            return "Sedentary"

        elif steps < 7500:
            return "Low Active"

        elif steps < 10000:
            return "Moderately Active"

        elif steps < 12500:
            return "Active"

        else:
            return "Highly Active"