import pandas as pd

def process_data(file_path):
    df = pd.read_csv(file_path)
    processed_data = []
    for index, row in df.iterrows():
        processed_row = {
            'id': row['id'],
            'value': row['value'] * 2  # Example processing
        }
        processed_data.append(processed_row)
    return pd.DataFrame(processed_data)


def process_data_optimized(file_path):
    df = pd.read_csv(file_path)
    #TODO
    return df

file_path = 'large_data_file.csv'
original_data = process_data(file_path)
optimized_data = process_data_optimized(file_path)

original_data.to_csv('processed_data_original.csv', index=False)
optimized_data.to_csv('processed_data_optimized.csv', index=False)