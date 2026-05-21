import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("titanic.csv")
female_survivors = df[(df["Sex"] == "female") & (df["Survived"] == 1)]
print(female_survivors.shape)
males_nsurvived = df[(df["Sex"] == "male") & (df["Survived"] == 0)]
print(males_nsurvived.shape)

# # Clean data
# df["Age"] = df["Age"].fillna(df["Age"].mean())
# df = df.drop(columns=["Cabin"])
# df = df.dropna(subset=["Embarked"])


# # Explore data
# print(df.head(5))
# print(df.shape)
# print(df.columns)
# print(df.isnull().sum())

# # Analysis
# print(df["Sex"].value_counts())
# print(df.groupby("Sex")["Survived"].sum())


# # charts 
# # bar chart 
# df["Survived"].value_counts().plot(kind="bar")
# plt.title("Survivors in Titnic")
# plt.xlabel("0 = Died, 1 = Survived")
# plt.ylabel("Number of Passengers")
# plt.show()
# # bar chart
# df.groupby("Sex")["Survived"].sum().plot(kind="bar")
# plt.title("Survivors by Gender")
# plt.xlabel("Gender")
# plt.ylabel("Number of Survivors")
# plt.show()
# # hist chart
# df["Age"].plot(kind="hist", bins=20)
# plt.title("Age Distribution of Passengers")
# plt.xlabel("Age")
# plt.ylabel("Count")
# plt.show()