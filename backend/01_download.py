from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# load data
california_housing = fetch_california_housing()
df_x = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
df_y = pd.DataFrame(california_housing.target, columns=['HousingPrices'])
df=pd.concat([df_x,df_y],axis=1)
df.to_csv("train.csv")

