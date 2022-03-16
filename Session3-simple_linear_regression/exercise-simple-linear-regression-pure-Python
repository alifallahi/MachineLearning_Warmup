import matplotlib.pyplot as plt
from numpy.polynomial.polynomial import polyfit

Area = [1,2,4,3,5]
Price = [1,3,3,2,5]

plt.scatter(Area, Price, color='blue')
plt.xlabel('Area')
plt.ylabel('Price')

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

def capital_y(user_input):
    return(beta0 + (beta1() * user_input))


user_input = [1,2,4,3,5]
predicted_y = []
for i in range(0, len(user_input)):
    predicted_y.append(capital_y(user_input[i]))
    
print("Predicted values are: ", predicted_y)

plt.scatter(Area, Price, color='blue')
plt.scatter(Area, predicted_y, color='red')
plt.xlabel('Area')
plt.ylabel('Price')
plt.plot(Area, predicted_y, color='orange')

def my_RMSE(y,predicted_y):
    my_temp = 0
    for i in range(0, input_size):
        my_temp = my_temp + ((y[i] - predicted_y[i])**2)
    my_temp = my_temp /  input_size
    my_temp = my_temp **(1/2)
    return(my_temp)

print("RMSE = ", my_RMSE(y,predicted_y))
