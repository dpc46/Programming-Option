import glob
path = 'H2Ooutfiles/*.*'
file_list = glob.glob(path)
all_data = []

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
    energy = float(l[4])                                   # energy is the 4th entry in the line
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

    import numpy as np
    data = np.array([r, theta, energy])             # creating a 1x3 array for this file
    all_data.append(data)                           # adding array to the list all_data
    f.close()
mat = np.array(all_data)                            # turning all data into an nx3 matrix
print(mat)
