import pandas as pd

def extract_csv_text(csv_path):
    """
    Convert CSV rows into text.
    """

    try:

        df = pd.read_csv(csv_path)

        return df.to_string(index=False)

    except Exception as e:

        return f"Error reading CSV: {str(e)}"