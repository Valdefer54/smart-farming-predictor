"""
Flask server module for the crop recommendation application.

This module initializes a Flask application to serve a simple frontend
and expose an endpoint for making predictions using a Machine Learning model.
"""
import os
import sys
import webbrowser
from threading import Timer

from flask import Flask, render_template, request, jsonify

# Conditional import of the prediction module.
# The 'predict' module is expected to contain the core logic for loading the model
# and performing inference based on input data.
try:
    # NOTE: Assumes 'model_ml' is a package/directory at the same level
    # or accessible via the PYTHONPATH.
    from model_ml.predict import predict
except ImportError as e:
    # CRITICAL ERROR: The application cannot function without the model.
    # sys.exit(1) is used for a controlled shutdown, notifying a critical failure.
    print("CRITICAL ERROR: Prediction module not found or import failed.")
    print(f"Detail: {e}")
    sys.exit(1)


# Flask application initialization.
# The template_folder is explicitly specified to match the project's directory
# structure (e.g., 'ui/templates').
app = Flask(__name__, template_folder='ui/templates')

@app.route('/')
def home():
    """
    Main route ('/'). Serves the HTML user interface.

    Returns:
        str: The rendered HTML content of 'interface.html'.
        str: An error message if the template is not found.
    """
    try:
        # Attempt to render the main frontend template.
        return render_template('interface.html')
    except Exception as e:
        # Error handling if the template does not exist or fails to render.
        return f"<h2>Error loading template</h2><p>{e}</p><p>Verify that 'ui/templates/interface.html' exists and is accessible.</p>"

@app.route('/predecir', methods=['POST'])
def make_prediction():
    """
    Endpoint for performing the crop prediction.

    Expects a JSON payload with the 7 soil/climate features (N, P, K, etc.).
    Uses the imported 'predict' module to get the recommendation.

    Returns:
        json: A JSON object with the status ('success' or 'error') and the result/message.
    """
    try:
        # 1. Retrieve and log the incoming data.
        data = request.get_json()
        print(f"DATA RECEIVED: {data}")

        # 2. Data conversion and structuring.
        # Values are extracted, converted to float, and packaged into a list,
        # respecting the feature order expected by the ML model.
        valores = [
            float(data['N']),
            float(data['P']),
            float(data['K']),
            float(data['temperature']),
            float(data['humidity']),
            float(data['ph']),
            float(data['rainfall'])
        ]

        # 3. Call the prediction model.
        # The list of values is wrapped in another list, as many ML models expect
        # an input shape of (number_of_samples, number_of_features).
        prediction = predict([valores])

        # 4. Result processing.
        # Ensures that if 'prediction' is an array/list, the first (and only)
        # result is extracted. If not iterable, it is used directly.
        crop_result = prediction[0] if hasattr(prediction, '__len__') else prediction

        print(f"CROP PREDICTED SUCCESFULLY: {crop_result}")
        # Return the result in JSON format for the frontend to process.
        return jsonify({'status': 'success', 'resultado': crop_result})

    except KeyError as e:
        # Specific handling for missing key errors in the input JSON (Client Error: 400).
        error_msg = f"Missing data field in request: {e}"
        print(f"CLIENT ERROR: {error_msg}")
        return jsonify({'status': 'error', 'message': error_msg}), 400

    except ValueError as e:
        # Specific handling for type conversion errors (e.g., trying to convert 'a' to float) (Client Error: 400).
        error_msg = f"Invalid data type in request: {e}"
        print(f"CLIENT ERROR: {error_msg}")
        return jsonify({'status': 'error', 'message': error_msg}), 400

    except Exception as e:
        # Generic handling for any other server or model error (Server Error: 500).
        error_msg = f"SERVER ERROR during prediction: {e}"
        print(error_msg)
        return jsonify({'status': 'error', 'message': error_msg}), 500

def open_browser():
    """
    Automatically opens the web browser to the application's URL.
    """
    # Prevents the browser from opening twice in debug mode (due to Werkzeug reloader).
    # 'WERKZEUG_RUN_MAIN' is an environment variable set by the reloader process.
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        webbrowser.open_new('http://127.0.0.1:5000/')

if __name__ == '__main__':
    # 1. Start a timer to open the browser after 1.5 seconds,
    # allowing the server time to fully initialize.
    Timer(1.5, open_browser).start()
    print("Server starting...")

    # 2. Start the Flask application.