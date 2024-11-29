import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
def load_and_explore_dataset():
    try:
        # Load the Iris dataset using sklearn
        iris = load_iris()
        data = pd.DataFrame(
            data=iris.data, 
            columns=iris.feature_names
        )
        data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
        
        # Display the first few rows
        print("First few rows of the dataset:")
        print(data.head())
        
        # Check the structure of the dataset
        print("\nDataset Info:")
        print(data.info())
        
        # Check for missing values
        print("\nMissing values in the dataset:")
        print(data.isnull().sum())
        
        # Clean the dataset (No missing values in Iris dataset)
        print("\nDataset is clean (no missing values).")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")

# Task 2: Basic Data Analysis
def analyze_dataset(data):
    # Basic statistics of numerical columns
    print("\nBasic statistics of numerical columns:")
    print(data.describe())
    
    # Grouping and mean calculation
    grouped_data = data.groupby('species').mean()
    print("\nMean values of numerical columns grouped by species:")
    print(grouped_data)
    
    # Identify patterns or findings
    print("\nKey Findings:")
    print("- Petal and sepal dimensions vary significantly between species.")
    print("- Versicolor species generally have intermediate dimensions.")
    return grouped_data

# Task 3: Data Visualization
def visualize_data(data):
    # Set Seaborn style
    sns.set(style="whitegrid")

    # Line chart (simulate a trend over species for illustration)
    grouped = data.groupby('species').mean()
    plt.figure(figsize=(8, 5))
    grouped.plot(kind='line', marker='o')
    plt.title("Mean Measurements by Species")
    plt.xlabel("Species")
    plt.ylabel("Mean Value")
    plt.xticks(ticks=range(len(grouped)), labels=grouped.index)
    plt.legend(loc="upper left")
    plt.grid()
    plt.show()

    # Bar chart (e.g., average petal length per species)
    plt.figure(figsize=(8, 5))
    sns.barplot(x='species', y=data.columns[2], data=data)
    plt.title("Average Petal Length per Species")
    plt.xlabel("Species")
    plt.ylabel("Petal Length (cm)")
    plt.show()

    # Histogram of a numerical column (e.g., sepal length)
    plt.figure(figsize=(8, 5))
    sns.histplot(data[data.columns[0]], kde=True, bins=15)
    plt.title("Distribution of Sepal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Frequency")
    plt.show()

    # Scatter plot (e.g., sepal length vs. petal length)
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=data.columns[0], y=data.columns[2], hue='species', data=data)
    plt.title("Sepal Length vs. Petal Length")
    plt.xlabel("Sepal Length (cm)")
    plt.ylabel("Petal Length (cm)")
    plt.legend(title="Species")
    plt.show()

# Main Execution
if __name__ == "__main__":
    # Load and explore the dataset
    dataset = load_and_explore_dataset()
    
    # Perform analysis if the dataset is loaded
    if dataset is not None:
        grouped_stats = analyze_dataset(dataset)
        
        # Visualize data
        visualize_data(dataset)
