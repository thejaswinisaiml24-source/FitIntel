from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline
from src.analytics.kpi_generator import KPIGenerator

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

activity = loader.load_daily_activity()
activity = cleaner.clean_activity(activity)
validator.validate_activity(activity)
activity = pipeline.run(activity)

print("Average Steps:", KPIGenerator.average_steps(activity))
print("Average Calories:", KPIGenerator.average_calories(activity))
print("Average Distance:", KPIGenerator.average_distance(activity))
print("Average Sedentary Minutes:", KPIGenerator.average_sedentary_minutes(activity))
print("Maximum Steps:", KPIGenerator.max_steps(activity))
print("Minimum Steps:", KPIGenerator.min_steps(activity))