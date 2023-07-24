#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd


# In[4]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\df -models\avgTripDensity350SA.csv')


# In[8]:


df['SA1_CODE21'] = df['SA1_CODE21'].astype(str)


# In[9]:


map_=gpd.read_file(r'C:\Melbourne_Escooter\RealDataset\shapefiles\CityofMelbourne\COM_TrialArea.shp')


# In[9]:


mapDF=map_.merge(df, on='SA1_CODE21', how="left")


# In[11]:


mapDF.to_file(filename = "C:\Melbourne_Escooter\RealDataset\shapefiles\TripDensity350SA3Months.shp", driver = "ESRI Shapefile")


# In[14]:


new=map_[map_['SA1_CODE21']=='20604150520']
new


# In[ ]:




