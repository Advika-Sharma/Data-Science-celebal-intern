#matplotlib 
#Matplotlib is a low level graph plotting library in python that serves as a visualization utility.
#Matplotlib was created by John D. Hunter.
#Matplotlib is open source and we can use it freely.
#Matplotlib is mostly written in python, a few segments are written in C, Objective-C and Javascript for Platform compatibility.

import matplotlib
print(matplotlib.__version__)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

#the plot function
#The plot function is used to plot the graph.
#It takes two parameters, the x-coordinates and the y-coordinates of the points to be plotted.


#markers
#Markers are used to highlight the points on the graph.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

#line styles
#Line styles are used to change the style of the line in the graph.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

#labels 
#Labels are used to add labels to the x-axis and y-axis of the graph.

import matplotlib.pyplot as plt
import numpy as np  
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', label = "Line 1")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("My first graph!")
plt.legend()
plt.show()

#grid 
#Grid is used to add a grid to the graph.
 
import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

plt.plot(x, y)

plt.grid()

plt.show()

#subplot 
#Subplot is used to create multiple plots in a single figure.

import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)

plt.show()

#scatter plot

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()

#bar chart

import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)
plt.show()

#histogram
#A histogram is used to represent the distribution of numerical data by dividing the data into bins.

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 

#pie chart

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show() 