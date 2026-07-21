from sklearn.datasets import load_iris
import pandas as pd

# Load Iris dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)

# Add target labels
df['species'] = [iris.target_names[i] for i in iris.target]

# Save to CSV
df.to_csv('dataset/iris.csv', index=False)

print("Dataset saved successfully!")
print(df.head())