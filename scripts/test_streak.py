from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline
from src.analytics.streak_detection import StreakDetector

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

activity = loader.load_daily_activity()
activity = cleaner.clean_activity(activity)
validator.validate_activity(activity)
activity = pipeline.run(activity)

print("Longest Step Streak:",
      StreakDetector.longest_streak(activity))