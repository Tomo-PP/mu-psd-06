from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

# load data
df=pd.read_csv("train.csv")

y = df['HousingPrices'] # Answer
x = df[['MedInc','HouseAge','AveRooms']] # Parameter

# Split Training Data and Test Data.
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

print("Data Prepared.")

# Train
model = LinearRegression()
# model = DecisionTreeRegressor(min_samples_leaf=5)
# model = RandomForestRegressor(random_state=42)

ret = model.fit(x_train,y_train)

print("Model Trained.")

# Evaluate
ret1=model.score(x_train,y_train)
ret2=model.score(x_test,y_test)

print("Score(Traind)={}%".format(ret1))
print("Score(Test  )={}%".format(ret2))

# Save Trained Model.
joblib.dump(model,'model.pkl')

print("Model Saved.")


