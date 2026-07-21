# from src.data_loader import load_data


# def main():

#     file_path = "dataset/iris.csv"

#     df = load_data(file_path)

#     if df is None:
#         print("Dataset could not be loaded.")
#         return


# if __name__ == "__main__":
#     main()


## Previous code was commented out and replaced with the following code that includes both data loading and preprocessing.
# from src.data_loader import load_data
# from src.preprocess import preprocess_data


# def main():

#     # Load dataset
#     df = load_data("dataset/iris.csv")

#     if df is None:
#         return

#     # Preprocess dataset
#     X_train, X_test, y_train, y_test = preprocess_data(df)


# if __name__ == "__main__":
#     main()


## The following code includes data loading, preprocessing, and visualization of the Iris dataset.


# from src.data_loader import load_data
# from src.preprocess import preprocess_data
# from src.visualize import visualize_data


# def main():

#     # Phase 1
#     df = load_data("dataset/iris.csv")

#     if df is None:
#         return

#     # Phase 2
#     X_train, X_test, y_train, y_test = preprocess_data(df)

#     # Phase 3
#     visualize_data(df)


# if __name__ == "__main__":
#     main()


## The following code includes data loading, preprocessing, visualization, and model training of the Iris dataset.
# from src.data_loader import load_data
# from src.preprocess import preprocess_data
# from src.visualize import visualize_data
# from src.train_model import train_model


# def main():

#     # Phase 1
#     df = load_data("dataset/iris.csv")

#     if df is None:
#         return

#     # Phase 2
#     X_train, X_test, y_train, y_test = preprocess_data(df)

#     # Phase 3
#     visualize_data(df)

#     # Phase 4
#     model = train_model(X_train, y_train)


# if __name__ == "__main__":
#     main()


## The following code includes data loading, preprocessing, visualization, model training, and model evaluation of the Iris dataset.

# from src.data_loader import load_data
# from src.preprocess import preprocess_data
# from src.visualize import visualize_data
# from src.train_model import train_model
# from src.evaluate import evaluate_model

# def main():

#     # Phase 1s
#     df = load_data("dataset/iris.csv")

#     if df is None:
#         return

#     # Phase 2
#     X_train, X_test, y_train, y_test = preprocess_data(df)

#     # Phase 3
#     visualize_data(df)

#     # Phase 4
#     model = train_model(X_train, y_train)

#     # Phase 5
#     evaluate_model(model, X_test, y_test)


# if __name__ == "__main__":
#     main()

### The following code includes data loading, preprocessing, visualization, model training, model evaluation, and flower prediction of the Iris dataset.

from src.data_loader import load_data
from src.preprocess import preprocess_data
from src.visualize import visualize_data
from src.train_model import train_model
from src.evaluate import evaluate_model
from src.predict import load_model, predict_flower



def main():

    # Phase 1
    df = load_data("dataset/iris.csv")


    if df is None:
        return


    # Phase 2
    X_train, X_test, y_train, y_test = preprocess_data(df)


    # Phase 3
    visualize_data(df)


    # Phase 4
    model = train_model(
        X_train,
        y_train
    )


    # Phase 5
    evaluate_model(
        model,
        X_test,
        y_test
    )


    # Phase 6
    print("\n" + "="*50)
    print("FLOWER PREDICTION")
    print("="*50)


    trained_model = load_model(
        "models/iris_classifier.pkl"
    )


    # New flower measurements
    new_flower = [
        5.1,  # Sepal Length
        3.5,  # Sepal Width
        1.4,  # Petal Length
        0.2   # Petal Width
    ]

    new_flower = [
    6.7,
    3.0,
    5.2,
    2.3
]


    result = predict_flower(
        trained_model,
        new_flower
    )


    print("\nPredicted Flower Species:")
    print(result)



if __name__ == "__main__":
    main()