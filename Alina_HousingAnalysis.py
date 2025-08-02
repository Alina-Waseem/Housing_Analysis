#Part 1: Setup & Load Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Housing.csv')
print(df)


# Part 2: Explore & Clean Data

print(df.head())

print(df.describe())

print(df.isnull().sum())

# Part 3: Compute Statistics

cols = ['price', 'area', 'bedrooms']

for col in cols:
  print(f"Statistics for {col.capitalize()}:")
  print("\nMean: ", df[col].mean())
  print("Median: ", df[col].median())
  print("Mode: ", df[col].mode()[0])
  print("Variance: ", df[col].var())
  print("Standard Deviation: ", df[col].std())
  print("SKewness: ", df[col].skew())
  print("kurtosis: ", df[col].kurt())
  print("Minimum: ", df[col].min())
  print("Maximum: ", df[col].max())
  print("-" * 40)

#Part 4:  Visualization

plt.figure(figsize=(8,5))
sns.histplot(df['price'], bins=30, kde=True)
plt.title('Distribution of Housing Prices')
plt.xlabel('Price')
plt.ylabel('Count')
plt.show()

plt.figure(figsize= (8,5))
sns.boxplot(x=df['area'])
plt.title('Box Plot of Area')
plt.show()

plt.figure(figsize = (8,5))
sns.scatterplot(x='area', y= 'price', data= df)
plt.title('Price vs Area')
plt.xlabel('Area')
plt.ylabel('Price')
plt.show()
