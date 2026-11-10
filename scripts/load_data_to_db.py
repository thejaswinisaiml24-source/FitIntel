from src.preprocessing.data_loader import DataLoader
from src.preprocessing.data_cleaner import DataCleaner
from src.preprocessing.data_validator import DataValidator
from src.features.feature_pipeline import FeaturePipeline

from database.models import DailyActivity
from database.db_connection import SessionLocal

loader = DataLoader()
cleaner = DataCleaner()
validator = DataValidator()
pipeline = FeaturePipeline()

# Load dataset
activity = loader.load_daily_activity()

# Clean
activity = cleaner.clean_activity(activity)

# Validate
validator.validate_activity(activity)

# Feature Engineering
activity = pipeline.run(activity)

# Connect Database
session = SessionLocal()

# Insert every row
for _, row in activity.iterrows():

    record = DailyActivity(

        user_id=int(row["Id"]),
        activity_date=row["ActivityDate"].date(),
        total_steps=int(row["TotalSteps"]),
        calories=int(row["Calories"]),
        fitness_score=int(row["FitnessScore"]),
        activity_level=row["ActivityLevel"],
        total_distance=float(row["TotalDistance"]),
        sedentary_minutes=int(row["SedentaryMinutes"])

    )

    session.add(record)

session.commit()

session.close()

print("✅ Data inserted successfully!")