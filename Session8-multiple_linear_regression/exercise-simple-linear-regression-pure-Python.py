### --- shape (1) codes | کدهای مربوط به شکل (1) در قسمت هشتم  --- start

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

### --- shape (1) codes | کدهای مربوط به شکل (1) در قسمت هشتم  --- end


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


### --- Calculating θ₀ and θ₁ in simple linear regression --- start
### --- بخش مربوط به محاسبه تتا0 و تتا1 در رگرسیون خطی ساده --- start

def teta1():
     teta1_numerator = 0
     teta1_denumerator = 0
     for i in range (0, input_size):
          teta1_numerator = teta1_numerator + ((x[i] - avg_x)*(y[i] - avg_y))
          teta1_denumerator = teta1_denumerator + ((x[i] - avg_x)**2)
     return(teta1_numerator/teta1_denumerator)
 
print("θ₁ = ", teta1())
 
teta0 = avg_y - (teta1() * avg_x)
print("θ₀ = ", avg_y , "-" , "(" , teta1() , "*" , avg_x , ") =" , teta0)

### --- Calculating θ₀ and θ₁ in simple linear regression --- end
### --- بخش مربوط به محاسبه تتا0 و تتا1 در رگرسیون خطی ساده --- end
