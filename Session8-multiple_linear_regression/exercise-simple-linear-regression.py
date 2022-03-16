### --- #shape (1) codes | کدهای مربوط به شکل (1) در قسمت هشتم  --- start

import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

Area = [10,15,20,25,30]
Price = [500,750,1000,1250,1500]

plt.scatter(Area, Price, color='blue')
plt.xlabel('Area')
plt.ylabel('Price')

input_size = len(Area)
x = Area
y = Price

### --- #shape (1) codes | کدهای مربوط به شکل (1) در قسمت هشتم  --- end


### --- بخش مربوط به محاسبه میانگین --- start
### --- Average calculation section --- start

input_size = len(Area)
x = Area
y = Price

def avg(avg_input):
     my_temp = 0
     for i in range (0, input_size):
          my_temp = my_temp + avg_input[i]
     return(my_temp/input_size)

avg_x = avg(x)
avg_y = avg(y)
print("Average of x: ", avg_x)
print("Average of y: ", avg_y)

### --- Average calculation section --- end
### --- بخش مربوط به محاسبه میانگین --- end


### --- بخش مربوط به محاسبه تتا1 و تتا2 در رگرسیون خطی ساده --- start
### --- Calculating theta 1 and theta 2 in simple linear regression --- start

def beta1():
     beta1_numerator = 0
     beta1_denumerator = 0
     for i in range (0, input_size):
          beta1_numerator = beta1_numerator + ((x[i] - avg_x)*(y[i] - avg_y))
          beta1_denumerator = beta1_denumerator + ((x[i] - avg_x)**2)
     return(beta1_numerator/beta1_denumerator)

print("Beta1 = ", beta1())

beta0 = avg_y - (beta1() * avg_x)
print("Beta0 = ", avg_y , "-" , "(" , beta1() , "*" , avg_x , ") =" , beta0)

### --- Calculating theta 1 and theta 2 in simple linear regression --- end
### --- بخش مربوط به محاسبه تتا1 و تتا2 در رگرسیون خطی ساده --- end
