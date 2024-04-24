# import numpy library
import numpy as np 

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
print(a)

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

#check numpy version
print(np.__version__)

#----------------------------------------------------------------------------------------------------------


#Type---------

# Check the type of the array
type(a)

#As numpy arrays contain data of the same type, we can use the attribute "dtype" to obtain the data type of the array’s elements. In this case, it's a 64-bit integer:
a.dtype
########################################################################################################################


#Assign Value-------------------------------

# Create numpy array
c = np.array([20, 1, 2, 3, 4])
c

# Assign the first element to 100
c[0] = 100
c

# Assign the 5th element to 0
c[4] = 0
c

#TRY YOURSELF--
a = np.array([10, 2, 30, 40,50])
# Enter your code here
a[1]=20
print(a)

##################################################################################################################################

#Slicing---------------------

# Slicing the numpy array
d = c[1:4]
d

# Set the fourth element and fifth element to 300 and 400
c[3:5] = 300, 400
c
#We can also define the steps in slicing, like this: [start:end:step].
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])
#If we don't pass start its considered 0
print(arr[:4])
#If we don't pass end it considers till the length of array.
print(arr[4:])
#If we don't pass step its considered 1
print(arr[1:5:])

#TRY YOURSELF---------------------
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
d=arr[1:8:2]
print(d)

##############################################################################################################################################

#ASSIGN value with list

# Create the index list
select = [0, 2, 3, 4]
select

# Use List to select elements
d = c[select]
d

# Assign the specified elements to new value
c[select] = 100000
c

########################################################################################################################################################

#Other attributes----------------------------------

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])
a

# Get the size of numpy array
a.size

# Get the number of dimensions of numpy array
a.ndim

# Get the shape/size of numpy array
a.shape

#TRY YOURSELF---------------
#Find the size ,dimension and shape for the given array b
b = np.array([10, 20, 30, 40, 50, 60, 70])

b.size  ##for size

b.ndim  ##for dimension

b.shape #for the shape
# Enter your code here

##################################################################################################################################################################

#Numpy Statistical Functions-----------------------

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()
mean
# Get the standard deviation of numpy array
standard_deviation=a.std()
standard_deviation

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])
b
# Get the biggest value in the numpy array
max_b = b.max()
max_b
# Get the smallest value in the numpy array
min_b = b.min()
min_b

#TRY YOURSELF-----------------------------
#Find the sum of maximum and minimum value in the given numpy array
c = np.array([-10, 201, 43, 94, 502])

d=np.max(c) #finding max
print(d)

e=np.min(c)
print(e)

#adding min and max
sum=np.add(d,e)
print(sum)

####################################################################################################################################################################

#Numpy Array Operations----------------------------


#ADDITION____________________________________________________________
u = np.array([1, 0])
u
v = np.array([0, 1])
v
# Numpy Array Addition
z = np.add(u, v)
z

#VERY IMPORTANT----

# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays
Plotvec1(u, z, v)
#TRY
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3=np.add(arr1,arr2)
arr3
# Enter your code here

#DIVISION___________________________________________________________________________________________________

a = np.array([10, 20, 30])
a

b = np.array([5, 10, 15])
b

c = np.subtract(a, b)
print(c)

#TRY----
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([20, 21, 22, 23, 24, 25])

arr3=np.subtract(arr1,arr2)
arr3
# Enter your code here


#MULTIPLICATION_________________________________________________________________________________________________________
# Create a numpy array
x = np.array([1, 2])
x

# Create a numpy array
y = np.array([2, 1])
y

# Numpy Array Multiplication
z = np.multiply(x, y)
z

#TRY-------------
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([2, 1, 2, 3, 4, 5])

arr3=np.multiply(arr1,arr2)
arr3
# Enter your code here


#DIVISION___________________________________________________________________________________________________________________________
a = np.array([10, 20, 30])
a
b = np.array([2, 10, 5])
b
c = np.divide(a, b)
c

#TRY-------------
arr1 = np.array([10, 20, 30, 40, 50, 60])
arr2 = np.array([3, 5, 10, 8, 2, 33])

arr3=np.divide(arr1,arr2)
arr3
# Enter your code here


################################################################################################################################################

#DOT PRODUCT------------------------------------------------------------------------------------------------
X = np.array([1, 2])
Y = np.array([3, 2])
# Calculate the dot product
np.dot(X, Y)

#Elements of X
print(X[0])
print(X[1])
#Elements of Y
print(Y[0])
print(Y[1])

#TRY-----------
arr1 = np.array([3, 5])
arr2 = np.array([2, 4])

