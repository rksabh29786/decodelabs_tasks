def recommend_movies(df, genre, mood, language):

    recommendations = []

    for _, row in df.iterrows():

        score = 0

        if row["Genre"].lower() == genre.lower():
            score += 3

        if row["Mood"].lower() == mood.lower():
            score += 2

        if row["Language"].lower() == language.lower():
            score += 1

        if score > 0:
            recommendations.append({
                "Movie": row["Movie"],
                "Genre": row["Genre"],
                "Mood": row["Mood"],
                "Language": row["Language"],
                "Rating": row["Rating"],
                "Score": score
            })

    recommendations.sort(
        key=lambda x: (x["Score"], x["Rating"]),
        reverse=True
    )

    return recommendations[:10]