"""
Prediction module for crop recommendation.

This module handles the lazy loading of the Random Forest model
and exposes the main 'predict' function to perform inference on
soil and climate features.
"""
import joblib
import os
import pandas as pd
from typing import List, Any
import numpy as np

# Definition of the absolute path to the model.
# __file__ points to the current module. This ensures the model path
# ('random_forest_model.joblib') is resolved correctly regardless of
# where the Flask server is executed from.
model_path = os.path.join(os.path.dirname(__file__), 'random_forest_model.joblib')

# Global variable to store the model instance.
# Initially set to None. This allows for loading the model only once
# the first time 'load_model' is called (simple Singleton pattern).
_model = None


def load_model(path: str):
    """
    Loads the Machine Learning model from the specified path.

    Implements lazy loading to ensure the model is loaded into memory
    only once during the server's lifecycle.

    Args:
        path: The full path to the serialized model file (.joblib).

    Returns:
        The loaded ML model object (e.g., sklearn Random Forest).

    Raises:
        FileNotFoundError: If the model file does not exist at the path.
    """
    global _model
    # Checks if the model is already loaded. If so, returns it immediately.
    if _model is not None:
        return _model

    # CRITICAL CHECK: Verifies file existence before attempting to load.
    if not os.path.exists(path):
        # NOTE: Using 'raise' in the ML module allows the Flask server to handle
        # the exception during initialization, preventing silent failures in production.
        raise FileNotFoundError(f"Model file not found at: {path}")

    # Loads the model and stores it in the global variable.
    print(f"INFO: Loading ML model from {path}...")
    _model = joblib.load(path)
    print("INFO: Model loaded successfully.")
    return _model


def predict(data: List[List[float]]) -> List[Any]:
    """
    Performs a prediction using the loaded model.

    This is the main entry point for the Flask server.

    Args:
        data: A list of lists containing the feature vectors
              (e.g., [[N, P, K, temp, hum, ph, rainfall]]).

    Returns:
        A list of predictions (the recommended crop labels).

    Raises:
        ValueError: If the input data cannot be converted to a valid format.
    """
    # 1. Model Loading: Uses 'load_model', leveraging the
    #    lazy loading mechanism ('_model' global).
    model = load_model(model_path)

    # 2. Data Preprocessing (Robustness Improvement):
    #    While the model might accept lists, converting input to a NumPy array
    #    is a best practice to ensure compatibility and efficiency with most
    #    ML frameworks (sklearn, etc.).
    try:
        input_array = np.array(data, dtype=np.float32)
    except Exception as e:
        # Error handling if data is not convertible (e.g., contains strings).
        raise ValueError(f"Error converting input data to NumPy array. Detail: {e}")

    # 3. Inference: The ML model's 'predict' method.
    predictions = model.predict(input_array)

    # 4. Post-processing: Converts the NumPy array of predictions back
    #    to a standard Python list before returning it to the server.
    return predictions.tolist()