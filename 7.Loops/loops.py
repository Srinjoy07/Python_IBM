#Range------------------------------------------------------------------------------
# Use the range
range(3)

#for------------------------------------------------------------------------------------
# For loop example
dates = [1982,1980,1973]
#N = len(dates)
for i in range(3):
    print(dates[i])
    
# Example of for loop
for i in range(0, 8):
    print(i)     
    
# Exmaple of for loop, loop through list
for year in dates:  
    print(year) 
    
# Use for loop to change the elements in list
squares = ['red', 'yellow', 'green', 'purple', 'blue']
for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])  
    
# Loop through the list and iterate on both index and element value
squares=['red', 'yellow', 'green', 'purple', 'blue']
for i, square in enumerate(squares):
    print(i, square)
    


#WHILE loop--------------------------------------------------------------------------------------
count = 1
while count <= 5:
    print(count)
    count +=1
    
# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]
while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]
    
print("It took ", i ,"repetitions to get out of loop.")



#Practise Exercise on Loops-----------------------------------------------------------------------
# Write your code below and press Shift+Enter to execute
for i in range(-4,5):
    print(i)
    
# Write your code below and press Shift+Enter to execute
Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
for genre in Genres:
    print(genre)
    
# Write your code below and press Shift+Enter to execute
squares=['red', 'yellow', 'green', 'purple', 'blue']
N=len(squares)
for i in range(N):
    print(squares[i]) 
    
# Write your code below and press Shift+Enter to execute
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 0
rating = PlayListRatings[0]
while(i < len(PlayListRatings) and rating >= 6):
    print(rating)
    i = i + 1 
    rating = PlayListRatings[i] 
    
# Write your code below and press Shift+Enter to execute
squares = ['orange', 'orange', 'purple', 'blue ', 'orange']
i=0
new_squares = squares[0]
while(new_squares=="orange"):
    print(new_squares)
    i+=1
    new_squares=squares[i]
    



#Some real life example-------------------------------------------------------------------------------------
# Write table of 6 and 7 to help brotha
print("Table of 6----")
for i in range(1,10):
    print("6*",i,"=",i*6)
    i+=1

print("Table of 7----")
for i in range(1,10):
    print("7*",i,"=",i*7)
    i+=1
    

# Write your code here
Animals = ["lion", "giraffe", "gorilla", "parrots", "crocodile","deer", "swan"]
#New=[]
i=0
while i<len(Animals) :
    if len(Animals[i]) == 7:
        print(Animals[i])
        #New.append(Animals[i])
    i+=1
#print(New)                    //to help brother select animals with 7 digit to write essay on