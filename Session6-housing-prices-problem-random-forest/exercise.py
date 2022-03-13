import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

file_path = 'train.csv'
home_data = pd.read_csv(file_path)


y = home_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

dt_model = DecisionTreeRegressor(random_state=1)
dt_model.fit(train_X, train_y)

val_predictions = dt_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for Decision tree, when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))





dt_model_with_depth = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
dt_model_with_depth.fit(train_X, train_y)
val_predictions = dt_model_with_depth.predict(val_X)
val_mae_with_depth = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for Decision tree, with best value of max_leaf_nodes: {:,.0f}".format(val_mae_with_depth))





import pandas as pd
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

file_path = 'train.csv'
home_data = pd.read_csv(file_path)


y = home_data.SalePrice
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[features]


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)

val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(val_predictions, val_y)

print("Validation MAE for Random forest, when not specifying max_leaf_nodes: {:,.0f}".format(rf_val_mae))





print("Summary:")
print("Normal Decision tree, MAE: {:,.0f}".format(val_mae))
print("Decision tree with max_leaf_nodes, MAE: {:,.0f}".format(val_mae_with_depth))
print("Normal Random forest, MAE: {:,.0f}".format(rf_val_mae))
