f = open(r"C:\Users\danpc\OneDrive - University of Cambridge\1. Chemistry\II\Programming\\H2O.r0.70theta70.0.out", "r")
lines = f.readlines()                           # defining tuple lines
s = "SCF Done"                                  # key term
i = 0

while i < len(lines):                           # searching for key term (SCF Done)
   if lines[i].find(s)!=-1:
     break
   i += 1

l = lines[i].split()                            # splitting line into separate components by spaces
energy = l[4]                                   # energy is the 4th entry in the line
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
data = np.array([r, theta, energy])             # creating an array
f.close()
