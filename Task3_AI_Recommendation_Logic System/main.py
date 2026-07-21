from src.dataset import load_dataset
from src.recommender import recommend_movies


def get_valid_input(prompt, valid_options):
    """
    Prompt the user until a valid option is entered.
    """
    while True:
        value = input(prompt).strip()

        # Empty input check
        if value == "":
            print("\n❌ Invalid input.")
            print("Please choose from the available options.\n")
            continue

        # Case-insensitive matching
        for option in valid_options:
            if value.lower() == option.lower():
                return option  # Return correct capitalization

        print("\n❌ Invalid input.")
        print("Please choose from the available options.\n")


# Load dataset
movies = load_dataset()

# Get unique options
genres = sorted(movies["Genre"].unique())
moods = sorted(movies["Mood"].unique())
languages = sorted(movies["Language"].unique())


print("=" * 60)
print("          AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 60)


while True:

    # -------------------------------
    # Genre Input Validation
    # -------------------------------

    print("\nAvailable Genres:")
    print(", ".join(genres))

    genre = get_valid_input(
        "\nEnter Genre: ",
        genres
    )


    # -------------------------------
    # Mood Input Validation
    # -------------------------------

    print("\nAvailable Moods:")
    print(", ".join(moods))

    mood = get_valid_input(
        "\nEnter Mood: ",
        moods
    )


    # -------------------------------
    # Language Input Validation
    # -------------------------------

    print("\nAvailable Languages:")
    print(", ".join(languages))

    language = get_valid_input(
        "\nEnter Language: ",
        languages
    )


    # -------------------------------
    # Generate Recommendations
    # -------------------------------

    results = recommend_movies(
        movies,
        genre,
        mood,
        language
    )


    print("\n" + "=" * 60)


    if len(results) == 0:

        print("No matching movies found.")


    else:

        print("Recommended Movies\n")


        print(
            f"{'Movie':30}"
            f"{'Genre':12}"
            f"{'Mood':15}"
            f"{'Language':12}"
            f"{'Rating':8}"
            f"{'Score'}"
        )


        print("-" * 90)


        for movie in results:

            print(
                f"{movie['Movie'][:28]:30}"
                f"{movie['Genre']:12}"
                f"{movie['Mood']:15}"
                f"{movie['Language']:12}"
                f"{movie['Rating']:<8}"
                f"{movie['Score']}"
            )


    print("=" * 60)


    # -------------------------------
    # Search Again Validation
    # -------------------------------

    while True:

        again = input(
            "\nSearch again? (y/n): "
        ).strip().lower()


        if again in ["y", "n"]:
            break

        print("\n❌ Invalid input. Enter y or n.")


    if again == "n":

        print(
            "\nThank you for using the AI Recommendation System!"
        )

        break