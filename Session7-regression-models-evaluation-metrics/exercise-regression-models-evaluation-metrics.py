### --- پیاده سازی رگرسیون خطی ساده با sklearn --- start
### --- Implementing the simple linear regression by scikit --- start

import pandas as pd

file_path = 'dataset.csv'
df = pd.read_csv(file_path)

df

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

y = df.Grade
features = ['Hours']
X = df[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

dt_model = LinearRegression()
dt_model.fit(train_X, train_y)

val_predictions = dt_model.predict(val_X)

print("Orginal values: \n",val_y)

print("\nPredicted values:", val_predictions)

### --- پیاده سازی رگرسیون خطی ساده با sklearn --- end
### --- Implementing the simple linear regression by scikit --- end


### https://scikit-learn.org/stable/modules/model_evaluation.html

### --- MSE and RMSE --- start
from sklearn.metrics import mean_squared_error
import math

val_mse = mean_squared_error(val_predictions, val_y)
val_rmse = mean_squared_error(val_predictions, val_y, squared=False)

print("MSE =", val_mse)
print("RMSE (by squared=False) =", val_rmse)

print("RMSE (bymath.sqrt) =", math.sqrt(val_mse))

### --- MSE and RMSE --- end


### --- MAE --- start
from sklearn.metrics import mean_absolute_error

val_mae = mean_absolute_error(val_predictions, val_y)

print("MAE =", val_mae)

### --- MAE --- end


### --- MAPE --- start
from sklearn.metrics import mean_absolute_percentage_error

val_mape = mean_absolute_percentage_error(val_predictions, val_y)

print("MAPE =", val_mape)

### --- MAPE --- end


### --- R2 --- start
from sklearn.metrics import r2_score

val_r2 = r2_score(val_predictions, val_y)

print("R2 =", val_r2)

### --- R2 --- end
