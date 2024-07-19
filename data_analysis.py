import pandas as pd

def analyze_data(file_path):
    data = pd.read_csv(file_path, index_col='Date', parse_dates=True)
    summary = data.describe()
    return summary

# Example usage:
analysis_summary = analyze_data('processed_data.csv')
print(analysis_summary)
