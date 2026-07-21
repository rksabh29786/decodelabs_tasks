import os
import matplotlib.pyplot as plt
import seaborn as sns


def visualize_data(df):
    """
    Create and save visualizations for the Iris dataset.
    """

    print("\n" + "=" * 50)
    print("DATA VISUALIZATION")
    print("=" * 50)

    # Create images folder if it doesn't exist
    os.makedirs("images", exist_ok=True)

    sns.set_style("whitegrid")

    # -------------------------------
    # Pair Plot
    # -------------------------------
    pair_plot = sns.pairplot(
        df,
        hue=df.columns[-1],
        diag_kind="hist"
    )

    pair_plot.savefig("images/pairplot.png")
    plt.close()

    print("✓ Pair Plot Saved")

    # -------------------------------
    # Correlation Heatmap
    # -------------------------------
    plt.figure(figsize=(8, 6))

    sns.heatmap(
        df.iloc[:, :-1].corr(),
        annot=True,
        cmap="Blues",
        linewidths=0.5
    )

    plt.title("Feature Correlation Heatmap")

    plt.tight_layout()

    plt.savefig("images/heatmap.png")
    plt.close()

    print("✓ Heatmap Saved")

    # -------------------------------
    # Histograms
    # -------------------------------
    df.iloc[:, :-1].hist(
        figsize=(10, 8),
        bins=15
    )

    plt.tight_layout()

    plt.savefig("images/histograms.png")
    plt.close()

    print("✓ Histograms Saved")

    # -------------------------------
    # Box Plots
    # -------------------------------
    plt.figure(figsize=(10, 6))

    sns.boxplot(data=df.iloc[:, :-1])

    plt.title("Feature Distribution")

    plt.tight_layout()

    plt.savefig("images/boxplot.png")
    plt.close()

    print("✓ Box Plot Saved")

    # -------------------------------
    # Scatter Plot
    # -------------------------------
    plt.figure(figsize=(8, 6))

    sns.scatterplot(
        data=df,
        x=df.columns[0],
        y=df.columns[2],
        hue=df.columns[-1],
        s=80
    )

    plt.title("Sepal Length vs Petal Length")

    plt.tight_layout()

    plt.savefig("images/scatterplot.png")
    plt.close()

    print("✓ Scatter Plot Saved")

    print("\nAll visualizations saved inside the images folder.")