from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)


class ModelEvaluator:

    @staticmethod
    def evaluate(model, X_test, y_test):

        predictions = model.predict(X_test)

        print("Accuracy:",
              accuracy_score(y_test, predictions))

        print("\nConfusion Matrix")

        print(confusion_matrix(y_test, predictions))

        print("\nClassification Report")

        print(classification_report(y_test, predictions))