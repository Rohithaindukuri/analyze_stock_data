import csv
import os

def read_csv_file(file_path):
    data = []
    try:
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
    return data

def main():
    # Specify the path to your CSV file
    file_name = 'historical_data.csv'
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, file_name)
    
    if os.path.exists(file_path):
        data = read_csv_file(file_path)
        if data:
            for row in data:
                print(row)
        else:
            print(f"No data found in '{file_path}'.")
    else:
        print(f"File '{file_name}' not found in directory '{current_directory}'.")

if __name__ == '__main__':
    main()
