import numpy as np

np_height = np.array([1.73, 1.80, 1.65, 1.75, 1.85]) 
np_weight = np.array([65.00, 45.00, 67.00, 34.00, 67.00]) 

bmi = np_weight / np_height ** 2
print(bmi[bmi > 20])

#2
np_2d = np.array([[1.73, 1.80, 1.65, 1.75, 1.85],
                  [65.00, 45.00, 67.00, 34.00, 67.00]]) 

bmi = np_weight / np_height ** 2
print(np_2d[:, 0:2])

#3
np_height1 = np.round(np.random.normal(1.75, 0.20, 5000), 2)
np_weight1 = np.round(np.random.normal(60.32, 15.00, 5000), 2)

np_city = np.column_stack((np_height1, np_weight1))
print(np_city)

#4
np_mean = np.mean(np_city[:, 0])
np_median = np.median(np_city[:, 0])
np_standard_dev = np.std(np_city[:, 0])
np_correlation = np.corrcoef(np_city[:, 0], np_city[:, 1])
print(np_mean)  
print(np_median)
print(np_standard_dev)
print(np_correlation)