import pandas as pd

def add_features(data):
    data['SMA_20'] = data['Close'].rolling(window=20).mean()
    data['SMA_50'] = data['Close'].rolling(window=50).mean()
    data['Volatility'] = data['Close'].rolling(window=20).std()
    data = data.dropna()
    return data

if __name__ == "__main__":
    ticker = input("Enter the stock ticker: ")
    data = pd.read_csv(f'{ticker}_scaled.csv')
    feature_data = add_features(data)
    feature_data.to_csv(f'{ticker}_features.csv', index=False)
