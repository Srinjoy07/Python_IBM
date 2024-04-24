# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set1
#--------------------------------------------------------------------------

# Convert list to set
album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19", "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             
album_set
#-----------------------------------------------------------------------

# Convert list to set
music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul" "progressive rock", "soft rock", "R&B", "disco"])
music_genres
#--------------------------------------------------------------------------

# Sample set
A = set(["Thriller", "Back in Black", "AC/DC"])
A

# Add element to set
A.add("NSYNC")
A

# Try to add duplicate element to the set
A.add("NSYNC")
A

# Remove the element from set
A.remove("NSYNC")
A

# Verify if the element is in the set
"AC/DC" in A
#----------------------------------------------------------------------------

# Sample Sets
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])

# Print two sets
album_set1, album_set2

# Find the intersections
intersection = album_set1 & album_set2
intersection

# Use intersection method to find the intersection of album_list1 and album_list2
album_set1.intersection(album_set2)   

# Find the union of two sets
album_set1.union(album_set2)

# Check if superset
set(album_set1).issuperset(album_set2) #SUPERSET

# Check if subset
set(album_set2).issubset(album_set1)  #SUBSET

#---------------------------------------------------------------------------



#QUIZ ON SET
# Write your code below and press Shift+Enter to execute
set1=set(['rap','house','electronic music', 'rap'])
set1   


# Write your code below and press Shift+Enter to execute
#(my solution)
A = [1, 2, 2, 1]
B = set([1, 2, 2, 1])
if sum(A) == sum(B):
      print("True",sum(A))
else:
       print("False",sum(B))

A = [1, 2, 2, 1]  
B = set([1, 2, 2, 1])
print("the sum of A is:", sum(A))
print("the sum of B is:", sum(B))


# Write your code below and press Shift+Enter to execute
album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
album_set3=album_set1.union(album_set2)
album_set3


# Write your code below and press Shift+Enter to execute
album_set1.issubset(album_set3)