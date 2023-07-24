#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
import glob
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


# In[3]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\dailyTrips'
all_files = glob.glob(path + "/*.csv")


# In[4]:


day_list=[]
num_trips_list=[]
for f in all_files:
    dateWithcsv=f.split('\\')[-1]
    date=dateWithcsv.split('.')[0]
    day_list.append(date)
    df = pd.read_csv(f)
    numTrips=len(df)
    num_trips_list.append(numTrips)
#print(day_list)
#print(num_trips_list)
result_df=pd.DataFrame({'month':10,'date':day_list, 'tripCount':num_trips_list})
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\dailyTrips\total.csv',index=False)


# In[5]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\dailyTrips\total.csv')


# In[69]:


df.replace({'day': {3: 'mon'}},inplace=True)
df.replace({'day': {10: 'mon'}},inplace=True)
df.replace({'day': {17: 'mon'}},inplace=True)
df.replace({'day': {24:'mon'}},inplace=True)

df.replace({'day': {4: 'tue'}},inplace=True)
df.replace({'day': {11: 'tue'}},inplace=True)
df.replace({'day': {18: 'tue'}},inplace=True)
df.replace({'day': {25: 'tue'}},inplace=True)

df.replace({'day': {5: 'wed'}},inplace=True)
df.replace({'day': {12: 'wed'}},inplace=True)
df.replace({'day': {19: 'wed'}},inplace=True)
df.replace({'day': {26: 'wed'}},inplace=True)

df.replace({'day': {6: 'thur'}},inplace=True)
df.replace({'day': {13: 'thur'}},inplace=True)
df.replace({'day': {20: 'thur'}},inplace=True)
df.replace({'day': {27: 'thur'}},inplace=True)

df.replace({'day': {7: 'fri'}},inplace=True)
df.replace({'day': {14: 'fri'}},inplace=True)
df.replace({'day': {21: 'fri'}},inplace=True)
df.replace({'day': {28: 'fri'}},inplace=True)

df.replace({'day': {1: 'sat'}},inplace=True)
df.replace({'day': {8: 'sat'}},inplace=True)
df.replace({'day': {15: 'sat'}},inplace=True)
df.replace({'day': {22: 'sat'}},inplace=True)
df.replace({'day': {29:'sat'}},inplace=True)

df.replace({'day': {2: 'sun'}},inplace=True)
df.replace({'day': {9: 'sun'}},inplace=True)
df.replace({'day': {16:'sun'}},inplace=True)
df.replace({'day': {23: 'sun'}},inplace=True)
df.replace({'day': {30: 'sun'}},inplace=True)
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\dailyTrips\total.csv',index=False)


# In[ ]:


df.replace({'day': {5: 'mon'}},inplace=True)
df.replace({'day': {12: 'mon'}},inplace=True)
df.replace({'day': {19: 'mon'}},inplace=True)
df.replace({'day': {26: 'mon'}},inplace=True)

df.replace({'day': {6: 'tue'}},inplace=True)
df.replace({'day': {13: 'tue'}},inplace=True)
df.replace({'day': {20: 'tue'}},inplace=True)
df.replace({'day': {27: 'tue'}},inplace=True)

df.replace({'day': {7: 'wed'}},inplace=True)
df.replace({'day': {14: 'wed'}},inplace=True)
df.replace({'day': {21: 'wed'}},inplace=True)
df.replace({'day': {28: 'wed'}},inplace=True)

df.replace({'day': {1: 'thur'}},inplace=True)
df.replace({'day': {8: 'thur'}},inplace=True)
df.replace({'day': {15: 'thur'}},inplace=True)
df.replace({'day': {22: 'thur'}},inplace=True)
df.replace({'day': {29: 'thur'}},inplace=True)

df.replace({'day': {2: 'fri'}},inplace=True)
df.replace({'day': {9: 'fri'}},inplace=True)
df.replace({'day': {16: 'fri'}},inplace=True)
df.replace({'day': {23: 'fri'}},inplace=True)
df.replace({'day': {30: 'fri'}},inplace=True)

