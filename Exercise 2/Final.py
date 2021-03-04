import glob
import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from scipy.optimize import curve_fit, minimize

path = 'H2Ooutfiles/*.*'                            # path relative to program
file_list = glob.glob(path)

all_data = []                                       # defining empty lists for data
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
    energy = float(l[4])                            # energy is the 4th entry in the line of any line that contains SCF Done

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
    all_data.append(data)                           # adding current row to list of all rows

    if int(theta) % 5 == 0:                         # reduced set of data for less visually noisy plotting
        reduced_data.append(data)                   # adding current row to list if theta is a multiple of 5


    f.close()
all_data = np.array(all_data)                       # converting full and reduced data sets to numpy arrays
reduced_data = np.array(reduced_data)               # can be treated as matrices

# parameterised function f(x,y) to be fitted is 5th order polynomial in x and y
def function(data, a, b, c, d, e, f, g, h, i, j, k, l, m):
    x = data[0]
    y = data[1]
    return a + b*(x) + c*(y) + d*(x**2) + e*(y**2) + f*(x**3) + g*(y**3) + h*(x**4) + i*(y**4) + j*(x**5) + k*(y**5)+ l*(x**6) + m*(y**6)


x_data = all_data[:,0]                                                          # r, bond lengths
y_data = all_data[:,1]                                                          # theta, bond angle
z_data = all_data[:,2]                                                          # energy of molecule


parameters, covariance = curve_fit(function, [x_data, y_data], z_data)          # obtaining fit parameters from curve_fit function

model_x_data = np.linspace(min(x_data), max(x_data), 30)                        # creating X, Y grid for surface plot
model_y_data = np.linspace(min(y_data), max(y_data), 30)
X, Y = np.meshgrid(model_x_data, model_y_data)

Z = function(np.array([X, Y]), *parameters)                                     # using fitted model to calculate energies

fig = plt.figure()                                                              # setting up plot
ax = Axes3D(fig)

ax.plot_surface(X, Y, Z, cmap=cm.coolwarm)                                      # plotting fitted surface

bond_length_x = reduced_data[:,0]                                               # setting up data for scatter plot
theta_y = reduced_data[:,1]
energy_z = reduced_data[:,2]

ax.scatter(bond_length_x, theta_y, energy_z, c='r', marker='.')

ax.set_xlabel('Bond Length / Angstroms')                                        # axes labels
ax.set_ylabel('Bond Angle, Theta')
ax.set_zlabel('Energy, E / Hartrees')
plt.show()

args = tuple(parameters)
min = minimize(function, [0.94,104], args)                                      # finding the energy minimum from quintic model

min_array = min['x']                                                            # extracting minimum coordinates
r_0 = min_array[0]                                                              # assigning r_0
theta_0 = min_array[1]                                                          # assigning theta_0
E_min = min['fun']                                                              # extracting energy minimum

                                                                                # reducing the range of the data to around the min.
min_data = []
for i in all_data:
    if (r_0 - 0.15)<i[0]<(r_0 + 0.15) and (theta_0 - 15)<i[1]<(theta_0 + 15):   # taking values of r_0 +/- 0.15 and theta_0 +/- 15
        min_data.append(i)
min_data = np.array(min_data)

                                                                                # taking a reduced set of data, to better approximate the min.
x_data = min_data[:,0]                                                          # r, bond lengths
y_data = min_data[:,1]                                                          # theta, bond angle
z_data = min_data[:,2]                                                          # energy of molecule

def function(data, a, b, c, d, e):                                              # defining a quadratic in x and y for fit about energy min.
    x = data[0]
    y = data[1]
    return a + b*(x) + c*(y) + d*(x**2) + e*(y**2)

parameters, covariance = curve_fit(function, [(x_data-r_0), (y_data-theta_0)], z_data) #obtaining parameters for quadratic fit about energy min.

k_r = 2 * parameters[3]                                                         # assigning the spring constant by comparison
k_theta = 2 * parameters[4]
m_u =  1.66053886e-27                                                           # defining the AMU
a = (1 / (2 * (math.pi)))                                                       # defining the constant a
c = 435.97                                                                      # conversion factor for k from Hartree Angstrom^-2 to Nm-1

k_r = c * k_r                                                                   # changing units of spring constant
k_theta = c * k_theta                                                           # changing units of spring constant

v_1 = a * (math.sqrt(k_r / (2 * m_u)))                                          # gives v in Hz
v_2 = a * math.sqrt(((k_theta * 2) / (m_u * ((r_0) ** 2))))                     # gives v in Hz

b = 3.3356e-11                                                                  # Hz to cm-1 conversion
v_1 = v_1 * b                                                                   # symetric stretch frequency in cm-1
v_2 = v_2 * b                                                                   # symmetric bend frequency in cm-1

print(v_1)                                                                      # should 3700cm-1
print(v_2)                                                                      # should be 1600cm-1


# need to add plot title, fix v1 and save plots. May want to plot only surface
