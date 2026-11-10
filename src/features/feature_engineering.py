from src.features.feature_formulas import FeatureFormulas


class FeatureEngineering:

    def create_features(self, df):

        df["FitnessScore"] = df["TotalSteps"].apply(
            FeatureFormulas.calculate_fitness_score
        )

        df["ActivityLevel"] = df["TotalSteps"].apply(
            FeatureFormulas.calculate_activity_level
        )

        return df