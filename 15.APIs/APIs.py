#Get Methods¶-------
#get_cell()
#get_city()
#get_dob()
#get_email()
#get_first_name()
#get_full_name()
#get_gender()
#get_id()
#get_id_number()
#get_id_type()
#get_info()
#get_last_name()
#get_login_md5()
#get_login_salt()
#get_login_sha1()
#get_login_sha256()
#get_password()
#get_phone()
#get_picture()
#get_postcode()
#get_registered()
#get_state()
#get_street()
#get_username()
#get_zipcode()

#To start using the API you can install the randomuser library running the pip install command.
!pip install randomuser

#Then, we will load the necessary libraries.
from randomuser import RandomUser
import pandas as pd

#First, we will create a random user object, r.
r = RandomUser()
#Then, using generate_users() function, we get a list of random 10 users.
some_list = r.generate_users(10)
some_list
#to get full name, we call get_full_name()
name = r.get_full_name()
name
#only need 10 users
for user in some_list:
    print (user.get_full_name()," ",user.get_email())
    


    
#EXERCISE1

#generate photos of the random 10 users.
for user in some_list:
    print(user.get_picture())
#To generate a table with information about the users, we can write a function containing all desirable parameters. For example, name, gender, city, etc. The parameters will depend on the requirements of the test to be performed. We call the Get Methods, listed at the beginning of this notebook. Then, we return pandas dataframe with the users.
def get_users():
    users =[]
    for user in RandomUser.generate_users(10):
        users.append({"Name":user.get_full_name(),"Gender":user.get_gender(),"City":user.get_city(),"State":user.get_state(),"Email":user.get_email(), "DOB":user.get_dob(),"Picture":user.get_picture()})
    return pd.DataFrame(users)     

get_users()
#To have a pandas dataframe that can be used for any testing purposes that the tester might have.
df1 = pd.DataFrame(get_users())  
df1



#EXAMPLE2

import requests
import json
#We will obtain the fruityvice API data using requests.get("url") function. The data is in a json format.
data = requests.get("https://fruityvice.com/api/fruit/all")
#We will retrieve results using json.loads() function.
results = json.loads(data.text)
#We will convert our json data into pandas data frame.
pd.DataFrame(results)
#The result is in a nested json format. The 'nutrition' column contains multiple subcolumns, so the data needs to be 'flattened' or normalized.
df2 = pd.json_normalize(results)
df2
#Let's see if we can extract some information from this dataframe. Perhaps, we need to know the family and genus of a cherry.
cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])
#EXERCISE2
#n this Exercise, find out how many calories are contained in a banana.
cal_banana = df2.loc[df2["name"] == 'Banana']
cal_banana.iloc[0]['nutritions.calories']




#EXAMPLE3


#1.Using requests.get("url") function, load the data from the URL.
data2=requests.get("https://official-joke-api.appspot.com/jokes/ten")
#2.Retrieve results using json.loads() function.
results2=json.loads(data2.text)
results2
#3.Convert json data into pandas data frame. Drop the type and id columns.
df3=pd.DataFrame(results2)
df3.drop(columns=["type","id"],inplace=True)
df3


