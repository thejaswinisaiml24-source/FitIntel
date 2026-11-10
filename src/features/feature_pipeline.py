from src.features.feature_engineering import FeatureEngineering


class FeaturePipeline:

    def __init__(self):

        self.engineer = FeatureEngineering()

    def run(self, df):

        return self.engineer.create_features(df)