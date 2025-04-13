# Data Processing in Python - Train-Test Split

# Import pandas
import pandas as pd
# Read CSV file using Pandas
dataset = pd.read_csv('loan_small.csv')


# Drop the rows with the missing values from 
# a particular columns where loan_status has missing values
cleandata = dataset.dropna(subset=['Loan_Status'])

# copy the dataset
df = cleandata.copy()

# Replace categorical values with mode
cols = ['Gender','Area','Loan_Status']
df[cols] = df[cols].fillna(df.mode().iloc[0])
df.isnull().sum(axis=0)

#Replace numerical values with mean
cols2 = ['ApplicantIncome','CoapplicantIncome','LoanAmount']
df[cols2] = df[cols2].fillna(df.mean)
df.isnull().sum(axis=0)

# Drop Irrelevant columns
df = df.drop(['Loan_ID'], axis=1)

# Create Dummy variables or Hot Encoding
df = pd.get_dummies(df, drop_first=True)


# Split the data vertically into X and Y

X = df.iloc[:, :-1] #Select all the columns except loan_status
Y = df.iloc[:, -1] #Select only the loan_status

# Split the dataset by rows

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=1234)
