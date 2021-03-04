import glob
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
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

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

bond_length_x = reduced_data[:,0]
theta_y = reduced_data[:,1]
energy_z = reduced_data[:,2]

ax.scatter(bond_length_x, theta_y, energy_z, c='r', marker='.')

ax.set_xlabel('Bond Length / Angstroms')
ax.set_ylabel('Bond Angle, Theta')
ax.set_zlabel('Energy, E / Hartrees')

plt.show()
