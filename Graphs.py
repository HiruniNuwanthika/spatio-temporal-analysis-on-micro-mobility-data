#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\graph results.csv')


# In[8]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\DF-startDensity.csv')
corrr=df.corr()
corrr.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\corr.csv')


# In[4]:


df1=df[df['time']=='overall']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
#fig = plt.figure(figsize = (12, 6))
#cr = ['#000054','#E61E2A','#E61E2A','#000054','#000054','#E61E2A','#E61E2A','#000054','#E61E2A','#E61E2A','#E61E2A','#000054','#000054','#E61E2A','#000054','#E61E2A','#000054','#E61E2A','#000054','#000054','#E61E2A','#000054']
cr = ['#E61E2A','#000054','#000054','#E61E2A','#000054','#E61E2A','#000054','#E61E2A','#000054','#000054','#E61E2A','#000054']
# creating the bar plot
plt.barh(feature, score,color=cr)
 
plt.xlabel("Importance", fontsize=12)
plt.ylabel("Feature",fontsize=12)
#plt.title("RFR: Total Trip")
plt.yticks(feature, feature,  ha='right', fontsize=10)

plt.show()
#Blue-#000054      Red-#E61E2A


# In[21]:


import matplotlib.pyplot as plt

plt.figure(figsize=(12,9))
feature = ['Population Density', 'Car Ownership%', 'without Children %', 'Age 30-39%',  'Office%', 'Male% ', 'Age 5-14%', 'Tram Density', 'Female %','MXI','Cafe%', 'Age 65Above%', 'Entropy', 'With Children%','Bus Density','Age 40-49%','Age 50-64%','Age 15-29%','Shop%','Campus Count','Recreation Count','Train Density']
score = [0.273,0.256,0.112,0.083,0.080, 0.050,0.041,0.020,0.012,0.012,0.011,0.009,0.009,0.009,0.005,0.004,0.003,0.003,0.001,0.000,0.000,0.000]
clr=['#000054','#E61E2A','#000054','#000054','#E61E2A','#000054','#E61E2A','#000054','#E61E2A','#000054','#000054','#E61E2A','#E61E2A','#E61E2A','#000054','#E61E2A','#E61E2A','#000054','#000054']
plt.barh(feature, score,color=clr)

plt.gca().invert_yaxis()
plt.xlabel("Importance",fontsize=15)
plt.ylabel("Feature",fontsize=15)

plt.yticks(feature, feature,  ha='right', fontsize=14)


plt.show()


# In[2]:


import matplotlib.pyplot as plt
   
feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.331,0.183,0.124,0.0571,0.0816,0.0669,0.0266,0.0322,0.0084,0.0252,0.0101,0.0056]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[3]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.2205,0.2372,0.0617,0.0922,0.0741,0.0565,0.0848,0.0598,0.0100,0.0109,0.0214,0.0403]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[4]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.2288,0.1118,0.1002,0.0120,0.0834,0.0283,0.0123,0.0603,0.0062,0.1297,0.0870,0.0050]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday 0-5)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[5]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.1666,0.1673,0.0740,0.0306,0.0531,0.0211,0.0874,0.1203,0.0047,0.0547,0.0697,0.0050]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend 0-5)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[6]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.2356,0.0518,0.0585,0.0246,0.1465,0.1042,0.0130,0.0792,0.0078,0.0653,0.0518,0.0390]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday 6-10)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[7]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.1076,0.0633,0.0314,0.0432,0.0846,0.1341,0.0100,0.2287,0.0190,0.0183,0.0099,0.1902]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend 6-10)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[8]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.0818,0.5345,0.1052,0.0595,0.0410,0.0679,0.0347,0.0254,0.0111,0.0034,0.0133,0.0079]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday 11-15)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[9]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.1061,0.3447,0.1250,0.0738,0.0627,0.0271,0.0189,0.0758,0.0093,0.0130,0.0909,0.0502]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend 11-15)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[10]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.1597,0.3101,0.0767,0.0770,0.0764,0.0819,0.0262,0.0750,0.0043,0.0139,0.0244,0.0196]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday 16-18)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[11]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.0625,0.1902,0.0310,0.0759,0.0560,0.1331,0.0891,0.0854,0.0047,0.0344,0.0879,0.0431]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend 16-18)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[12]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.2650,0.2669,0.0856,0.0264,0.0675,0.0245,0.0632,0.0705,0.0177,0.0359,0.0270,0.0019]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekday 19-23)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[13]:


