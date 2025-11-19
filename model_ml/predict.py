import joblib
import os
import pandas as pd

# Construir la ruta al modelo de forma robusta
model_path = os.path.join(os.path.dirname(__file__), 'random_forest_model.joblib')

def load_model(path):
    """Carga el modelo desde la ruta especificada."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo del modelo no se encontró en: {path}")
    return joblib.load(path)

def predict(data):
    """
    Realiza predicciones sobre nuevos datos.
    'data' debe ser un DataFrame de pandas con las mismas columnas que los datos de entrenamiento.
    """
    model = load_model(model_path)
    # Asegúrate de que las columnas de 'data' coincidan con las que el modelo espera
    # Por ejemplo: ['feature1', 'feature2', 'feature3']
    predictions = model.predict(data)
    return predictions