#check for errors--------------------------------------------------------------------------
1/0  #ZeroDivisionError

y = a + 5  #NameError

a = [1, 2, 3]
a[10]  #IndexError



#Exception Handling--------------------------------------------------------------------

# potential code before try catch
try:
    # code to try to execute
except:
    # code to execute if there is an exception
    
# code that will still execute if there is an exception


#TRY_EXCEPT EXAMPLE-------------------------
a = 1
try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except:
    print("There was an error")  
        

#TRY_EXCEPT-SPECIFIC EXAMPLE---------------------
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
    print("Success a=",a)
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
        


#Try Except Else and Finally Example------------
a = 1

try:
    b = int(input("Please enter a number to divide a"))
    a = a/b
except ZeroDivisionError:
    print("The number you provided cant divide 1 because it is 0")
except ValueError:
    print("You did not provide a number")
except:
    print("Something went wrong")
else:
    print("success a=",a)
finally:
    print("Processing Complete")
    
#-----------------------------------------------------------------------------------------------------------------------------


#PRACTICE PROBLEMS
#Exercise 1: Handling ZeroDivisionError
#Imagine you have two numbers and want to determine what happens when you divide one number by the other. To do this, you need to create a Python function called safe_divide. You give this function two numbers, a 'numerator' and a 'denominator'. The 'numerator' is the number you want to divide, and the 'denominator' is the number you want to divide by. Use the user input method of Python to take the values.
#The function should be able to do the division for you and give you the result. But here's the catch: if you try to divide by zero (which is not allowed in math), the function should be smart enough to catch that and tell you that it's not possible to divide by zero. Instead of showing an error, it should return None, which means 'nothing' or 'no value', and print "Error: Cannot divide by Zero.
def safe_divide(numerator,denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None

#Test case
numerator=int(input("Enter the numerator value:-"))
denominator=int(input("Enter the denominator value:-"))
print(safe_divide(numerator, denominator))


#Exercise 2: Handling ValueError
#magine you have a number and want to calculate its square root. To do this, you need to create a Python function. You give this function one number, 'number1'.
#The function should generate the square root value if you provide a positive integer or float value as input. However, the function should be clever enough to detect the mistake if you enter a negative value. It should kindly inform you with a message saying, 'Invalid input! Please enter a positive integer or a float value.
import math

def calculation(number1):
    try:
        result=math.sqrt(number1)
        print(f"Result: {result}")
    except ValueError:
        print("Error:'Invalid input! Please enter a positive integer or a float value.")
        
#value given
number1=float(input("Enter the number in float or integer:"))
calculation(number1)


#Exercise 3: Handling Generic Exceptions
#Imagine you have a number and want to perform a complex mathematical task. The calculation requires dividing the value of the input argument "num" by the difference between "num" and 5, and the result has to be stored in a variable called "result".
#You have to define a function so that it can perform that complex mathematical task. The function should handle any potential errors that occur during the calculation. To do this, you can use a try-except block. If any exception arises during the calculation, it should catch the error using the generic exception class "Exception" as "e". When an exception occurs, the function should display "An error occurred during calculation.
#Type your code here
def complex_calc(num):
    try:
        result = num/ (num-5)
        print(f"Result={result}")
    except Exception as e:
        print("An error occurred during calculation.")
    
#value for num
num1 = int(input("Enter value for num:-"))
complex_calc(num1)


