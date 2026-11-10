from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline
from src.analytics.goal_tracking import GoalTracker

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

activity = loader.load_daily_activity()
activity = cleaner.clean_activity(activity)
validator.validate_activity(activity)
activity = pipeline.run(activity)

print("Step Goal Achievement %:",
      GoalTracker.step_goal_percentage(activity))

print("Calories Goal Achievement %:",
      GoalTracker.calorie_goal_percentage(activity))

print("Goal Achieved Days:",
      GoalTracker.total_goal_days(activity))

print("Missed Days:",
      GoalTracker.missed_goal_days(activity))