import pandas as pd

file_path = 'train.csv'
model_data = pd.read_csv(file_path) 

filtered_model_data_data = model_data

y = filtered_model_data_data.SalePrice
model_data_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = filtered_model_data_data[model_data_features]

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)


from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: " , max_leaf_nodes , "Mean Absolute Error:", my_mae)


import matplotlib.pyplot as plt
ax = plt.axes()

ax.plot([5,50,500,5000], [347380,258171,243495,254983]);
