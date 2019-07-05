dataset=[
[2,4,8.5,196],
[2.4,4,9.6,221],
[1.5,4,5.9,136],
[3.5,6,11.1,255],
[3.5,6,10.6,244],
[3.5,6,10,230],
[3.5,6,10.1,232],
[3.7,6,11.1,255],
[3.7,6,11.6,267],
    ]


len_dataset = len(dataset)
independent_variables = []
dependent_variables = []


### selecting first values of each row as "y" or dependent values
for x in range(0, len_dataset):
    independent_variables.append(dataset[x][0])
    
sum_independent_variables = 0

### calculating sum of "y" or dependent values
for x in independent_variables:
    sum_independent_variables = x + sum_independent_variables

    
### selecting first values of each row as "x" or independent values
for x in range(0, len_dataset):
    dependent_variables.append(dataset[x][3])

sum_dependent_variables = 0

### calculating sum of "x" or independent values
for x in dependent_variables:
    sum_dependent_variables = x + sum_dependent_variables

    
    
### calculating average of "x" or independent values
average_independent_variables = sum_independent_variables / len_dataset
aiv = average_independent_variables

### calculating average of "y" or dependent values
average_dependent_variables = sum_dependent_variables / len_dataset
adv = average_dependent_variables


### calculating theta1
theta_1 = 0
theta1_numerator = 0
theta1_denumerator = 0
for x in range(0, len(dependent_variables)):
    theta1_numerator = ((independent_variables[x]-aiv)*(dependent_variables[x]-adv)) + theta1_numerator
    theta1_denumerator = ((independent_variables[x]-aiv)**2) + theta1_denumerator

theta_1 = theta1_numerator / theta1_denumerator

### calculating theta0
theta_0 = adv - (theta_1*aiv)



print("Calculation Summary")
print("Sum of X (Independent Variables)=",sum_independent_variables)
print("Sum of Y (Dependent Variables)=",sum_dependent_variables)
print("Mean X (Average of Dependent Variables)=",aiv)
print("Mean Y (Average of Independent Variables)=",adv)
print("Sum of squares (SSX)(θ1 Denumerator)=",theta1_denumerator)
print("Sum of products (SP))(θ1 Numerator)=",theta1_numerator)
print(" ")
print("Regression Equation = ŷ = bX + a")
print("ŷ = θ0 + θ1X1")
print(" ")
print("b(θ1) = SP/SSX =",theta1_numerator,"/",theta1_denumerator,"=",theta_1)
print(" ")
print("a(θ0) = MY-bMX =",adv,"- (",theta_1,"*",aiv,")=",theta_0)
print("θ0 = ȳ - θ1x̄")
print(" ")
print("ŷ =",theta_1,"X+",theta_0)


### setting "x" in ŷ = θ0 + θ1X1
target_independent_value = 2.4

### predicting the y for selected row
final_prediction = theta_0 + (theta_1 * target_independent_value)
print("final_prediction",final_prediction)
