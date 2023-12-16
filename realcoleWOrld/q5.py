import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset from the file
file_path = 'bezdekIris.data'  # Assuming both the Python script and the file are in the same folder
column_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'class']
iris_df = pd.read_csv(file_path, header=None, names=column_names)

# a. Plot bar chart to show the frequency of each class label
class_counts = iris_df['class'].value_counts()
class_counts.plot(kind='bar', color='skyblue')
plt.title('Class Frequency in Iris Dataset')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

# b. Draw a scatter plot for Petal width vs Sepal width
plt.figure(figsize=(8, 5))
colors = {'Iris-setosa': 'red', 'Iris-versicolor': 'green', 'Iris-virginica': 'blue'}
for flower_class, color in colors.items():
    subset = iris_df[iris_df['class'] == flower_class]
    plt.scatter(subset['petal width (cm)'], subset['sepal width (cm)'], label=flower_class, color=color)
plt.title('Scatter Plot: Petal Width vs Sepal Width')
plt.xlabel('Petal Width (cm)')
plt.ylabel('Sepal Width (cm)')
plt.legend()
plt.show()

# c. Plot density distribution for feature petal length
plt.figure(figsize=(8, 5))
sns.kdeplot(data=iris_df, x='petal length (cm)', hue='class', fill=True, common_norm=False, palette='viridis')
plt.title('Density Distribution of Petal Length')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Density')
plt.show()

# d. Use a pair plot to show pairwise bivariate distribution in the Iris Dataset
plt.figure(figsize=(10, 8))
sns.pairplot(iris_df, hue='class', palette='viridis', height=2.5)
plt.suptitle('Pairwise Bivariate Distribution in Iris Dataset', y=1.02)
plt.show()