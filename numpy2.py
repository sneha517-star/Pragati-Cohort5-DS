import numpy as np 
#creating a list of lists of 5 mpg, horsepower and acceleration values
car_attributes = [[18, 15, 18, 16, 17],[130, 165, 150, 150, 140],[307, 350, 318, 304, 302]]
#converting dtype
car_attributes_arr = np.array(car_attributes, dtype = 'float')
print(car_attributes_arr)
print(car_attributes_arr.dtype)
