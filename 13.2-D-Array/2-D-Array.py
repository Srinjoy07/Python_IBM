# Import the libraries
import numpy as np

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
a


# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)
A
# Show the numpy array dimensions
A.ndim
# Show the numpy array shape
A.shape
# Show the numpy array size
A.size



#######################################################################

#Accessing Elements of a Numpy Array---------------------------------------------

# Access the element on the second row and third column
A[1, 2]
# Access the element on the second row and third column
A[1][2]
# Access the element on the first row and first column
A[0][0]
# Access the element on the first row and first and second columns
A[0,0:2]
# Access the element on the first and second rows and third column
A[0:2, 2]

###################################################################################

#BASIC OPERATIONS---------------------------------

#ADD------
# Create a numpy array X and Y
X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]])
# Add X and Y
Z = X + Y
Z

#Scaler MUL-----
# Create a numpy array Y
Y = np.array([[2, 1], [1, 2]]) 
# Multiply Y with 2
Z = 2 * Y
Z

#Numpy array MUL------
# Create a numpy array X and Y
X = np.array([[1, 0], [0, 1]]) 
Y = np.array([[2, 1], [1, 2]]) 
# Multiply X with Y
Z = X * Y
Z

#We can also perform matrix multiplication with the numpy arrays A and B as follows:
# Create a matrix A and B
A = np.array([[0, 1, 1], [1, 0, 1]])
B = np.array([[1, 1], [1, 1], [-1, 1]])
# Calculate the dot product
Z = np.dot(A,B)
Z

# Calculate the sine of Z
np.sin(Z)
# Get the transposed of Z
Z.T

#################################################################################################



#QUIZ on 2-D Array---------------------------

# Q)Consider the following list a, convert it to Numpy Array.
a = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
A = np.array(a)
A

# Q)Calculate the numpy array size.
A.size

#Q)Access the element on the first row and first and second columns.
A[0,0:2]

# Q)Perform matrix multiplication with the numpy arrays A and B.
B = np.array([[0, 1], [1, 0], [1, 1], [-1, 0]])
C = np.dot(A,B)
C
