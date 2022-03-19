### --- پیاده سازی الگوریتم درخت تصمیم و تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- start
### --- Running the decision tree and splitting data into training and validation sets by sklearn --- start

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


### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE بدون تنظیم عمق درخت --- start
### --- calculating Mean Absolute Error (MAE) for the decision tree without setting a specific depth --- start

val_predictions = dt_model.predict(val_X)
val_mae = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for Decision tree, when not specifying max_leaf_nodes: {:,.0f}".format(val_mae))

### --- calculating Mean Absolute Error (MAE) for the decision tree without setting a specific depth --- end
### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE بدون تنظیم عمق درخت --- end


### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE درخت با عمق 100 --- start
### --- calculating Mean Absolute Error (MAE) for the decision tree with a specific depth --- start

dt_model_with_depth = DecisionTreeRegressor(max_leaf_nodes=100, random_state=1)
dt_model_with_depth.fit(train_X, train_y)
val_predictions = dt_model_with_depth.predict(val_X)
val_mae_with_depth = mean_absolute_error(val_predictions, val_y)
print("Validation MAE for Decision tree, with best value of max_leaf_nodes: {:,.0f}".format(val_mae_with_depth))

### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE درخت با عمق 100 --- end
### --- calculating Mean Absolute Error (MAE) for the decision tree with a specific depth --- end



### --- پیاده سازی الگوریتم درخت تصمیم و تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- end
### --- Running the decision tree and splitting data into training and validation sets by sklearn --- end





### --- پیاده سازی الگوریتم جنگل تصادفی و تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- start
### --- Running the random forest and splitting data into training and validation sets by sklearn--- start

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

### --- پیاده سازی الگوریتم جنگل تصادفی و تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- end
### --- Running the random forest and splitting data into training and validation sets by sklearn--- end


### --- مقایسه مقادیر MAE برای سه حالت پیاده سازی شده --- start
### --- comparing MAE for the three above implementations --- start

print("Summary:")
print("Normal Decision tree, MAE: {:,.0f}".format(val_mae))
print("Decision tree with max_leaf_nodes, MAE: {:,.0f}".format(val_mae_with_depth))
print("Normal Random forest, MAE: {:,.0f}".format(rf_val_mae))

### --- comparing MAE for the three above implementations --- end
### --- مقایسه مقادیر MAE برای سه حالت پیاده سازی شده --- end
