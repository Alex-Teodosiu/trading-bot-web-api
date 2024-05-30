import pandas as pd

def calculate_bollinger_bands(data, window=20, num_std_dev=2):
    data['middle_band'] = data['close'].rolling(window=window).mean()
    data['std_dev'] = data['close'].rolling(window=window).std()
    data['upper_band'] = data['middle_band'] + (data['std_dev'] * num_std_dev)
    data['lower_band'] = data['middle_band'] - (data['std_dev'] * num_std_dev)
    return data[['middle_band', 'upper_band', 'lower_band']]
