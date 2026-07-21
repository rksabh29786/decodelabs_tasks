import pandas as pd


def load_data(file_path):
    """
    Load the Iris dataset.
    """

    try:
        df = pd.read_csv(file_path)

        print("=" * 50)
        print("Dataset Loaded Successfully")
        print("=" * 50)

        print("\nFirst Five Rows:\n")
        print(df.head())

        print("\nDataset Shape:")
        print(df.shape)

        print("\nColumn Names:")
        print(df.columns.tolist())

        print("\nDataset Information:")
        print(df.info())

        print("\nStatistical Summary:")
        print(df.describe())

        print("\nMissing Values:")
        print(df.isnull().sum())

        return df

    except Exception as e:
        print("Error:", e)
        return None