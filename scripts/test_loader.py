from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator

from src.features.feature_pipeline import FeaturePipeline

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

activity = loader.load_daily_activity()

print("Original Shape:", activity.shape)

activity = cleaner.clean_activity(activity)

validator.validate_activity(activity)

activity = pipeline.run(activity)

print(activity.head())

print(activity[[
    "TotalSteps",
    "FitnessScore",
    "ActivityLevel"
]].head())