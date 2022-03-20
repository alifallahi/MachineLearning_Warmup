### --- پیاده سازی رگرسیون خطی چندگانه بااستفاده از sklearn --- start
### --- Multiple linear regression by sklearn --- start


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

file_path = 'dataset.csv'

df = pd.read_csv(file_path)

y = df.Grade
features = ['Hours','Amount']
X = df[features]

train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

dt_model = LinearRegression()
dt_model.fit(train_X, train_y)


val_predictions = dt_model.predict(val_X)

print("----- Multiple linear regression by sklearn -----")
print("Orginal values: \n",val_y)

print("\nPredicted values:", val_predictions)

print("\ny = θ₀ + θ₁X₁ + θ₂X₂")
print("θ₀ =",dt_model.intercept_)
print("θ₁ =",dt_model.coef_[0])
print("θ₂ =",dt_model.coef_[1])


### --- پیاده سازی رگرسیون خطی چندگانه بااستفاده از sklearn --- end
### --- Multiple linear regression by sklearn --- end


### --- پیاده سازی رگرسیون خطی چندگانه بدون sklearn --- start
### --- Multiple linear regression without sklearn --- start
  
def paramcalc(x1,x2,y,input_x1,input_x2):
     x1y = []
     x2y = []
     x1x2 = []
     x1power2 = []
     x2power2 = []
  
     sum_x1 = 0 
     sum_x2 = 0
     sum_y = 0
     sum_x1y = 0
     sum_x2y = 0
     sum_x1x2 = 0
     sum_x1power2 = 0
     sum_x2power2 = 0
  
     for i in range(0, input_size):
          x1y.append(x1[i]*y[i])
          x2y.append(x2[i]*y[i])
          x1x2.append(x1[i]*x2[i])
          x1power2.append(x1[i]**2)
          x2power2.append(x2[i]**2)
  
     for i in range(0, input_size):
          sum_x1 = sum_x1 + x1[i]
          sum_x2 = sum_x2 + x2[i]
          sum_y =  sum_y + y[i]
          sum_x1y = sum_x1y + x1y[i]
          sum_x2y = sum_x2y + x2y[i]
          sum_x1x2 = sum_x1x2 + x1x2[i]
          sum_x1power2 = sum_x1power2 + x1power2[i]
          sum_x2power2 = sum_x2power2 + x2power2[i]
  
     orginal_m = [[input_size,sum_x1,sum_x2],
                          [sum_x1,sum_x1power2,sum_x1x2],
                          [sum_x2,sum_x1x2,sum_x2power2]
                         ]
     teta0_numerator = [[sum_y,sum_x1,sum_x2],
                                     [sum_x1y,sum_x1power2,sum_x1x2],
                                     [sum_x2y,sum_x1x2,sum_x2power2]
                                    ]
     teta1_numerator = [[input_size,sum_y,sum_x2],
                                     [sum_x1,sum_x1y,sum_x1x2],
                                     [sum_x2,sum_x2y,sum_x2power2]
                                    ]
     teta2_numerator = [[input_size,sum_x1,sum_y],
                                     [sum_x1,sum_x1power2,sum_x1y],
                                     [sum_x2,sum_x1x2,sum_x2y]
                                    ]
  
     teta0 = det(teta0_numerator)/det(orginal_m)
     teta1 = det(teta1_numerator)/det(orginal_m)
     teta2 = det(teta2_numerator)/det(orginal_m)
  
     print("\nθ₀ = " , teta0)
     print("θ₁ = " , teta1)
     print("θ₂ = " , teta2)
     print("y = θ₀ + θ₁X₁ + θ₂X₂")
     temp_print = teta0 + (teta1*input_x1) + (teta2*input_x2)
     print("y = ",teta0,"+(",teta1,"*",input_x1,")+(",teta2,"*",input_x2,")=",temp_print)
  
     predicted_value = teta0 + (teta1 * input_x1) +  (teta2 * input_x2) 
     print("predicted value for x1=",input_x1, "and x2=",input_x2,"=", predicted_value)
  
  
def det(m):
     det_result = (m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))) -(m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))) +(m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0])))
     return (det_result)
  
  
x1 = [2,2.2,4,7,8,12,21]
x2 = [1,2,4,5,6,8,9]
y = [7,8,15,22,29,45.7,49]
input_size = len(x1)
 
print("\n ----- Multiple linear regression without sklearn -----") 
x1_list= [2.8,25,11]
x2_list = [3,10,7]
for i in range(0,3):
    paramcalc(x1,x2,y,x1_list[i],x2_list[i])
  
### --- پیاده سازی رگرسیون خطی چندگانه بدون sklearn --- end
### --- Multiple linear regression without sklearn --- end
