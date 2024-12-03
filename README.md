# House Price Prediction

## Overview
This project predicts house prices based on various input features using a machine learning pipeline. The pipeline includes data ingestion, cleaning, transformation, model training, validation, and prediction. The application integrates the trained model with a Flask web app, allowing users to input features and receive price predictions.

## Features
- **Data Pipeline**: Includes ingestion, cleaning, transformation, and validation steps.
- **Model Training**: Utilizes XGBoost regression with hyperparameter tuning.
- **Web Application**: Interactive Flask app for user input and real-time predictions.
- **Visualization**: Generates residual plots, learning curves, and feature importance plots.

## Project Structure
```plaintext
MY_OWN/
├── .github/
├── artifacts/
│   ├── data_clean/
│   ├── data_ingestion/
│   ├── data_transform/
│   ├── model_train/
│   ├── model_validation/
├── config/
│   └── config.yaml
├── logs/
│   └── logging.log
├── research/
├── src/
│   ├── datascience/
│   │   ├── components/
│   │   ├── config/
│   │   ├── constants/
│   │   ├── entity/
│   │   ├── logs/
│   │   ├── pipeline/
│   │   ├── utils/
├── static/
│   └── scores_plot.png
├── templates/
│   ├── index.html
│   ├── train_results.html
├── app.py
├── Dockerfile
├── main.py
├── params.yaml
├── requirements.txt
├── schema.yaml
├── setup.py
```

## Installation

### Prerequisites
- Python 3.10+
- Git

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Prahaladha-Reddy/House_Price_Prediction.git
   cd House_Price_Prediction
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Access the app at `http://127.0.0.1:5000`.

## Usage

### Training the Model
1. Go to the root URL of the app.
2. Click the "Train" button to start the training pipeline.
3. Training results, including evaluation scores and plots, will be displayed.

### Making Predictions
1. Input the following features in the form:
   - **Beds**
   - **Baths**
   - **Size**
   - **Zip Code**
2. Click "Predict" to get the house price prediction.

## Key Files

- **`app.py`**: Main Flask application file.
- **`config/config.yaml`**: Configuration file for pipeline paths and parameters.
- **`src/datascience/pipeline/prediction_pipeline.py`**: Handles prediction using the trained model.
- **`artifacts/`**: Stores intermediate and final results, including cleaned data, trained models, and plots.
- **`templates/`**: Contains HTML files for the Flask app.

## Visualizations
- **Residual Distribution**: Visualizes residuals to evaluate model performance.
- **Feature Importance**: Highlights the importance of each feature used in the model.
- **Learning Curve**: Shows model performance as the training size increases.
