import os
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model.

    Parameters:
        model : Trained model
        X_test : Testing features
        y_test : True labels
    """

    print("\n" + "=" * 50)
    print("MODEL EVALUATION")
    print("=" * 50)

    # Predict
    y_pred = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, y_pred)

    print(f"\nModel Accuracy : {accuracy * 100:.2f}%")

    # Classification Report
    print("\nClassification Report\n")
    print(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    # Create images folder
    os.makedirs("images", exist_ok=True)

    plt.figure(figsize=(6,5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=model.classes_,
        yticklabels=model.classes_
    )

    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    plt.tight_layout()

    plt.savefig("images/confusion_matrix.png")

    plt.close()

    print("Confusion Matrix saved as images/confusion_matrix.png")