df.replace({'day': {3: 'sat'}},inplace=True)
df.replace({'day': {10: 'sat'}},inplace=True)
df.replace({'day': {17: 'sat'}},inplace=True)
df.replace({'day': {24: 'sat'}},inplace=True)

df.replace({'day': {4: 'sun'}},inplace=True)
df.replace({'day': {11: 'sun'}},inplace=True)
df.replace({'day': {18: 'sun'}},inplace=True)
df.replace({'day': {25: 'sun'}},inplace=True)


# In[78]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\dailyTrips\total.csv')


# In[79]:


df.replace({'day': {1: 'mon'}},inplace=True)
df.replace({'day': {8: 'mon'}},inplace=True)
df.replace({'day': {15: 'mon'}},inplace=True)
df.replace({'day': {22: 'mon'}},inplace=True)
df.replace({'day': {29: 'mon'}},inplace=True)

df.replace({'day': {2: 'tue'}},inplace=True)
df.replace({'day': {9: 'tue'}},inplace=True)
df.replace({'day': {16: 'tue'}},inplace=True)
df.replace({'day': {23: 'tue'}},inplace=True)
df.replace({'day': {30: 'tue'}},inplace=True)

df.replace({'day': {3: 'wed'}},inplace=True)
df.replace({'day': {10: 'wed'}},inplace=True)
df.replace({'day': {17: 'wed'}},inplace=True)
df.replace({'day': {24: 'wed'}},inplace=True)
df.replace({'day': {31: 'wed'}},inplace=True)

df.replace({'day': {4: 'thur'}},inplace=True)
df.replace({'day': {11: 'thur'}},inplace=True)
df.replace({'day': {18: 'thur'}},inplace=True)
df.replace({'day': {25: 'thur'}},inplace=True)

df.replace({'day': {5: 'fri'}},inplace=True)
df.replace({'day': {12: 'fri'}},inplace=True)
df.replace({'day': {19: 'fri'}},inplace=True)
df.replace({'day': {26: 'fri'}},inplace=True)

df.replace({'day': {6: 'sat'}},inplace=True)
df.replace({'day': {13: 'sat'}},inplace=True)
df.replace({'day': {20: 'sat'}},inplace=True)
df.replace({'day': {27: 'sat'}},inplace=True)

df.replace({'day': {7: 'sun'}},inplace=True)
df.replace({'day': {14: 'sun'}},inplace=True)
df.replace({'day': {21: 'sun'}},inplace=True)
df.replace({'day': {28: 'sun'}},inplace=True)
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\dailyTrips\total.csv',index=False)


# In[92]:


weather_oct=pd.read_csv(r'C:\Melbourne_Escooter\Melbourne-weather\October\Melbourne-rainfall_temp.csv')
trips_oct=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\dailyTrips\total.csv')
oct_=weather_oct.merge(trips_oct, on='date')
oct_.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\oct.csv',index=False)


# In[95]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\aug.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\sep.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\oct.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\all3months.csv',index=False)


# In[98]:


corre=final_df.corr(method='pearson')
final_df


# In[100]:


corre.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\correlation.csv')


# In[1]:


###########for plot


# In[6]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly'
all_files = glob.glob(path + "/*.csv")


# In[7]:


date_list=[]
time_list=[]
num_trips_list=[]
for f in all_files:
    fileName=f.split('\\')[-1]
    date=fileName.split('_')[0]
    date_list.append(date)
    timeWithcsv=fileName.split('_')[1]
    time=timeWithcsv.split('.')[0]
    time_list.append(time)
    df = pd.read_csv(f)
    numTrips=len(df)
    num_trips_list.append(numTrips)
#print(day_list)
#print(num_trips_list)
result_df=pd.DataFrame({'month':10,'date':date_list,'time':time_list ,'tripCount':num_trips_list})
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\TotalCount\total.csv',index=False)

#result_df


# In[8]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\TotalCount\total.csv')


