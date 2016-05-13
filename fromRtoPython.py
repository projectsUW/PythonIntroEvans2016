#%%
## BASIC DATA ANALYSIS

#%% Where am I?
import os
os.getcwd()


#%% where should I be?
placeToBe="/Users/JoseManuel/Documents/GITHUBs/PythonIntroEvans2016"
os.chdir(placeToBe)

#%% Getting ready to import data

import pandas as pd

pd.set_option('display.width', 200) # console width

nameFolder ='data'
nameFile='worldIndexes.csv'

# os.path.join will paste both objects. 
# It is just for more order:
fileCSV =os.path.join(nameFolder,nameFile)

# here you have the file as a data frame in Pandas's Style!
indexes=pd.read_csv(fileCSV)

#%% Verify what you have (numbers, category, text):
# float is number, object is text and category is... category!

indexes.dtypes # Like 'str' in R... 

#%% first five rows (you can change number of rows)

indexes.head() # similar to R...(NaN is missing in Python)

#%% summarizing

# summary in Python will not include categories by default
indexes.describe() 


#%% summarizing with categories (I)

# This should summarize categories, if coded as such:

indexes.describe(exclude=['O']) 

#%% summarizing with categories (II)

# Region need to be set as a category:
indexes["Region"]=indexes["Region"].astype('category')

#%% summarizing with categories (III)

indexes.describe(exclude=['O']) #now this works

#%% Frequencies

indexes["Region"].value_counts()

#%% Plotting (I)

# calling packages / modules

#import matplotlib.pyplot as plt

#import matplotlib 
#matplotlib.style.use('ggplot')


#%% First plot...

#plt.figure() # not estrictly needed
indexes.idi2015.plot.hist()
#plt.show()  # not estrictly needed

#%% Second plot...


indexes.plot.hist(alpha=0.5) #alpha for transparency


#%% Cleaning second plot

varsToDrop=['iefRank2015'] # this shouldn't be here....
indexes.drop(varsToDrop,axis=1).plot.hist(alpha=0.5)

#if axis = 0, then drop by row

# second plot still bad
#%% Remeber

# IDI has different range

indexes.describe()

#%% Let's subset:

subSetVars=['idi2015','ief2015','press2015']
subSet=indexes[subSetVars]

#%% and standardize:

subSet_stand = (subSet - subSet.mean()) / subSet.std()

#%% now plot:

subSet_stand.plot.hist(alpha=0.5)

# good but...

#%% maybe box plots are better:

subSet_stand.boxplot()

#%% one by one?

subSet_stand.diff().hist()













