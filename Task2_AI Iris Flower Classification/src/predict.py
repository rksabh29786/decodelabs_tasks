import joblib
import numpy as np


def load_model(model_path):
    """
    Load trained model from file.
    """

    model = joblib.load(model_path)

    print("Model loaded successfully.")

    return model



def predict_flower(model, flower_data):
    """
    Predict Iris flower species.
    """

    # Convert input into numpy array
    flower_data = np.array(flower_data).reshape(1, -1)

    prediction = model.predict(flower_data)

    return prediction[0]