# In[9]:


df.replace({'day': {3: 'mon'}},inplace=True)
df.replace({'day': {10: 'mon'}},inplace=True)
df.replace({'day': {17: 'mon'}},inplace=True)
df.replace({'day': {24:'mon'}},inplace=True)

df.replace({'day': {4: 'tue'}},inplace=True)
df.replace({'day': {11: 'tue'}},inplace=True)
df.replace({'day': {18: 'tue'}},inplace=True)
df.replace({'day': {25: 'tue'}},inplace=True)

df.replace({'day': {5: 'wed'}},inplace=True)
df.replace({'day': {12: 'wed'}},inplace=True)
df.replace({'day': {19: 'wed'}},inplace=True)
df.replace({'day': {26: 'wed'}},inplace=True)

df.replace({'day': {6: 'thur'}},inplace=True)
df.replace({'day': {13: 'thur'}},inplace=True)
df.replace({'day': {20: 'thur'}},inplace=True)
df.replace({'day': {27: 'thur'}},inplace=True)

df.replace({'day': {7: 'fri'}},inplace=True)
df.replace({'day': {14: 'fri'}},inplace=True)
df.replace({'day': {21: 'fri'}},inplace=True)
df.replace({'day': {28: 'fri'}},inplace=True)

df.replace({'day': {1: 'sat'}},inplace=True)
df.replace({'day': {8: 'sat'}},inplace=True)
df.replace({'day': {15: 'sat'}},inplace=True)
df.replace({'day': {22: 'sat'}},inplace=True)
df.replace({'day': {29:'sat'}},inplace=True)

df.replace({'day': {2: 'sun'}},inplace=True)
df.replace({'day': {9: 'sun'}},inplace=True)
df.replace({'day': {16:'sun'}},inplace=True)
df.replace({'day': {23: 'sun'}},inplace=True)
df.replace({'day': {30: 'sun'}},inplace=True)
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\TotalCount\total.csv',index=False)


# In[10]:


df


# In[11]:


result=df.groupby(['day','time'])['tripCount'].sum()
result.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\TotalCount\groupedSum.csv')


# In[12]:


aug=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Hourly\TotalCount\groupedSum.csv')
sep=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Hourly\TotalCount\groupedSum.csv')
octo=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\TotalCount\groupedSum.csv')


# In[13]:


fina_df=pd.concat([aug,sep,octo],axis=1)


# In[14]:


fina_df.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\toGraph.csv',index=False)


# In[101]:


###### plot


# In[15]:


data=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\HourlyTotalPerDay.csv')


# In[16]:


data.columns.values


# In[17]:


a=data.columns.values[-24:]


# In[18]:


data['day']


# In[19]:


data.head()


# In[20]:


import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt

X = data.columns.values[-24:]
Y0 = data.iloc[0,-24:]
Y1 = data.iloc[1,-24:]
Y2 = data.iloc[2,-24:]
Y3 = data.iloc[3,-24:]
Y4 = data.iloc[4,-24:]
Y5 = data.iloc[5,-24:]
Y6 = data.iloc[6,-24:]
#hours=np.zeros(len(Y0))

index = np.arange(len(X))


#ax1.bar(X_axis, Y0, 0.3,label = 'Girls')
#plt.title('Total Trip Counts')

#r1 = ax.bar(index, Y0, bar_width)
#r2 = ax.bar(index+24, Y1, bar_width)
#r3 = ax.bar(index+48, Y2, bar_width)

