
### --- بخش مربوط به محاسبه متغیرهای معادله در رگرسیون خطی چندگانه --- start
### --- Calculating equation variables in multiple linear regression --- start

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

     print("x1y = ",x1y , "sum_x1y = ",sum_x1y)
     print("x2y = ",x2y , "sum_x2y = ",sum_x2y)
     print("x1x2 = ",x1x2 ,"sum_x1x2 = ",sum_x1x2)
     print("x1power2 = ",x1power2 , "sum_x1power2 = ",sum_x1power2)
     print("x2power2 = ",x2power2 , "sum_x2power2 = ",sum_x2power2)

     print("sum_x1", sum_x1)
     print("sum_x2", sum_x2)
     print("sum_y", sum_y)

### --- Calculating equation variables in multiple linear regression --- end
### --- بخش مربوط به محاسبه متغیرهای معادله در رگرسیون خطی چندگانه--- end



### --- بخش مربوط به محاسبه تتا0، تتا1 و تتا2 در رگرسیون خطی چندگانه--- start
### --- Calculating theta 0, theta 1 and theta 2 in multiple linear regression --- start

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

     print("\nteta0 = " , teta0)
     print("teta1 = " , teta1)
     print("teta2 = " , teta2)

     predicted_value = teta0 + (teta1 * input_x1) +  (teta2 * input_x2) 
     print("predicted value for x1=",input_x1, "and x2=",input_x2,"=", predicted_value)


def det(m):
     det_result = (m[0][0] * ((m[1][1] * m[2][2]) - (m[1][2] * m[2][1]))) -(m[0][1] * ((m[1][0] * m[2][2]) - (m[1][2] * m[2][0]))) +(m[0][2] * ((m[1][0] * m[2][1]) - (m[1][1] * m[2][0])))
     return (det_result)


x1 = [1,2,3,4]
x2 = [10,1,2,3]
y = [12,18,24,30]
input_size = len(x1)
input_x1 = 0
input_x2 = 0

paramcalc(x1,x2,y,input_x1,input_x2)

### --- Calculating theta 0, theta 1 and theta 2 in multiple linear regression --- end
### --- بخش مربوط به محاسبه تتا0، تتا1 و تتا2 در رگرسیون خطی چندگانه--- end

