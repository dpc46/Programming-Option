import numpy
from matplotlib import pyplot

nx = 41    #number of cells in the space
dx = 2 / (nx - 1) #spatial step
nt = 100    #the number of timesteps we want to calculate. Increasing number increases diffusion.
nu = 0.3   #the value of viscosity
sigma = .2 #sigma is a parameter, we'll learn more about it later
dt = sigma * dx**2 / nu #dt is defined using sigma ... more later!


u = numpy.zeros(nx)      #a numpy array with nx elements all equal to 0.
u[0] = 1  #I.C. is [A] = 1 at x = 0

un = numpy.zeros(nx) #our placeholder array, un, to advance the solution in time

for n in range(nt):  #iterate through time
    un = u.copy() #copy the existing values of u into un
    for i in range(1, nx - 1): #calculating concentration at each point in space
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1]) #this is the concentration function

#here we have a nested loop. we take a time-step, and calculate the new concentration
#at all points in space for this time-step. We then do the same for all the other time-steps
#we need to replace this function with the Oregonator. It would be nice if we were to define these loops
#as a function, which could then be called.

pyplot.plot(numpy.linspace(0, 2, nx), u)
pyplot.show()
