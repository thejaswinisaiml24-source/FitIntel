from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


class RegressionEvaluator:

    @staticmethod
    def evaluate(model, X_test, y_test):

        predictions = model.predict(X_test)

        print("\nModel Evaluation")
        print("----------------------------")
        print("MAE:", mean_absolute_error(y_test, predictions))
        print("MSE:", mean_squared_error(y_test, predictions))
        print("R² Score:", r2_score(y_test, predictions))