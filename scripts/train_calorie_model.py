from src.ml.calorie_prediction_model import CaloriePredictionModel
from src.ml.regression_evaluator import RegressionEvaluator

trainer = CaloriePredictionModel()

model, X_test, y_test = trainer.train()

RegressionEvaluator.evaluate(
    model,
    X_test,
    y_test
)