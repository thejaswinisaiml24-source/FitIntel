import matplotlib.pyplot as plt

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

steps = TrendAnalyzer.daily_steps(activity)

plt.figure(figsize=(12,6))
plt.plot(
    steps["ActivityDate"],
    steps["TotalSteps"],
    marker="o"
)

plt.title("Daily Steps Trend")
plt.xlabel("Date")
plt.ylabel("Steps")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()