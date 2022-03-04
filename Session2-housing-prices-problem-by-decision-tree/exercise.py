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
