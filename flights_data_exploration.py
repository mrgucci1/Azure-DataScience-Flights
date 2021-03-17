import pandas as pd
# Read in data into dataframe
df_flights = pd.read_csv('flights.csv')
df_flights.head()

#Identify missing values
print(df_flights.isnull().sum())

#Fill missing values with 0 
df_flights.DepDel15 = df_flights.DepDel15.fillna(0)

#Check we solved the missing values
print(df_flights.isnull().sum())