# Enter your code here
arr3=np.dot(arr1,arr2)
arr3




#ADDING constant to a numpy array-------------------------------
# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 
u
# Add the constant to array
u + 1

###########################################################################################################################################################

#Mathematical Functions---------------------------------------------------------------------------------------------------------------------------------------------

# The value of pi
np.pi
# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])
# Calculate the sin of each elements
y = np.sin(x)
y

###################################################################################################################################################################

#Linspace---------------------

# Makeup a numpy array within [-2, 2] and 5 elements
import numpy as np
np.linspace(-2, 2, num=5)

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Make a numpy array within [0, 2π] and 100 elements 
import numpy as np
np.pi
x = np.linspace(0, 2*np.pi, num=100)

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
#import matplotlib.pyplot as plt
plt.plot(x, y)


############################################################################################################################################################################

#Iterating 1-D Arrays--------------------------------------------------------------------------------------------------------------------------------------------------------------

#If we execute the numpy array, we get in the array format
arr1 = np.array([1, 2, 3])
print(arr1)
#But if you want to result in the form of the list, then you can use for loop:
for x in arr1:
  print(x)
  

######################################################################################################################################################################################


#QUIZ ON 1-D---------------------------

#Implement the following vector subtraction in numpy: u-v
# Write your code below and press Shift+Enter to execute
u = np.array([1, 0])
v = np.array([0, 1])

z=np.subtract(u,v)
print(z)



#Multiply the numpy array z with -2:
# Write your code below and press Shift+Enter to execute

z = np.array([2, 4])

m=np.multiply(z,-2)
m
#-2 * z



#Consider the list [1, 2, 3, 4, 5] and [1, 0, 1, 0, 1]. Cast both lists to a numpy array then multiply them together:

a=np.array([1, 2, 3, 4, 5])
b=np.array([1, 0, 1, 0, 1])

c=np.multiply(a,b)
c




#Convert the list [-1, 1] and [1, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt


def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)
    
# Write your code below and press Shift+Enter to execute
a=np.array([-1,1])
b=np.array([1,1])

c=np.dot(a,b)
print(c)

Plotvec2(a,b)

#SAME QUESTIONS DOWN BELOW________________________________
#Convert the list [1, 0] and [0, 1] to numpy arrays a and b. Then, plot the arrays as vectors using the function Plotvec2 and find their dot product:
#sol:
a = np.array([1, 0])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

#Convert the list [1, 1] and [0, 1] to numpy arrays a and b. Then plot the arrays as vectors using the fuction Plotvec2 and find their dot product:
#sol:
a = np.array([1, 1])
b = np.array([0, 1])
Plotvec2(a, b)
print("The dot product is", np.dot(a, b))

#Why are the results of the dot product for [-1, 1] and [1, 1] and the dot product for [1, 0] and [0, 1] zero, but not zero for the dot product for [1, 1] and [0, 1]?
         #Hint: Study the corresponding figures, pay attention to the direction the arrows are pointing to.
#Sol:The vectors used for question 4 and 5 are perpendicular. As a result, the dot product is zero.
         
#Convert the list [1, 2, 3] and [8, 9, 10] to numpy arrays arr1 and arr2. Then perform Addition , Subtraction , Multiplication , Division and Dot Operation on the arr1 and arr2.
#Sol:
arr1 = np.array([1, 2, 3])
arr2 = np.array([8, 9, 10])
arr3 = np.add(arr1, arr2)
arr3
arr4 = np.subtract(arr1, arr2)
arr4
arr5 = np.multiply(arr1, arr2)
arr5
arr6 = np.divide(arr1, arr2)
arr6
arr7 = np.dot(arr1, arr2)
arr7

#Convert the list [1, 2, 3, 4, 5] and [6, 7, 8, 9, 10] to numpy arrays arr1 and arr2. Then find the even and odd numbers from arr1 and arr2.
#Sol:
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

#Starting index in slice is 1 as first even element(2) in array1 is at index 1
even_arr1 = arr1[1:5:2]
print("even for array1",even_arr1)
    
#Starting index in slice is 0 as first odd element(1) in array1 is at index 0
odd_arr1=arr1[0:5:2]
print("odd for array1",odd_arr1)

#Starting index in slice is 0 as first even element(6) in array2 is at index 0
even_arr2 = arr2[0:5:2]
print("even for array2",even_arr2)
    
    
#Starting index in slice is 1 as first odd element(7) in array2 is at index 1
odd_arr2=arr2[1:5:2]
print("odd for array2",odd_arr2)

