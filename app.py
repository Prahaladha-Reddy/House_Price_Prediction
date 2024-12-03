
from flask import Flask, render_template, request, send_from_directory
import os
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import *
import matplotlib.pyplot as plt
import numpy as np
app = Flask(__name__)  # Initializing Flask App

@app.route('/', methods=['GET', 'POST'])  # Single route for both input and output
def predict():
    if request.method == 'POST':
        try:
            # Get user inputs
            beds = float(request.form['beds'])
            baths = float(request.form['baths'])
            size = float(request.form['size'])
            zip_code = float(request.form['zip_code'])

            # Prepare the data for prediction
            input_features = np.array([[beds, baths, size, zip_code]])

            # Use the PredictionPipeline to make predictions
            pipeline = PredictionPipeline()
            predicted_price = pipeline.predict(input_features)[0]

            # Format the prediction result
            formatted_price = f"${predicted_price:,.2f}"

            return render_template('index.html', price=formatted_price)

        except Exception as e:
            print(f"Error during prediction: {e}")
            return render_template('index.html', price="Error during prediction. Please try again.")
    else:
        return render_template('index.html', price=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
