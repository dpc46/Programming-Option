import glob
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from scipy.optimize import curve_fit, minimize


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

    f.close()
all_data = np.array(all_data)
reduced_data = np.array(reduced_data)


# parameterised function f(x,y) to be fitted is 5th order polynomial in x and y
def function(data, a, b, c, d, e, f, g, h, i, j, k, l, m):
    x = data[0]
    y = data[1]
    return a + b*(x) + c*(y) + d*(x**2) + e*(y**2) + f*(x**3) + g*(y**3) + h*(x**4) + i*(y**4) + j*(x**5) + k*(y**5)+ l*(x**6) + m*(y**6)

# convert data into proper format
x_data = all_data[:,0]                                                          # r, bond lengths
y_data = all_data[:,1]                                                          # theta, bond angle
z_data = all_data[:,2]                                                          # energy of molecule

# get fit parameters from scipy curve fit
parameters, covariance = curve_fit(function, [x_data, y_data], z_data)

# create surface function model
# setup data points for calculating surface model
model_x_data = np.linspace(min(x_data), max(x_data), 30)
model_y_data = np.linspace(min(y_data), max(y_data), 30)
X, Y = np.meshgrid(model_x_data, model_y_data)

# calculating Z = f(x,y) for fitted model
Z = function(np.array([X, Y]), *parameters)

# setup figure object
fig = plt.figure()
ax = Axes3D(fig)

# plot model surface
ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)

# plot input data
bond_length_x = reduced_data[:,0]
theta_y = reduced_data[:,1]
energy_z = reduced_data[:,2]

 # ax.scatter(bond_length_x, theta_y, energy_z, c='r', marker='.')
# axes labels
ax.set_xlabel('Bond Length / Angstroms')
ax.set_ylabel('Bond Angle, Theta')
ax.set_zlabel('Energy, E / Hartrees')
plt.show()

# calculating frequencies of normal modes
k_r = 2 * parameters[3]
k_theta = 2 * parameters[4]
args=tuple(parameters)
min = minimize(function, [1,100], args)