f, (ax1, ax2,ax3,ax4,ax5,ax6,ax7) = plt.subplots(1, 7,  figsize=(15, 5), sharex='col', sharey='row', gridspec_kw = {'wspace': 0, 'hspace': 0})
ax1.bar(X,Y0,0.4)
ax1.set_xlabel("Monday",labelpad=15)
#x_ticks=['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
x_ticks=['0','','','','4','','','','8','','','','12','','','','16','','','','20','','','23']
ax1.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax2.bar(X,Y1,0.4)
ax2.set_xlabel("Tuesday",labelpad=15)
ax2.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax3.bar(X,Y2,0.4)
ax3.set_xlabel("Wednesday",labelpad=15)
ax3.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax4.bar(X,Y3,0.4)
ax4.set_xlabel("Thursday",labelpad=15)
ax4.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax5.bar(X,Y4,0.4)
ax5.set_xlabel("Friday",labelpad=15)
ax5.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax6.bar(X,Y5,0.4)
ax6.set_xlabel("Saturday",labelpad=15)
ax6.set_xticklabels(x_ticks, rotation=0, fontsize=8)
ax7.bar(X,Y6,0.4)
ax7.set_xlabel("Sunday",labelpad=15)
ax7.set_xticklabels(x_ticks, rotation=0, fontsize=8)

f.supxlabel('Days')
f.supylabel('Total Trip Count')
plt.tight_layout()
plt.show()


# In[9]:


data.loc[data['day'] == 'Monday']


# In[21]:


df=pd.DataFrame({'x':['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23'], 'Monday':[1231,882,625,544,422,448,553,735,1377,1094,1346,1355,1719,1814,1931,2105,1978,2193,1924,1594,1600,1460,1357,1074], 'Tuesday':[893,661,423,278,259,446,715,847,1579,1192,1227,1312,1618,1713,1800,2194,2284,2691,2207,1932,1801,1770,1644,1270], 'Wednesday':[969,768,507,352,326,452,664,852,1595,1161,1237,1434,1741,1838,1951,2346,2592,2682,2533,1910,1711,1799,1859,1339],'Thursday':[1060,788,679,351,286,471,651,859,1430,1207,1179,1460,1773,1951,1978,2421,2639,2765,2471,1914,1802,1956,2051,1618],'Friday':[1271,954,792,526,394,518,696,836,1489,1269,1490,1756,1915,2009,2238,2485,2623,3103,3297,3001,2656,2793,3243,2865],'Saturday':[2362,2006,1437,953,620,414,497,607,890,1378,2041,2500,2885,3189,3329,3610,3631,3732,3755,3569,3138,3504,3734,3339],'Sunday':[2904,2481,1731,1400,800,574,712,768,988,1543,2045,2415,2923,2845,2999,3367,3346,3083,3001,2459,2505,2287,1930,1578]})


# In[43]:


plt.figure(figsize=(10, 6))
plt.plot( 'x', 'Monday', data=df, marker='', color='rosybrown', linewidth=2)
plt.plot( 'x', 'Tuesday', data=df, marker='', color='lightcoral', linewidth=2)
plt.plot( 'x', 'Wednesday', data=df, marker='', color='firebrick', linewidth=2)
plt.plot( 'x', 'Thursday', data=df, marker='', color='saddlebrown', linewidth=2)
plt.plot( 'x', 'Friday', data=df, marker='', color='orangered', linewidth=2)
plt.plot( 'x', 'Saturday', data=df, marker='', color='forestgreen', linewidth=2)
plt.plot( 'x', 'Sunday', data=df, marker='', color='limegreen', linewidth=2)
#plt.plot( 'x_values', 'weekday_stop', data=df, marker='', color='red', linewidth=2)
#plt.plot( 'x_values', 'weekend_start', data=df, marker='', color='green', linewidth=2, linestyle='dashed')
#plt.plot( 'x_values', 'weekend_stop', data=df, marker='', color='red', linewidth=2, linestyle='dashed')


#plt.title('Number of Trip starts')
plt.xlabel("Time of the day", fontsize=16)
plt.ylabel("Trip count", fontsize=16)
plt.yticks(ha='right', fontsize=14)
plt.xticks(ha='right', fontsize=12)

plt.legend(loc=(1.05, 0.2),fontsize=15, title_fontsize=25)
#plt.legend(fontsize=10, title_fontsize=25)
plt.tight_layout()

plt.show()


# In[ ]:





# In[ ]:




