#---------------------------------
# Data preprocessing in python
#---------------------------------
#
# Import pandas
import pandas as pd


#Read csv file using Pandas
dataset = pd.read_csv('loan_small.csv')

# Access the dataframe data using iloc
subset = dataset.iloc[0:3, 1:3]

#Access the data using column names
subsetN = dataset[['Gender', 'ApplicantIncome']][0:3]

#Read TSV file using pandas
datasetT = pd.read_csv('loan_small_tsv.txt', sep='\t')

#Functions of pandas
#head - get a quick view of the dataset
dataset.head(10)

#get the shape of the dataset
dataset.shape

# get the column names of the file
dataset.columns

#Find out the columns with missing values
dataset.isnull().sum(axis=0)

# Data preprocessing by replacing mssing values
# Derop the rows with the missing values
cleandata = dataset.dropna()

cleandata = dataset.dropna(subset=['Loan_Status'])

# copy the dataset
dt = dataset.copy()

# Replace categorical vlaues with mode
cols = ['Gender', 'Area', 'Loan_Status']

dt[cols] = dt[cols].fillna(dt.mode().iloc[0])
dt.isnull().sum(axis=0)

# Replace numerical values with mean
cols2 = ['ApplicantIncome', 'CoapplicantIncome','LoanAmount' ]
dt[cols2] = dt[cols2].fillna(dt.mean())
dt.isnull().sum(axis=0)


# Label Encoding using pandas
dt.dtypes

# Change the datatypes
dt[cols] = dt[cols].astype('category')

for columns in cols:
    dt[columns] = dt[columns].cat.codes


# create dummy  variables or Hot encoding
df2 = dataset.drop(['Loan_ID'], axis=1)
df2 = pd.get_dummies(df2)



