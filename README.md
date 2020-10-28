# Plotting sorted data

We have learned how the value of y in a sentence such as the one below can be found:

_y % of the data points are less than or equal to x._

We still need to decide on the value of x here, however.  If we want to represent all the data compactly, it is not clear how we should decide on these x values. The problem is that the values that should be used for x in sentences such as the one above will depend on the data that we have obtained.  

It would be nice if we could flip the problem around.  In other words, it would be nice if we could provide a y value and extract x.  If we had a method that allowed us to obtain the x value for a given value of y in a sentence like the one above, this could be deployed to investigate any data set.  We could, for instance, write a general summary for any data set as follows:

_a is the minimum value obtained
25% of the data points are less than or equal to b
50% of the data points are less than or equal to c
75% of the data points are less than or equal to d   
e is the maximum value obtained_

A similar block of text could then be written to summarise the results for any set of experiments we might perform.  This form of analysis should be familiar to you.  As you no no doubt know that b is a statistic known as the lower quartile, c is the median and d is the upper quartile.  

Over the next few of these tasks, we are going to learn how to use Python to compute the quantities described above.  The first step in this procedure is to sort the data into ascending order.  Thankfully, this is relatively straightforward.  If we have an np array of unsorted data called `x` and if you issue the command:

````
x.sort() 
````

then the elements of `x` are sorted into ascending order.  Try using this command now to sort out the data in the array `x` whose elements have been set by reading in the `data.dat` file.

To complete the exercise use the Python you have learned to generate a plot of the data in the data.dat file in which the y coordinates of the points are the elements of `x` sorted into ascending order.  You should create an array holding the x coordinates.  These x-coordinates of points will be the integers from 1 up to 200 (the number of points in the file).  The first point in your graph will thus be plotted at `(1,x[0])`, the second will be at `(2,x[1])`, the third at `(3,x[2])` and so on.  Critically, however, when you plot the graph, the array `x` will be sorted into ascending order.
