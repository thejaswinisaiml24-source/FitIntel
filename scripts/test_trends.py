from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline
from src.analytics.trend_analysis import TrendAnalyzer

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

activity = loader.load_daily_activity()
activity = cleaner.clean_activity(activity)
validator.validate_activity(activity)
activity = pipeline.run(activity)

print("\nDaily Steps")
print(TrendAnalyzer.daily_steps(activity).head())

print("\nDaily Calories")
print(TrendAnalyzer.daily_calories(activity).head())

print("\nDaily Fitness Score")
print(TrendAnalyzer.daily_fitness_score(activity).head())