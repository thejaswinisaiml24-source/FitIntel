from src.ml.goal_achievement_model import GoalAchievementModel
from src.ml.model_evaluator import ModelEvaluator

trainer = GoalAchievementModel()

model, X_test, y_test = trainer.train()

ModelEvaluator.evaluate(
    model,
    X_test,
    y_test
)