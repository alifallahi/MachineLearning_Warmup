### --- پیاده سازی رگرسیون خطی ساده بااستفاده از sklearn --- start
### --- Simple linear regression by sklearn --- start

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

file_path = 'dataset.csv'

df = pd.read_csv(file_path)

y = df.Grade
features = ['Hours']
X = df[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

dt_model = LinearRegression()
dt_model.fit(train_X, train_y)


val_predictions = dt_model.predict(val_X)

print("Orginal values: \n",val_y)

print("\nPredicted values:", val_predictions)

print("\ny = θ₀ + θ₁X₁")
print("θ₀ =",dt_model.intercept_)
print("θ₁ =",dt_model.coef_)

### --- پیاده سازی رگرسیون خطی ساده بااستفاده از sklearn --- end
### --- Simple linear regression by sklearn --- end
