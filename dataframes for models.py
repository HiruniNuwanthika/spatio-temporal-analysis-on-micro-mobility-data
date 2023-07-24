#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point


# In[2]:


map_=gpd.read_file(r'C:\Melbourne_Escooter\RealDataset\shapefiles\CityofMelbourne\COM_TrialArea.shp')


# In[3]:


#count number of start points in each SA in each hour
def countPointsInPolygon():
        df=pd.read_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-0_5.csv')
        df['coords'] = list(zip(df['longitude'],df['latitude']))
        df['coords'] = df['coords'].apply(Point)
        points = gpd.GeoDataFrame(df, geometry='coords', crs=map_.crs)
        pointInPolys = gpd.tools.sjoin(points, map_, op="within", how='left')
        list_SA=[]
        list_numPoints=[]
        for sa in pointInPolys['SA1_CODE21']:
            if(pd.isnull(sa)==False):
                if sa not in list_SA:
                    list_SA.append(sa)
                    pnt_LA = points[pointInPolys.SA1_CODE21==sa]
                    list_numPoints.append(len(pnt_LA))
        #print(list_SA)
        #print(list_numPoints)
        numPoints_df=pd.DataFrame({'SA_code':list_SA, 'numPoints':list_numPoints})
        new_df=numPoints_df.merge(map_, left_on='SA_code',right_on='SA1_CODE21', how='right')
        final_df=new_df[['SA1_CODE21','numPoints','AREASQKM21']]
        final_df['numPoints']=final_df['numPoints'].fillna(0)
        final_df.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\df -models\new\weekday-start-0_5.csv',index=False)


# In[4]:


countPointsInPolygon()


# In[16]:


#count number of start points in each SA in each hour
def countPointsInPolygon(day):
    for hour in range(0,24):
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\{}_{}.csv'.format(day,hour))
        df['coords'] = list(zip(df['longitude'],df['latitude']))
        df['coords'] = df['coords'].apply(Point)
        points = gpd.GeoDataFrame(df, geometry='coords', crs=map_.crs)
        pointInPolys = gpd.tools.sjoin(points, map_, op="within", how='left')
        list_SA=[]
        list_numPoints=[]
        for sa in pointInPolys['SA1_CODE21']:
            if(pd.isnull(sa)==False):
                if sa not in list_SA:
                    list_SA.append(sa)
                    pnt_LA = points[pointInPolys.SA1_CODE21==sa]
                    list_numPoints.append(len(pnt_LA))
        #print(list_SA)
        #print(list_numPoints)
        numPoints_df=pd.DataFrame({'SA_code':list_SA, 'numPoints':list_numPoints})
        new_df=numPoints_df.merge(map_, left_on='SA_code',right_on='SA1_CODE21', how='right')
        final_df=new_df[['SA1_CODE21','numPoints','AREASQKM21']]
        final_df['numPoints']=final_df['numPoints'].fillna(0)
        final_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\counts\{}\{}.csv'.format(day,hour),index=False)


# In[17]:


for day in range (1,31):
    countPointsInPolygon(day)


# In[18]:


# merge hourly start point number to daily -SA wise


# In[51]:


def getDailyTripStartCountinSA(day):
    hour_list=[]
    for i in range(0,24):
        hour=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Hourly\counts\{}\{}.csv'.format(day,i))
        hour_list.append(hour)
    df=pd.concat(hour_list,axis=0)
    count = df.groupby('SA1_CODE21')['numPoints'].sum()  
    count
    count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\startPointCountSAwise_day{}.csv'.format(day))


# In[52]:


for day in range(1,31):
    getDailyTripStartCountinSA(day)


# In[53]:


day1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\startPointCountSAwise_day1.csv')
day2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\startPointCountSAwise_day2.csv')


# In[54]:


df=pd.concat([day1,day2], axis=0)


# In[55]:


df


# In[56]:


count = df.groupby('SA1_CODE21')['numPoints'].sum() 
count


# In[ ]:


# merge daily start point number to monthly -SA wise


# In[63]:


day_list=[]
for day in range(1,31):
    day=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\startPointCountSAwise_day{}.csv'.format(day))
    day_list.append(day)
df=pd.concat(day_list,axis=0)
count = df.groupby('SA1_CODE21')['numPoints'].sum()  
count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Monthly\startPointCountSAwise-oct.csv'.format(day))


# In[64]:


#merge 3 months trip start count-> SA wise


# In[67]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Monthly\startPointCountSAwise-aug.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Monthly\startPointCountSAwise-sep.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Monthly\startPointCountSAwise-oct.csv')
df_final=pd.concat([df1,df2,df3], axis=0)
count = df_final.groupby('SA1_CODE21')['numPoints'].sum()  
count.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\3monthsSAwiseStartCount.csv')


# In[ ]:


#3 months trip start density SA wise


# In[71]:


static_features=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\static features.csv')


# In[74]:


start_count=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\3monthsSAwiseStartCount.csv')


# In[72]:


static_features


# In[75]:


start_count


# In[76]:


featureANDtripCount=static_features.merge(start_count, on='SA1_CODE21')


# In[77]:


featureANDtripCount.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\DF-startcount.csv',index=False)


# In[78]:


featureANDtripCount['tripDensity']=featureANDtripCount['numPoints']/featureANDtripCount['AREASQKM21']


# In[81]:


featureANDtripCount.to_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\DF-startDensity.csv',index=False) #remove area and numPoints


# In[ ]:




