# Use quotation marks for defining string
A="Michael Jackson"
print(A)

# Use single quotation marks for defining string
'Michael Jackson'

# Digitals and spaces in string
'1 2 3 4 5 6 '

# Special characters in string
'@#2_#]&*^%$'

# Print the string
print("hello!")

# Assign string to variable
name = "Michael Jackson"
print(name)


#indexing------------------------------------
# Print the first element in the string
Name="Michael Jackson"
print(Name[0])

# Print the element on index 6 in the string
Name="Michael Jackson"
print(Name[6])


#Negative index in Python------------------------
# Print the last element in the string
print(name[-1])

# Print the first element in the string
Name="Michael Jackson"
print(Name[-15])


#length of string-------------------------------
# Find the length of string
len("Michael Jackson")


#Slicing---------------------------------------
# Take the slice on variable name with only index 0 to index 3
Name="Michael Jackson"
name[0:4]

# Take the slice on variable name with only index 8 to index 11
name[8:12]

# Get every second element. The elments on index 1, 3, 5 ...
name[::2]

# Get every second element in the range from index 0 to index 4
name[0:5:2]


#String Concatenation----------------------------------
# Concatenate two strings
Name="Michael Jackson"
statement = name + "\tis the best"
print(statement)

# Print the string for 3 times
3 * "Michael Jackson "

# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
name


#Escape Sequence----------------------------------------
# New line escape sequence
print(" Michael Jackson \n is the best" )

# Tab escape sequence
print(" Michael Jackson \t is the best" )

# Include back slash in string
print(" Michael Jackson \\ is the best" )

# r will tell python that string will be display as raw string
print(r" Michael Jackson \ is the best" )


#String Operations------------------------------------------
# Convert all the characters in string to upper case
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)

# Convert all the characters in string to lower case
a = "MICHAEL JACKSON IS THE BEST"
print("Before lower:", a)
b = a.lower()
print("After lower:", b)

#replace method use
a = "Michael Jackson is the best"
b = a.replace('Michael', 'Janet')
print(b)

# Replace the old substring with the new target substring by removing some punctuations.
a = "Hello! Michael Jackson has: 12 characters."
print(a)
b = a.replace('!','').replace(':','').replace('.','')
print(b)

# Find the substring in the string. Only the index of the first elment of substring in string will be the output
name = "Michael Jackson"
name.find('el')

# Find the substring in the string.
name.find('Jack')

# If cannot find the substring in the string
name.find('Jasdfasdasdf')

#Split the substring into list
name = "Michael Jackson"
split_string = (name.split())
split_string



#RegEx--------------------------------------------------
import re
s1 = "Michael Jackson is the best 123"

# Define the pattern to search for
pattern = r"\d\d\d"

# Use the search() function to search for the pattern in the string
result = re.search(pattern, s1)

# Check if a match was found
if result:
    print("Match found!")
else:
    print("Match not found.")
#################################


import re
pattern = r"\d\d\d\d\d\d\d\d\d\d"  # Matches any ten consecutive digits
text = "My Phone number is 1234567890"
match = re.search(pattern, text)

if match:
    print("Phone number found:", match.group())
else:
    print("No match")
################################
       
import re
pattern = r"\W"  # Matches any non-word character
text = "Hello, world!"
matches = re.findall(pattern, text)

print("Matches:", matches)
#################################

import re
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the findall() function to find all occurrences of the "as" in the string
result = re.findall("as", s2)

# Print out the list of matched words
print(result)
################################

import re
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"

# Use the split function to split the string by the "\s"
split_array = re.split("\s", s2)

# The split_array contains all the substrings, split by whitespace characters
print(split_array) 
##############################


import re
s2 = "Michael Jackson was a singer and known as the 'King of Pop'"

# Define the regular expression pattern to search for
pattern = r"King of Pop"

# Define the replacement string
replacement = "legend"

# Use the sub function to replace the pattern with the replacement string
new_string = re.sub(pattern, replacement, s2, flags=re.IGNORECASE)

# The new_string contains the original string with the pattern replaced by the replacement string
print(new_string) 
#############################





