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

mytest_model.predict(X)

y

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

from sklearn.metrics import mean_absolute_error

my_MAE = mean_absolute_error(new_orginal_prices, predicted_home_prices)

print("\n MAE =", my_MAE)

from sklearn.model_selection import train_test_split


train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

splitted_model = DecisionTreeRegressor(random_state=1)

splitted_model.fit(train_X, train_y)

val_predictions = splitted_model.predict(val_X)


#print(train_X.head())
#print("\n",val_X.head())


splitted_MAE = mean_absolute_error(val_predictions, val_y)

print("\n MAE =", splitted_MAE)
