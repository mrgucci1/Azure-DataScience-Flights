import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_rows', 50)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
# Read in data into dataframe
df_flights = pd.read_csv('flights.csv')
df_flights.head()

#Fill missing values with 0 
df_flights.DepDel15 = df_flights.DepDel15.fillna(0)

#Check we solved the missing values
print(df_flights.isnull().sum())

#Describe the data for every column
print(df_flights.describe())

#Create histogran fir DepDelay and ArrDelay
var_depdel = df_flights['DepDelay']
plt.hist(var_depdel)
plt.title('Distribution of Departure Delay')
plt.xlabel('value')
plt.ylabel('frequency')
plt.show()