feature = ['Population density', 'Car owner %', 'Couples without children %', '30-39%', 'Office%','male%', '5-14%', 'Tram density',' Female%', 'MXI', 'Cafe%', 'Above 65%']
score = [0.1959,0.1906,0.0616,0.1131,0.0810,0.0425,0.1222,0.0701,0.0058,0.0135,0.0481,0.0295]
clr=['b','r','b','b','r','b','r','b','r','b','b','r']
plt.barh(feature, score)

plt.gca().invert_yaxis()
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: top 12 features (weekend 19-23)")
plt.yticks(feature, feature,  ha='right', fontsize=14)

plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[14]:


df1=df[df['time']=='weekday']
#df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday)")
plt.gca().invert_yaxis()
plt.show()


# In[34]:


df1=df[df['time']=='weekend']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend)")
plt.show()


# In[18]:


df1=df[df['time']=='t1']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (0:00-5:59)")
plt.show()


# In[24]:


df1=df[df['time']=='t2']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (6:00-10:59)")
plt.show()


# In[25]:


df1=df[df['time']=='t3']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (11:00-15:59)")
plt.show()


# In[26]:


df1=df[df['time']=='t4']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (16:00-18:59)")
plt.show()


# In[28]:


df1=df[df['time']=='t5']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (19:00-23:59)")
plt.show()


# In[40]:


df1=df[df['time']=='weekday 0_5']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday 0:00-5:59)")
plt.show()


# In[41]:


df1=df[df['time']=='weekday 6_10']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday 6:00-10:59)")
plt.show()


# In[42]:


df1=df[df['time']=='weekday 11_15']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday 11:00-15:59)")
plt.show()


# In[43]:


df1=df[df['time']=='weekday 16_18']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday 16:00-18:59)")
plt.show()


# In[44]:


df1=df[df['time']=='weekday 19_23']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekday 19:00-23:59)")
plt.show()


# In[46]:


df1=df[df['time']=='weekend 0_5']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend 0:00-5:59)")
plt.show()


# In[47]:


df1=df[df['time']=='weekend 6_10']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend 6:00-10:59)")
plt.show()


# In[48]:


df1=df[df['time']=='weekend 11_15']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend 11:00-15:59)")
plt.show()


# In[49]:


df1=df[df['time']=='weekend 16_18']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend 16:00-18:59)")
plt.show()


# In[50]:


df1=df[df['time']=='weekend 19_23']
df1.sort_values('importance',inplace=True)
score=df1['importance']
feature=df1['feature']
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.barh(feature, score)
 
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("RFR: top 10 features (weekend 19:00-23:59)")
plt.show()


# In[ ]:





# In[ ]:


#corrrelation graph


# In[54]:


import seaborn as sns

df= pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-11_15.csv')
sns.scatterplot(x="total_trip_density", y="car owner %", data=df)


# In[60]:


df= pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-19_23.csv')
sns.scatterplot(x="total_trip_density", y="car owner %", data=df)


# In[57]:


df= pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-19_23.csv')
sns.scatterplot(x="total_trip_density", y="car owner %", data=df)


# In[ ]:


# trip weekend weekday summary


# In[63]:


import pandas as pd
import matplotlib.pyplot as plt
  

df = pd.DataFrame({
    'Time of the day': ['0:00-5:59', '6:00-10:59', '11:00-15:59', '16:00-18:59','19:00-23:59'],
    'Weekday': [194.42],
    'Weekend': [430.7,278.3,706.4,473.4,694.3]
})


df.plot(x="Time of the day", y=["Weekday", "Weekend"], kind="bar", title="Avg. trip count per day")


# In[4]:


import numpy as np
import matplotlib.pyplot as plt
  
N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [194.42,240.74,452.92,342.08,457.02]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [225.48,242.62,459.38,338.92,462.12]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [406.23,255.77,706.42,473.38,694.46]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [458.23,260.04,691.81,488.50,717.54]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=800) #ymax is your value
plt.ylim(bottom=100) #ymin is your value
 
plt.xlabel("Time of day")
plt.ylabel('number of trips per day')
plt.title("Average trip starts/stops per day")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[ ]:




