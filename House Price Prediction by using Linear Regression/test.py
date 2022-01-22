import math

import matplotlib.pyplot as pyplot
from keras.losses import mean_squared_error
from matplotlib import style
import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn import metrics

data=pd.read_csv("prices.csv")
data=data[["price","lot_area","living_area","num_floors","num_bedrooms","num_bathrooms","waterfront","year_built","year_renovated"]]

print(data.head())

predict="price"

X=np.array(data.drop([predict],1))
y=np.array(data[predict])


reg=linear_model.LinearRegression()
x_train,x_test ,y_train,y_test=sklearn.model_selection.train_test_split(X,y,train_size=0.8,random_state=42)

reg.fit(x_train,y_train)
y_pred=reg.predict(x_test)

from sklearn.metrics import mean_squared_error

val="{:.2f}".format(math.sqrt(mean_squared_error(y_test,y_pred)))
print("Root mean squared error :",val)

p='living_area'
style.use("ggplot")
pyplot.scatter(data[p],data["price"])
pyplot.xlabel(p)
pyplot.ylabel("price")

pyplot.show()






