from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

df = pd.read_csv('train.csv')

# choose target column and explain-columns
y = df['HousingPrices']
x = df[['MedInc','HouseAge','AveRooms','Population','AveOccup']] # Parameter


# split train-data and test-data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

# train model
model = DecisionTreeRegressor(min_samples_leaf=5)
model.fit(x_train,y_train)

# evaluate trained model
ret1=model.score(x_train,y_train)
ret2=model.score(x_test,y_test)

print("Score(Traind)={}%".format(ret1))
print("Score(Test  )={}%".format(ret2))

