### --- پیاده سازی الگوریتم درخت تصمیم --- start
### --- Running the decision tree --- start

import pandas as pd
from sklearn.tree import DecisionTreeRegressor

file_path = 'train.csv'

home_data = pd.read_csv(file_path)
home_data.head()

y = home_data.SalePrice
feature_columns = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = home_data[feature_columns]

mytest_model = DecisionTreeRegressor()
mytest_model.fit(X, y)

print("First in-sample predictions:", mytest_model.predict(X.head()))
print("Actual target values for those homes:", y.head().tolist())

### --- Running the decision tree --- end
### --- پیاده سازی الگوریتم درخت تصمیم --- end


### --- مقایسه مقادیر پیش بینی شده و مقادیر اصلی --- start
### --- Comparing predicted values and original ones --- start

mytest_model.predict(X)

y

### --- مقایسه مقادیر پیش بینی شده و مقادیر اصلی --- end
### --- Comparing predicted values and original ones --- end


### --- پیاده سازی معیار سنجش قدرمطلق میانگین خطا MAE  --- start
### --- Manually calculating the Mean Absolute Error (MAE) --- start

predicted_home_prices = mytest_model.predict(X).tolist()
orginal_prices = y.tolist()

new_orginal_prices = []

for i in range(0, len(orginal_prices)):
    new_orginal_prices.append(int(orginal_prices[i]))

print(new_orginal_prices)

print("\n\n",predicted_home_prices)

c = 0
print("index   Orginal - Predicted = Difference")
for i in range(0, len(new_orginal_prices)):
    x1 = new_orginal_prices[i]
    x2 = predicted_home_prices[i]
    if(x1 - x2 !=0):
        c1 = (x1 - x2)
        print([i]," ", x1 ," - ", x2, " = ", x1-x2)
        c = c + abs(c1)

print("\nManually calculated MAE = ",(1/len(new_orginal_prices)*c))

### --- پیاده سازی معیار سنجش قدرمطلق میانگین خطا MAE  --- end
### --- Manually calculating the Mean Absolute Error (MAE) --- end


### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE با استفاده از sklearn  --- start
### --- Calculating the Mean Absolute Error (MAE) by sklearn --- start

from sklearn.metrics import mean_absolute_error

my_MAE = mean_absolute_error(y, mytest_model.predict(X))

print("\n MAE by sklearn =", my_MAE)

### ---  اندازه گیری معیار سنجش قدرمطلق میانگین خطا MAE با استفاده از sklearn  --- end
### --- Calculating the Mean Absolute Error (MAE) by sklearn --- end


### --- تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- start
### --- Splitting data into training and validation sets by sklearn --- start

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

splitted_model = DecisionTreeRegressor(random_state=1)

splitted_model.fit(train_X, train_y)

val_predictions = splitted_model.predict(val_X)

splitted_MAE = mean_absolute_error(val_predictions, val_y)

print("\n MAE  =", splitted_MAE)

### --- تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- end
### --- Splitting data into training and validation sets by sklearn --- end
