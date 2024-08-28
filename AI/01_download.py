# https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset
# - MedInc      収入中央値
# - HouseAge    住宅築年数の中央値
# - AveRooms    世帯あたりの平均部屋数
# - AveBedrms   世帯あたりの平均寝室数
# - Population  人口
# - AveOccup    平均世帯員数
# - Latitude    緯度
# - Longitude   経度

from sklearn.datasets import fetch_california_housing
import pandas as pd
california_housing = fetch_california_housing()
data1 = pd.DataFrame(california_housing.data, columns=california_housing.feature_names)
data2 = pd.DataFrame(california_housing.target, columns=['HousingPrices'])
data=pd.concat([data1,data2],axis=1)
data.to_csv("train.csv")
