
# coding: utf-8

# # Analytics in Practice
# 
# # Data Wrangling - Assignment 1 
# - By Srushti Padade

# # Summary
# 
# The libraries such as Pandas, Json, Pandas_profiling in Python plays an important role in data wrangling process of preprocessing. We also have libraries like dplyr, ISLR, etc in R language. Any real time data have various constraints, such as the data inconsistaency, missing values, duplicacy, or major issue with reading the data due to its format.
# Thus, just loading the data does not necessarily help with descriptive statistics of the data, but some time it takes more extraction by manipulation, as we have done it with the json file. Cleaning of data is must to gain the information it store. Therefore, applying the statistics measures we can gain an insight of the data to build a model and further help with Machine learning.
# 
# Here while dealing with the 3 different data set of varied format we have learnt the techniques to read these files and summaries the data they have.The data can be of different datatype which can create a difficulty in manipulating them, but there are methods to be used to change and manipulate the data. We have also learnt the drawback of an raw data and also the cleaning techniques of them. Extracting the possible information also could be gathered for a better data visualization.
# 

# In[1]:


# The below libraries are imported for the data wrangling purpose. 
# Pandas is the renoumced library in python that helps with multiplefunctionalities.
# Similarly, Json libaray is used to manipulate the data from .json file format.


# In[2]:


import pandas as pd
import json

#Reading the .csv data file
Companies_Data = pd.read_csv('us_companies.csv')
Agencies_Data = pd.read_csv('us_agencies.csv')

# Computes the size and dimension of the data.
CSize = Companies_Data.size
ASize = Agencies_Data.size

CShape = Companies_Data.shape
AShape = Agencies_Data.shape


# In[3]:


print("The Size of Company Data is :", CSize)

print("The Size of Agencies Data is :", ASize)

print("The Dimensions of Company Data is :", CShape)

print("The Dimensions of Agencies Data is :", AShape)


# In[4]:


# To get all the Variables of the data set.
Companies_Data.columns


# In[5]:


Agencies_Data.columns


# # Question 1: Are there any missing columns?
# 
# By looking at the Data columns we cannot determine the missing columns unless we have a DOMAIN knowldge about the data.
# But simply looking the columns there do not seems to be any missing columns.

# In[6]:


# To know the data type of each variable.
Agencies_Data.dtypes


# In[7]:


Companies_Data.dtypes


# # Question 2: Are there any missing column names or errors in the column names? If so, name those columns.
# 
# All the Columns are named in both the dataset. 
# The column used_by_fte does look like a column that could have a better name.

# In[8]:


# The Null values in each column can be computed as below.
Agencies_Data.isnull().sum()


# In[9]:


Companies_Data.isnull().sum()


# In[10]:


# Here we have the total NULL values from the data set.
Agencies_Data.isnull().sum().sum()


# In[11]:


Companies_Data.isnull().sum().sum()


# # Question 3: Are there any values in the columns missing?
# 
# There are many missing values in the dataset.
# Above is the detail view of ll the missing values column wise and total missing values for Agencies data is 2718, whereas for companies data is 2316.

# In[12]:


# To have a descriptive statistics or summary of the data below command is helpful.
Companies_Data.describe(include = 'all')


# In[13]:


Agencies_Data.describe(include = 'all')


# # Question 4: How is data organized in each column? Is it properly organized?
# 
# The summary statistics of the data have a good picture how the data is organised.
# 
# For Agencies the data is a catagorical value and hence the distribution cannot be obtained.
# However, for Companies data the distribution is available.
# 
# The data organised is well manner in the columns but due to missing values it is difficult to extract the ditribution of the data. Also the data_impact column is not organized as it contains a empty lists in it.

# # Question 5: Is data in the proper shape for further analysis? If not, why? Explain.
# 
# The data are not in the proper shape for further analysis.
# - There are lots of missing values in the dataset(73%).
# - There is also redandancy in the data.
# - The is made complexed by direct storage of the list values in column like data_impact.
# - Few columns are having highly corelated data which might affect the training later. 

# In[30]:


# Cleaning the dataset.
Clean_Companies = Companies_Data.dropna(axis='columns')

Clean_Companies.head()


# In[31]:


Clean_Agencies = Agencies_Data.dropna()

Clean_Agencies.head()


# # Question 6: How will you fix this dataset? Describe the methods you will use to fix this dataset for further analysis?
# 
# The Data set could be cleaned using below measures:
# - Remove the missing values from the column.
# - The columns could be droped with very few data entries.
# - The redanduncy can be eliminated be removing corelated columns. (Remove duplicated)
# - The columns with the list values can be extracted to generate new columns for cleaner visibility.

# # Question 7: How are the two datasets linked to each other? Is there a common “primary key” to connect the two datasets?
# 
# The two dataset are linked to each other using the company name: 
# Comapnies_Data:company_name = Agencies_Data:used_by. 

# In[16]:


# Loading the .json file in the environment.


# In[17]:


with open('ChicagoTraffic.json') as f:
    data = json.load(f)


# In[18]:


# Here the json file is stored with 2 key roots - MetaData and Data we have to extract the data individually.
DataEntries = pd.Series(data["data"])

MetaData = pd.Series(data["meta"]["view"]["columns"])


# In[19]:


# Here we can see all the summary of each column from the data by manipulating the Metadata.
pd.DataFrame.from_dict(MetaData.to_dict())


# In[20]:


# The below librar provides a better view of the data with respect to its descriptive statistics.

#Installation
#conda install -c conda-forge pandas-profiling

#import pandas_profiling
#from pandas_profiling import ProfileReport

#profile = ProfileReport(Companies_data)
#profile

#This libarary gives a clearer picture of the data with all its distribution like: 
#Percentage missing value, catagorical data, distribution of the data, etc.


# # Question 1: How many variables are in the dataset?
# 
# There are 23 variables in the data set.

# In[21]:


pd.DataFrame.from_dict(MetaData.to_dict()).index


# # Question 2: Name all the variables?
# 
# Above are the names of all the variables from the dataset.

# In[22]:


# To know the traffic of the streets we have stored he street names as a list for computation.
Traffic = list()

Street = ["100th St", "101 St", "102 St", "103rd St", "104th St", "105th St", "106th St", "107th St", "108th St",
       "109th St", "110th St", "111th St", "112th St", "113th St", "114th St", "115th St"]


# In[23]:


#The below loop iterates over the Data entries and retrieve the Traffic count of each street.


# In[24]:


for item in DataEntries:
    if item[10] in Street:
        temp = int(item[12])
        Traffic.append(temp)


# # Question 3: What is the total traffic of vehicles on 100th street to 115th street?
# 
# The traffic count is computed below.

# In[25]:


#The totl traffic is the sum of all the individual traffic.
print("The Total traffic between street 100th to 115 is", sum(Traffic))


# In[26]:


#Similarly, for the Coordinates of the location we can reterive the traffic count.
Coordinates = list()


# In[27]:


for item in DataEntries:
    if item[14] == "41.66836" and item[15] == "-87.620176":
        temp = int(item[12])
    elif item[14] == "41.651861" and item[15] == "-87.54501":
        temp1 = int(item[12])
        


# # Question 4: What is the total traffic of vehicles on geolocations, (41.651861, -87.54501) and (41.66836, -87.620176)
# 
# The total traffic for the given geographic location is computed below.

# In[28]:


print("Total traffic with at Latitute = 41.66836 and longitude = -87.620176 is", temp)

print("Total traffic with at Latitute = 41.651861 and longitude = -87.54501 is", temp1)

print("Total traffic at the given coordinates will be", temp+temp1)

