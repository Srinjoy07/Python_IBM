#INTRODUCTIOn to PANDAS----------------------------------------------------------------------------------------------
# Dependency needed to install file 

# If running the notebook on your machine, else leave it commented
#!pip install xlrd

#!pip install openpyxl 
import piplite
await piplite.install(['xlrd','openpyxl'])

# Import required library
import pandas as pd
############################################################################################################################3


# Read data from CSV file--------------------------------------------------------------------------------------------------------
# csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
# df = pd.read_csv(csv_path)

from pyodide.http import pyfetch
import pandas as pd
filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "TopSellingAlbums.csv")
df = pd.read_csv("TopSellingAlbums.csv")

#for LOCAL MACHINE USAGE---------------------------------------------------------------------------------------
#filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
#df = pd.read_csv(filename)
#---------------------------------------------------------------------------------------------------

# Print first five rows of the dataframe
df.head()

# Read data from Excel File and print the first five rows
xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
await download(xlsx_path, "TopSellingAlbums.xlsx")
df = pd.read_excel("TopSellingAlbums.xlsx")
df.head()

#for LOCAL MACHINE USAGE--------------------------------------------------------------------------------------
#xlsx_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx'
#df = pd.read_excel(xlsx_path)
#df.head()

# Access to the column Length
x = df[['Length']]
x
###########################################################################################################################333


#Viewing Data and Accessing Data------------------------------------------------------------------------------------------
# Get the column as a series
x = df['Length']
x

# Get the column as a dataframe
x = df[['Artist']]
type(x)

# Access to multiple columns
y = df[['Artist','Length','Genre']]
y

# Access the value on the first row and the first column
df.iloc[0, 0]

# Access the value on the second row and the first column
df.iloc[1,0]

# Access the value on the first row and the third column
df.iloc[0,2]

# Access the value on the second row and the third column
df.iloc[1,2]

# Access the column using the name
df.loc[0, 'Artist']

# Access the column using the name
df.loc[1, 'Artist']

# Access the column using the name
df.loc[0, 'Released']

# Access the column using the name
df.loc[1, 'Released']

# Slicing the dataframe
df.iloc[0:2, 0:3]

# Slicing the dataframe using name
df.loc[0:2, 'Artist':'Released']
############################################################################################################################

#Quiz on DataFrame---------------------------------------------------------------------------------------------------------

#Use a variable q to store the column Rating as a dataframe
q=df['Rating']
q

#Assign the variable q to the dataframe that is made up of the column Released and Artist:
q=df[['Released','Artist']]
q

#Access the 2nd row and the 3rd column of df:
df.iloc[1,2]

#Use the following list to convert the dataframe index df to characters and assign it to df_new; find the element corresponding to the row index a and column 'Artist'. Then select the rows a through d for the column 'Artist'
new_index=['a','b','c','d','e','f','g','h']
df_new=df   
df_new.index=new_index
#df_new.loc['a','Artist']   #prints the first index--
df_new.loc['a':'d', 'Artist']
