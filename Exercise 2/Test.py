import glob
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import curve_fit, minimize

r_0 = 0.9436669834498017
theta_0 = 100.75449458604727

path = 'H2Ooutfiles/*.*'
file_list = glob.glob(path)
all_data = []
reduced_data = []
for file in glob.glob(path):
    f = open(file, 'r')
    lines = f.readlines()                           # defining tuple lines
    s = "SCF Done"                                  # key term
    i = 0

    while i < len(lines):                           # searching for key term (SCF Done)
       if lines[i].find(s)!=-1:
         break
       i += 1

    l = lines[i].split()                            # splitting line into separate components by spaces
    energy = float(l[4])                            # energy is the 4th entry in the line
                                                    # of any line that contains SCF Done

    s = "theta"                                     # key term
    i = 0

    while i < len(lines):                           # searching for key term (theta)
       if lines[i].find(s)!=-1:
         break
       i += 1
    import re
    input = re.findall(r'\d+', lines[i])            # isolating the numbers from line

    r = float(input[1]) + (float(input[2]) / 100)   # picking out theta and r
    theta = input[3]

    data = np.array([r, theta, energy])             # creating an array
    data = data.astype(float)
    all_data.append(data)                           # adding current row to matrix

    if int(theta) % 5 == 0:                         # taking a less messy set of data
        reduced_data.append(data)

    if (r_0 - 0.15)<r<(r_0 + 0.15) and (theta_0 - 9.5)<float(theta)<(theta_0 - 9.5):
        minimum_data.append(data)


    f.close()
all_data = np.array(all_data)
reduced_data = np.array(reduced_data)


# coordinated of the minimum
r_0 = 0.9436669834498017
theta_0 = 100.75449458604727

# reducing the range of the data to around the min.
min_data = []
for i in all_data:
    if (r_0 - 0.15)<i[0]<(r_0 + 0.15) and (theta_0 - 15)<i[1]<(theta_0 + 15):
        min_data.append(i)
min_data = np.array(min_data)

#getting new function f(x,y) better defined around the min.
# parameterised function f(x,y) to be fitted is 5th order polynomial in x and y
def function(data, a, b, c, d, e, f, g, h, i, j, k):
    x = data[0]
    y = data[1]
    return a + b*(x) + c*(y) + d*(x**2) + e*(y**2) + f*(x**3) + g*(y**3) + h*(x**4) + i*(y**4) + j*(x**5) + k*(y**5)

# convert data into proper format
x_data = min_data[:,0]                                                          # r, bond lengths
y_data = min_data[:,1]                                                          # theta, bond angle
z_data = min_data[:,2]                                                          # energy of molecule

# get fit parameters from scipy curve fit
parameters, covariance = curve_fit(function, [(x_data), (y_data)], z_data)

k_r = 2 * parameters[3]
k_theta = 2 * parameters[4]
print(min_data)

for i in min_data:
    print (i)
    i = i + 1
