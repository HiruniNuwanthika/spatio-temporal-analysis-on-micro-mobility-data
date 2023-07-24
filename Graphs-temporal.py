#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:



score=[0.232,0.120,0.119,0.109,0.094,0.087,0.074,0.059,0.050,0.020,0.010,0.007,0.006,0.006]
feature=['humidity','saturday','avg_temp','time_19_23','avg_wind_speed', 'time_16_18','time_6_10','sunday','time_11_15','precipitation','monday','tuesday','thursday','wednesday']
  
fig = plt.figure(figsize = (10,5))
clr=['#E61E2A','gray','#000054','gray','#000054','gray','gray','gray','gray','#E61E2A','gray','gray','gray','gray']
# creating the bar plot
plt.barh(feature, score,color=clr)
 
plt.xlabel("Importance",fontsize=10)
plt.ylabel("Feature",fontsize=10)
#plt.title("RFR: Feature importance")
plt.yticks(feature, feature,  ha='right', fontsize=9)
plt.gca().invert_yaxis()
plt.show()

#Blue-#000054      Red-#E61E2A


# In[3]:



score=[0.258,0.014,0.05,0.311,0.032,0.128,0.011,0.084,0.015,0.031,0.0051,0.020,0.0124,0.0192]
feature=['humidity','saturday','time_19_23','avg_temp','time_16_18','avg_wind_speed','time_6_10','time_11_15','sunday','precipitation','monday','tuesday','wednesday','thursday']
  
fig = plt.figure(figsize = (10, 5))
clr=['r','gray','gray','b','gray','b','gray','gray','gray','r','gray','gray','gray','gray']
# creating the bar plot
plt.barh(feature, score)
 
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: Feature importance -office SA")
plt.yticks(feature, feature,  ha='right', fontsize=14)
plt.gca().invert_yaxis()
plt.show()


# In[4]:



score=[0.115,0.058,0.264,0.1126,0.0308,0.074,0.2523,0.0057,0.0419,0.009,0.0061,0.0021,0.023,0.0013]
feature=['humidity','saturday','time_19_23','avg_temp','time_16_18','avg_wind_speed','time_6_10','time_11_15','sunday','precipitation','monday','tuesday','wednesday','thursday']
  
fig = plt.figure(figsize = (10, 5))
clr=['r','gray','gray','b','gray','b','gray','gray','gray','r','gray','gray','gray','gray']
# creating the bar plot
plt.barh(feature, score)
 
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: Feature importance - cafe SA")
plt.yticks(feature, feature,  ha='right', fontsize=14)
plt.gca().invert_yaxis()
plt.show()


# In[5]:



score=[0.195,0.0913,0.097,0.336,0.0179,0.1773,0.003,0.0105,0.039,0.0086,0.0038,0.0099,0.0038,0.0040]
feature=['humidity','saturday','time_19_23','avg_temp','time_16_18','avg_wind_speed','time_6_10','time_11_15','sunday','precipitation','monday','tuesday','wednesday','thursday']
  
fig = plt.figure(figsize = (10, 5))
clr=['r','gray','gray','b','gray','b','gray','gray','gray','r','gray','gray','gray','gray']
# creating the bar plot
plt.barh(feature, score)
 
#plt.xlabel("Importance",fontsize=15)
#plt.ylabel("Feature",fontsize=15)
#plt.title("RFR: Feature importance - garden SA")
plt.yticks(feature, feature,  ha='right', fontsize=14)
plt.gca().invert_yaxis()
plt.show()


# In[10]:


###### weather graphs


# In[4]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\hourlyTripWeather_timeFrames.csv')


# In[21]:


df


# In[15]:


df1=df[df['day']=='mon']
df1


# In[5]:


df['mm-dd-tt']=df['MM'].astype(str) +'_'+ df['DD'].astype(str) +'_' +df['HH24'].astype(str)


# In[6]:


df


# In[7]:


x=df['mm-dd-tt']
y=df['tripCount']
df=pd.DataFrame({'x':x,'y':y})


# In[11]:


fig = plt.figure(figsize=(18, 18))
plt.plot( 'x', 'y', data=df, marker='', color='green', linewidth=2)


# In[ ]:




