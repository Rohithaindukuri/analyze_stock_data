import pandas as pd

def process_historical_data(file_path):
    historical_data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    historical_data.dropna(inplace=True)
    historical_data['20d_ma'] = historical_data['Close'].rolling(window=20).mean()
    historical_data['50d_ma'] = historical_data['Close'].rolling(window=50).mean()
    historical_data['Daily_Return'] = historical_data['Close'].pct_change()
    return historical_data

# Example usage:
processed_data = process_historical_data('historical_data.csv')
processed_data.to_csv('processed_data.csv')
