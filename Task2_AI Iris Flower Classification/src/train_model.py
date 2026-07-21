import os
import joblib

from sklearn.ensemble import RandomForestClassifier


def train_model(X_train, y_train):
    """
    Train a Random Forest classifier.

    Parameters:
        X_train : Training features
        y_train : Training labels

    Returns:
        model : Trained model
    """

    print("\n" + "=" * 50)
    print("MODEL TRAINING")
    print("=" * 50)

    # Create Random Forest model
    model = RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )

    # Train the model
    model.fit(X_train, y_train)

    print("Model trained successfully.")

    # Create models folder if it doesn't exist
    os.makedirs("models", exist_ok=True)

    # Save model
    joblib.dump(model, "models/iris_classifier.pkl")

    print("Model saved to models/iris_classifier.pkl")

    return model