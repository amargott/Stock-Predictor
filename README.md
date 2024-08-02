# Stock Predictor

This project aims to predict stock market trends using machine learning models. The project structure includes data preprocessing, feature engineering, model training, and evaluation scripts. The prediction is based on historical stock data collected using `yfinance`.

## Project Structure

stock-predictor/
├── historical_data.csv
├── data_preprocessing.py
├── feature_engineering.py
├── model_training.py
├── model_evaluation.py
├── requirements.txt
└── README.md

## Setup

### 1. Clone the Repository

First, clone the repository to your local machine using the following command:

git clone https://github.com/yourusername/stock-predictor.git
cd stock-predictor
2. Install Dependencies
Install the necessary dependencies by running:

pip install -r requirements.txt
3. Data Preprocessing
Run the preprocessing script to download and preprocess the stock data. This script will prompt you to enter a stock ticker symbol (e.g., AAPL for Apple).
python data_preprocessing.py
Description:
Downloads historical stock data for the given ticker.
Preprocesses the data by handling missing values and normalizing the Close prices.
Saves the scaled data to a CSV file.

4. Feature Engineering
Run the feature engineering script to add additional features to the preprocessed data. This script will also prompt you to enter the same stock ticker symbol used in the preprocessing step.
python feature_engineering.py

Description:
Adds technical indicators such as Simple Moving Averages (SMA) and volatility.
Saves the engineered features to a new CSV file.

5. Model Training
Train the LSTM model using the feature-engineered data. Again, enter the same stock ticker symbol when prompted.
python model_training.py
Description:
Creates datasets for training and testing.
Defines and trains an LSTM model.
Saves the trained model to an H5 file.

6. Model Evaluation
Evaluate the model's performance using the test dataset. Enter the stock ticker symbol used in the previous steps.
python model_evaluation.py

Description:
Loads the trained model and test data.
Makes predictions on the test data.
Calculates and prints the Mean Squared Error (MSE) of the predictions.
Example Usage
Here's an example of how you might use this project step-by-step:

Clone the Repository:
git clone https://github.com/yourusername/stock-predictor.git
cd stock-predictor

Install Dependencies:
pip install -r requirements.txt

Download and Preprocess Data:
python data_preprocessing.py
When prompted, enter: AAPL

Add Features:
python feature_engineering.py
When prompted, enter: AAPL

Train the Model:
python model_training.py
When prompted, enter: AAPL

Evaluate the Model:
python model_evaluation.py
When prompted, enter: AAPL
