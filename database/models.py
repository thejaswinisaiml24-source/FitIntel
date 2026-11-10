from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date
)

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class DailyActivity(Base):

    __tablename__ = "daily_activity"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer)

    activity_date = Column(Date)

    total_steps = Column(Integer)

    calories = Column(Integer)

    fitness_score = Column(Integer)

    activity_level = Column(String)

    total_distance = Column(Float)

    sedentary_minutes = Column(Integer)