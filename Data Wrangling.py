# -*- coding: utf-8 -*-
"""GlobalTemperatures.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oU0ODMN6DZ72GnYTg5nS1ipSS22cKfhZ
"""

import pandas as pd

df=pd.read_csv("/content/drive/MyDrive/Data/GlobalTemperatures.csv")

df.duplicated().sum()

df.isna().sum()/df.shape[0]

df.head()

df.isna()

df.isna().sum()

df.groupby('City').count()

df.info()

df.dt.astype("datetime64")

df.info()

df["dt"]=df.dt.astype("datetime64")

df.info()

df.rename(columns={"dt":"Date"}, inplace=True)

df.head()

df.info()

df.dropna(inplace=True)

df.head()

df.isna().sum()

df["Location"] = df["Latitude"] + ", " + df["Longitude"]

df.head()

df.drop(["Latitude", "Longitude"], axis=1, inplace=True)

df.head()

df = df.loc[df["Country"].isin(["Australia", "Brazil"])]

df.head()

df.sort_values(by=["Date"], inplace=True, ascending=False)

df.head(2000)

df.to_csv("assignment.csv", index=False)

