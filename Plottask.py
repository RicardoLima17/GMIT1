# Author Ricardo Rodriguers

#This program displays a plot of the functions 

import numpy as np
import matplotlib.pyplot as plt

#first function x
#range 0 to 4
x = np.linspace(0,4)
y=  x

#naming the label for each function
plt.plot(x,y, label= "f(x)= x")

#second function x2^2
# range 0 to 4
x2= np.linspace(0,4)
y2= x2**2

#naming the label for each function
plt.plot(x2,y2, label= "g(x)= $x^2$")

#third function x3^3
# range 0 to 4
x3= np.linspace(0,4)
y3= x3 **3

#naming the label for each function
plt.plot(x3, y3, label= "h(x)= $x^3$")

#y-axis and x-axis
plt.xlabel("x-axis")
plt.ylabel("y-axis")


#this places the legend on the upper left of the plot
plt.legend(loc="upper left")

#title to plot
plt.title("Function x")

#adding grid
plt.grid()

#show plot
#plt.show()


plt.savefig('plottask.png')
#References
#https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
#https://www.w3schools.com/python/matplotlib_pyplot.asp
#lectures
