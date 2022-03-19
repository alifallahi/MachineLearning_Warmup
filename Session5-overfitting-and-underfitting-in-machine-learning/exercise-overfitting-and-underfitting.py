import pandas as pd

file_path = 'train.csv'
model_data = pd.read_csv(file_path) 

filtered_model_data_data = model_data

y = filtered_model_data_data.SalePrice
model_data_features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']
X = filtered_model_data_data[model_data_features]

### --- تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- start
### --- Splitting data into training and validation sets by sklearn --- start

from sklearn.model_selection import train_test_split

train_X, val_X, train_y, val_y = train_test_split(X, y,random_state = 0)

### --- تقسیم بندی مجموعه داده به دو بخش کلی train و validation --- end
### --- Splitting data into training and validation sets by sklearn --- end


### --- پیاده سازی الگوریتم درخت تصمیم و ارزیابی عملکرد آن با عمق های متفاوت توسط معیار میانگین قدرمطلق خطا MAE --- start
### --- Running the decision tree with different depths and calculating the Mean Absolute Error (MAE) --- start

from sklearn.metrics import mean_absolute_error
from sklearn.tree import DecisionTreeRegressor


def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    # Setting different depths by max_leaf_nodes | max_leaf_nodes تعریف مقدار عمق درخت با استفاده از 
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

for max_leaf_nodes in [5, 50, 500, 5000]:
    my_mae = get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y)
    print("Max leaf nodes: " , max_leaf_nodes , "Mean Absolute Error:", my_mae)
    
### --- پیاده سازی الگوریتم درخت تصمیم و ارزیابی عملکرد آن با عمق های متفاوت توسط معیار میانگین قدرمطلق خطا MAE --- end
### --- Running the decision tree with different depths and calculating the Mean Absolute Error (MAE) --- end

### --- نمایش ارتباط بین عمق درخت و میانگین قدرمطلق خطا  --- start
### --- Showing the relation between MAE and depth of the tree --- start
import matplotlib.pyplot as plt
ax = plt.axes()
ax.plot([5,50,500,5000], [347380,258171,243495,254983]);
### --- Showing the relation between MAE and depth of the tree --- end
### --- نمایش ارتباط بین عمق درخت و میانگین قدرمطلق خطا  --- end
