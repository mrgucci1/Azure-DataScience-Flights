import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from scipy import stats
import matplotlib.ticker as ticker
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

#Get Stats on Depparture delay
var = df_flights['DepDelay']
print("Departure delay stats")
min_val = var.min()
max_val = var.max()
mean_val = var.mean()
med_val = var.median()
mod_val = var.mode()[0]
print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                        mean_val,
                                                                                        med_val,
                                                                                        mod_val,
                                                                                        max_val))
#Get Stats on arrival delay
var = df_flights['ArrDelay']
print("Arrival delay stats")
min_val = var.min()
max_val = var.max()
mean_val = var.mean()
med_val = var.median()
mod_val = var.mode()[0]
print('Minimum:{:.2f}\nMean:{:.2f}\nMedian:{:.2f}\nMode:{:.2f}\nMaximum:{:.2f}\n'.format(min_val,
                                                                                        mean_val,
                                                                                        med_val,
                                                                                        mod_val,
                                                                                        max_val))
																						
																						
#Create histogran for DepDelay and ArrDelay
# Create a Figure
fig = plt.figure(figsize=(10,4))
q_hi = df_flights['DepDelay'].quantile(0.95)
q_low = df_flights['DepDelay'].quantile(0.05)
#filter dataframe so we are excluding the highest 5% and lowest 5% of the data
var_depdel = df_flights[(df_flights['DepDelay']<q_hi)&(df_flights['DepDelay'] > q_low)]['DepDelay']
plt.hist(var_depdel, 150)
plt.title('Distribution of Departure Delay')
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# Add lines for the statistics
#plt.axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
plt.axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
plt.axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
plt.axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
#plt.axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)
plt.show()
# Create a Figure
fig = plt.figure(figsize=(10,4))
q_hi = df_flights['ArrDelay'].quantile(0.95)
q_low = df_flights['ArrDelay'].quantile(0.05)
#filter dataframe so we are excluding the highest 5% and lowest 5% of the data
var_depdel = df_flights[(df_flights['ArrDelay']<q_hi)&(df_flights['ArrDelay'] > q_low)]['ArrDelay']
plt.hist(var_depdel, 150)
plt.title('Distribution of Arrival Delay')
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
# Add lines for the statistics
#plt.axvline(x=min_val, color = 'gray', linestyle='dashed', linewidth = 2)
plt.axvline(x=mean_val, color = 'cyan', linestyle='dashed', linewidth = 2)
plt.axvline(x=med_val, color = 'red', linestyle='dashed', linewidth = 2)
plt.axvline(x=mod_val, color = 'yellow', linestyle='dashed', linewidth = 2)
#plt.axvline(x=max_val, color = 'gray', linestyle='dashed', linewidth = 2)
plt.show()