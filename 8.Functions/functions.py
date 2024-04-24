# First function example: Add 1 to a and store as b

def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)
#----------------------------------------------------------------------

# Get a help on add function
# First function example: Add 1 to a and store as b
def add(a):
    """
    add 1 to a
    """
    b = a + 1
    print(a, "if you add one", b)
    return(b)
help(add)
# Call the function add()
add(1)
#-------------------------------------------------------------------------------

# Define a function for multiple two numbers
def Mult(a, b):
    c = a* b
    return(c)
    print('This is not printed') 
result = Mult(12,2)
print(result)

# Use mult() multiply two integers
Mult(2, 3)

# Use mult() multiply two floats
Mult(10.0, 3.14)
# Use mult() multiply two different type values together
Mult(2, "Michael Jackson ")
#-----------------------------------------------------------------------------------

#Variables--------------------------------------------------------------------------------------
# Function Definition
def square(a):
    # Local variable b
    b = 1
    c = a * a + b
    print(a, "if you square + 1", c) 
    return(c)

# Initializes Global variable  
def square(a):
    """
    Square the input
    """
    c=a*a
    print("The square of",a,"is","c")
    return(c)
x = 3
# Makes function call and return function a y
y = square(x)
y

# Directly enter a number as parameter
square(2)
#-----------------------------------------------------------------------------------------

# Define functions, one with return value None and other without return value

def MJ():
    print('Michael Jackson')
    
def MJ1():
    print('Michael Jackson')
    return(None)

# See the output
MJ()
# See the output
MJ1()
# See what functions returns are
print(MJ())
print(MJ1())
#-----------------------------------------------------------------------------------------------

# Define the function for combining strings
def con(a, b):
    return(a + b)
# Test on the con() function
con("This ", "is")
#-------------------------------------------------------------------------------------------------

#SIMPLIFYING CODE------------------------------------
#block1
a1 = 4
b1 = 5
c1 = a1 + b1 + 2 * a1 * b1 - 1
if(c1 < 0):
    c1 = 0 
else:
    c1 = 5
c1  

#block2
a2 = 0
b2 = 0
c2 = a2 + b2 + 2 * a2 * b2 - 1
if(c2 < 0):
    c2 = 0 
else:
    c2 = 5
c2 

# MAKING A FUNC TO DEFYNING THE ADD FUNC
def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c)   
#set from BLOCK1
a1 = 4
b1 = 5
c1 = Equation(a1, b1)
c1
#set from BLOCK2
a2 = 0
b2 = 0
c2 = Equation(a2, b2)
c2
#-------------------------------------------------------------------------------------

#predefined
# Build-in function print()
album_ratings = [10.0, 8.5, 9.5, 7.0, 7.0, 9.5, 9.0, 9.5] 
print(album_ratings)
# Use sum() to add every element in a list or tuple together
sum(album_ratings)
# Show the length of the list or tuple
len(album_ratings)
#--------------------------------------------------------------------------------------

#Comparison-------------------------------------------------------------------------------
#Compare Two Strings Directly using in operator
# add string
string= "Michael Jackson is the best"
# Define a funtion
def check_string(text):
    
# Use if else statement and 'in' operatore to compare the string
    if text in string:
        return 'String matched'
    else:
        return 'String not matched'
check_string("Michael Jackson is the best")

#Compare two strings using == operator and function
def compareStrings(x, y):
# Use if else statement to compare x and y
    if x==y:
        return True   
# Declare two different variables as string1 and string2 and pass string in it
string1 = "Michael Jackson is the best"
string2 = "Michael Jackson is the best"
# Declare a variable to store result after comparing both the strings
check = compareStrings(string1, string2)
#Use if else statement to compare the string
if check==True:
    print("\nString Matched")
else:
    print("\nString not Matched")
    


# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the dictionary
    print("The Frequency of words is:",Dict)
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")
#------------------------------------------------------------------------------------------------------------------------------------

#DEFINING GLOBAL VAR in func---------------------------------------------------------------------------------
artist = "Michael Jackson"
def printer(artist):
    global internal_var
    internal_var= "Whitney Houston"
    print(artist,"is an artist")

printer(artist) 
printer(internal_var)
#----------------------------------------------------------------------------------------------------------------------

#COLLECTION OF ARGUMENTS USING " * "------------
def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

#The arguments can also be packed into a dictionary as shown:
def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')
    
#Functions can be incredibly powerful and versatile. They can accept (and return) data types, objects and even other functions as arguements. Consider the example below:
def addItems(list):
    list.append("Three")
    list.append("Four")
myList = ["One","Two"]
addItems(myList)
myList
#-----------------------------------------------------------------------------------------------------------------------------

#QUIZ ON FUNCTIONS---------------------------------------------------------------------------------------------------------------------
#QUESTION 1) Come up with a function that divides the first input by the second input:
#def division(a,b):
#    global c
#    c=a/b
#    return c

#division(6,3)
def div(a, b):
    return(a/b)


#QUESTION 2)Use the function con for the following question.
# Use the con function for the following question
def con(a, b):
    return(a + b)

#QUESTION 3)Can the con function we defined before be used to add two integers or strings?
# Write your code below and press Shift+Enter to execute
def con(a, b):
    return(a + b)
con("MJ ","is the best")


#QUESTION 4)Can the con function we defined before be used to concatenate lists or tuples?
# Write your code below and press Shift+Enter to execute
def con(a, b):
    return(a + b)

con(["Hi","Myself"],["Srinjoy"])

#QUESTION 5)Write a function code to find total count of word little in the given string: "Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"**
# Python Program to Count words in a String using Dictionary
def freq(string):
    
    #step1: A list variable is declared and initialized to an empty list.
    words = []
    
    #step2: Break the string into list of words
    words = string.split() # or string.lower().split()
    
    #step3: Declare a dictionary
    Dict = {}
    
    #step4: Use for loop to iterate words and values to the dictionary
    for key in words:
        Dict[key] = words.count(key)
        
    #step5: Print the total count of word "little"
    print("The Frequency of words little is:",Dict["little"])
    
#step6: Call function and pass string in it
freq("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went \
Everywhere that Mary went The lamb was sure to go")



