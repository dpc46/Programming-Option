import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()        #defining a single plot
xdata, ydata = [], []           #defining empty lists for xdata, ydata
ln, = plt.plot([], [], 'ro')    #plots x,y data when called

def init():
    ax.set_xlim(0, 2)     #defining the axes properly
    ax.set_ylim(0, 4)
    return ln,             #return exits a function and returns a value

def update(x):              #defining a function update, with arguement frame
    xdata.append(x)         #adding x data point to xdata
    ydata.append(x**2)         #adding y data point to ydata
    ln.set_data(xdata, ydata)
    return ln,                  #returns function with extra points added

ani = FuncAnimation(fig, update, frames=np.linspace(0, 2, 100),
                    init_func=init, blit=True, interval=1)
#interval is the time between frames in ms

plt.show()
