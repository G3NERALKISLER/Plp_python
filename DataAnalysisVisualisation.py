import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("sales_data.csv")
df = df.sort_values("Date")
First_few_rows =df.head(3)
StructureOfDataset = df.dtypes
AnyMissingValue = df.isnull().sum()
FillQuantitySold = df["Quantity Sold"].fillna(0, inplace=True)

#plot lineGraph
plt.plot(df["Date"], df["Revenue"], marker="o", linestyle="-", color="blue")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Revenue Over Time")
plt.grid(True)  

#plot Bar graph
plt.bar(df["Product"], df["Quantity Sold"], edgecolor="black")
plt.xlabel("Date")
plt.ylabel("Revenue")
plt.title("Revenue Over Time")
plt.grid(True)  

#plot histoGram
plt.hist(df["Revenue"], bins=5, color="green", edgecolor="black")

plt.xlabel("Revenue Ranges")
plt.ylabel("Number of Products")
plt.title("Distribution of Revenue")

#plot scatterplot
plt.scatter(df["Quantity Sold"], df["Revenue"], color="red")

plt.xlabel("Quantity Sold")
plt.ylabel("Revenue")
plt.title("Scatter Plot: Quantity vs Revenue")
plt.show()