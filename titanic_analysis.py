import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
print(df.head(5))
print(df.shape)
print(df["Sex"].value_counts())
print(df.groupby("Sex")["Survived"].sum())
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survivors in titnic")
plt.xlabel("0 = Died, 1 = Survived")
plt.ylabel("Number of Passengers")
plt.show()
df.groupby("Sex")["Survived"].sum().plot(kind="bar")
plt.title("Survivors by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Survivors")
plt.show()