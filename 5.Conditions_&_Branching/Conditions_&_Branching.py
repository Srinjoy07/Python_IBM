#COMPARISON OPERATORS------------------------------------------------------------
#equal: ==
#not equal: !=
#greater than: >
#less than: <
#greater than or equal to: >=
#less than or equal to: <=

# Condition Equal
a = 5
a == 6   #o/p:False

# Greater than Sign
i = 6
i > 5

# Greater than Sign
i = 2
i > 5

# Inequality Sign
i = 2
i != 6

# Inequality Sign
i = 6
i != 6

# Use Equality sign to compare the strings
"ACDC" == "Michael Jackson"

# Use Inequality sign to compare the strings
"ACDC" != "Michael Jackson"

# Compare characters
'B' > 'A'

# Compare characters
'BA' > 'AB'


#BRANCHING-----------------------------------------------------------------------

#EXAMPLE_1          
# If statement example
age = 19
#age = 18
#expression that can be true or false
if age > 18:   
    #within an indent, we have the expression that is run if the condition is true
    print("you can enter" )
#The statements after the if statement will run regardless if the condition is true or false 
print("move on")

# Else statement example
age = 18
# age = 19
if age > 18:
    print("you can enter" )
else:
    print("go see Meat Loaf" )
print("move on")

# Elif statment example
age = 18
if age > 18:
    print("you can enter" )
elif age == 18:
    print("go see Pink Floyd")
else:
    print("go see Meat Loaf" )    
print("move on")

#################################

#EXAMPLE_2
# Condition statement example
#album_year = 1983
album_year = 1990
if album_year > 1980:
    print("Album year is greater than 1980")
print('do something..')

# Condition statement example
album_year = 1983
#album_year = 1980
if album_year > 1980:
    print("Album year is greater than 1980")
else:
    print("less than 1980")
print('do something..')

#LOGICAL OPERATORS---------------------------------------------------------------------------------------------------
#and
#or
#not

#Example
#Condition statement example
album_year = 1980
if(album_year > 1979) and (album_year < 1990):
    print ("Album year was in between 1980 and 1989")    
print("")
print("Do Stuff..")

# Condition statement example
album_year = 1990
if(album_year < 1980) or (album_year > 1989):
    print ("Album was not made in the 1980's")
else:
    print("The Album was made in the 1980's ")
    
# Condition statement example
album_year = 1983
if not (album_year == 1984):
    print ("Album year is not 1984")
    
    
    
#QUESTIONS TO SOLVE--------------------------------------------------------------------------------------------------------------
#Question-1)There are 2 sisters, Annie and Jane, born in 1996 and 1999 respectively. They want to know who was born in a leap year. Write an if-else statement to determine who was born in a leap year.
# Write your code below and press Shift+Enter to execute
Annie_year=1996
Jane_year=1999
if Annie_year%4==0:
    print("Annie was born in a leap year.",Annie_year)
elif Jane_year%4==0:
    print("Jane was born in a leap year.")
else:
    print("None was born in leap year.")
    
#Question-2)In a school canteen, children under the age of 9 are only given milk porridge for breakfast. Children from 10 to 14 are given a sandwich, and children from 15 to 17 are given a burger. The canteen master asks the age of the student and gives them breakfast accordingly. Sam's age is 10. Use if-else statement to determine what the canteen master will offer to him.
# Write your code below and press Shift+Enter to execute
age=10
if age<=9:
    print("Milk porrdige is served.")
elif age>=10 and age<=14:
    print("Sandwich is served.")
elif age>=15 and age<=17:
    print("Burger is served")