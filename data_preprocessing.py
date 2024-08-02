import yfinance as yf
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def download_data(ticker, period='5y'):
    data = yf.download(ticker, period=period)
    data.to_csv(f'{ticker}.csv')
    return data

def preprocess_data(data):
    data = data.dropna()
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(data[['Close']].values)
    return scaled_data, scaler

if __name__ == "__main__":
    ticker = input("Enter the stock ticker: ")
    data = download_data(ticker)
    scaled_data, scaler = preprocess_data(data)
    pd.DataFrame(scaled_data).to_csv(f'{ticker}_scaled.csv', index=False)
