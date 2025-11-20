# Crop Recommendation System

A simple web application built with Flask that uses a pre-trained Random Forest machine learning model to recommend the best crop to grow based on soil and environmental features.

## Features

-   **Web Interface:** An easy-to-use interface to input soil and weather data.
-   **ML-Powered Predictions:** Utilizes a `scikit-learn` Random Forest model to provide crop recommendations.
-   **REST API:** A simple `/predecir` endpoint for predictions.

## Project Structure

```
.
├───main.py                     # Main Flask application file
├───requirements.txt            # Project dependencies
├───model_ml/
│   ├───predict.py              # Handles loading the model and making predictions
│   └───random_forest_model.joblib  # The pre-trained machine learning model
└───ui/
    └───templates/
        └───interface.html      # Frontend HTML
```

## Setup and Installation

Follow these steps to get the application running on your local machine.

### 1. Prerequisites

-   Python 3.8+
-   `pip` package manager

### 2. Clone the Repository (Optional)

If you have `git` installed, you can clone the repository:

```bash
git clone <your-repository-url>
cd <repository-folder>
```

### 3. Create and Activate a Virtual Environment

It is highly recommended to use a virtual environment to manage project dependencies.

**On Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install Dependencies

Install all the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

1.  **Run the Flask Application:**

    ```bash
    python main.py
    ```

2.  **Open the Web Interface:**

    The application will automatically open a new tab in your web browser at `http://127.0.0.1:5000`. If it doesn't, you can manually navigate to that URL.

3.  **Get a Prediction:**

    -   Fill in the values for the following features in the web form:
        -   **N:** Nitrogen content in the soil
        -   **P:** Phosphorus content in the soil
        -   **K:** Potassium content in the soil
        -   **Temperature:** Temperature in Celsius
        -   **Humidity:** Relative humidity in %
        -   **pH:** pH value of the soil
        -   **Rainfall:** Rainfall in mm
    -   Click the **"ANALYZE SOIL"** button to see the recommended crop.

## API Endpoint

The application exposes a single API endpoint for predictions.

### `POST /predecir`

This endpoint receives the 7 features as a JSON object and returns the predicted crop.

-   **Request Body:**

    ```json
    {
        "N": "90",
        "P": "42",
        "K": "43",
        "temperature": "20.87",
        "humidity": "82.0",
        "ph": "6.5",
        "rainfall": "202.9"
    }
    ```

-   **Success Response (200 OK):**

    ```json
    {
        "status": "success",
        "resultado": "rice"
    }
    ```

-   **Error Response (400/500):**

    ```json
    {
        "status": "error",
        "message": "Missing data field in request: 'N'"
    }
    ```

## How It Works

The application uses a `RandomForestClassifier` model from `scikit-learn` that was trained on a dataset of crop information. The `model_ml/predict.py` script loads this pre-trained model (from `random_forest_model.joblib`) and uses it to infer the most suitable crop based on the input data provided through the API.

## Dataset

The model was trained using the **Smart Farming Data 2024 (SF24)** dataset, which is available on Kaggle. This dataset contains various soil and environmental measurements for different crops.

-   **Dataset Link:** [Smart Farming Data 2024 (SF24) on Kaggle](https://www.kaggle.com/datasets/datasetengineer/smart-farming-data-2024-sf24/code)

## License

This project is unlicensed. You are free to use, modify, and distribute it as you see fit.