### --- پیاده سازی رگرسیون لجستیک بر روی دیتاست Iris  --- start
### --- Running logistic regression on the Iris dataset --- start

import pandas as pd
iris = pd.read_csv('iris.csv')

iris.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

y = iris.variety
features = ['sepal.length','sepal.width','petal.length','petal.width']
X = iris[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, test_size=0.4, random_state=1)

### --- رگرسیون لجستیک | Logistic regression
dt_model = LogisticRegression()
dt_model.fit(train_X, train_y)

val_predictions = dt_model.predict(val_X)

from sklearn import metrics
print(metrics.accuracy_score(val_y, val_predictions))

### --- Running logistic regression on the Iris dataset --- end
### --- پیاده سازی رگرسیون لجستیک بر روی دیتاست Iris  --- end
