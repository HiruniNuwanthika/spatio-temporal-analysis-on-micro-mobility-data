#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt


# In[13]:


df=pd.read_csv(r'C:\SA similarity\TripStops\3-months SA wise\20604150301.csv')


# In[14]:


df


# In[15]:


trip_weather=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\hourlyTripStopsWeather_timeFrames.csv')


# In[16]:


trip_weather


# In[17]:


dffinal = pd.merge(trip_weather, df,  how='left', left_on=['MM','DD', 'HH24'], right_on = ['month','day','hour'])
dffinal.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\20604150301.csv',index=False)
# remove month, date, time, trip count adn other columns manually


# In[ ]:




