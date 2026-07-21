from sklearn.model_selection import train_test_split


def preprocess_data(df):
    """
    Preprocess the Iris dataset.

    Parameters:
        df (DataFrame): Loaded dataset

    Returns:
        X_train, X_test, y_train, y_test
    """

    print("\n" + "=" * 50)
    print("DATA PREPROCESSING")
    print("=" * 50)

    # Check missing values
    print("\nMissing Values:")
    print(df.isnull().sum())

    # Features
    X = df.iloc[:, :-1]

    # Target
    y = df.iloc[:, -1]

    print("\nFeatures Shape :", X.shape)
    print("Target Shape   :", y.shape)

    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.20,
        random_state=42,
        stratify=y
    )

    print("\nDataset Split Successfully")
    print(f"Training Samples : {len(X_train)}")
    print(f"Testing Samples  : {len(X_test)}")

    return X_train, X_test, y_train, y_test