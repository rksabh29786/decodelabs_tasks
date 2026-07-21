import pandas as pd


def load_dataset():
    """
    Load the movie dataset from CSV.
    """
    return pd.read_csv("data/movies.csv")