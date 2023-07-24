#!/usr/bin/env python
# coding: utf-8

# In[1]:


import geopandas as gpd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from shapely.geometry import Point


# In[ ]:


####### Spatial ###############


# In[ ]:


# global spatial model - Trip density dataset + static features = entire spatial


# In[2]:


map_=gpd.read_file(r'C:\Melbourne_Escooter\RealDataset\shapefiles\CityofMelbourne\COM_TrialArea.shp')


# In[11]:


#count number of start points in each SA in each hour
def countPointsInPolygon(day):
    for hour in range(0,24):
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\{}_{}.csv'.format(day,hour))
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
        final_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\{}\{}.csv'.format(day,hour),index=False)


# In[12]:


for day in range (1,31):
    countPointsInPolygon(day)


# In[22]:


def getDailyTripStartCountinSA(day):
    hour_list=[]
    for i in range(0,24):
        hour=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\{}\{}.csv'.format(day,i))
        hour_list.append(hour)
    df=pd.concat(hour_list,axis=0)
    count = df.groupby('SA1_CODE21')['numPoints'].sum()  
    count
    count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\startPointCountSAwise_day{}.csv'.format(day))


# In[23]:


for day in range(1,31):
    getDailyTripStartCountinSA(day)


# In[26]:


day_list=[]
for day in range(1,31):
    day=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\startPointCountSAwise_day{}.csv'.format(day))
    day_list.append(day)
df=pd.concat(day_list,axis=0)
count = df.groupby('SA1_CODE21')['numPoints'].sum()  
count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Monthly\startPointCountSAwise-oct.csv'.format(day))


# In[28]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Monthly\startPointCountSAwise-aug.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Monthly\startPointCountSAwise-sep.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Monthly\startPointCountSAwise-oct.csv')
df_final=pd.concat([df1,df2,df3], axis=0)
count = df_final.groupby('SA1_CODE21')['numPoints'].sum()  
count.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\3monthsSAwiseSopCount.csv')


# In[ ]:





# In[29]:


static_features=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\static features.csv')


# In[31]:


stop_count=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\3monthsSAwiseSopCount.csv')


# In[34]:


featureANDtripCount=static_features.merge(stop_count, on='SA1_CODE21')


# In[35]:


featureANDtripCount.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\DF-stopcount.csv',index=False)


# In[36]:


featureANDtripCount['tripDensity']=featureANDtripCount['numPoints']/featureANDtripCount['AREASQKM21']


# In[37]:


featureANDtripCount.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\DF-stopDensity.csv',index=False) #remove area and numPoints


# In[1]:


# spatial dataset into separate time frames


# In[1]:


import os
import glob
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import ckwrap


# In[35]:


def createDailyTripCountFile(day):
    df_list=[]
    for hour in range(0,24):
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\{}\{}.csv'.format(day,hour))
        #df=df[df['SA1_CODE21'].isin(list_35SA)]
        #new_df=df[['SA1_CODE21','AREASQKM21','numPoints']]
        df['date']=day
        df['hour']=hour
        #new_df['tripDensity']=new_df['NUMPOINTS']/new_df['AREASQKM21']
        df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\{}_{}.csv'.format(day,hour), index=False)
        df_list.append(df)
    df_1=pd.concat(df_list,axis=0)
    df_1.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\\Hourly\count\with date\{}.csv'.format(day),index=False)


# In[36]:


for i in range(1,31):
    createDailyTripCountFile(i)


# In[37]:


def createTripCountMonth():
    day_list=[]
    for day in range(1, 31):
        day=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\{}.csv'.format(day))
        day_list.append(day)
    df_al1=pd.concat(day_list,axis=0)
    df_al1.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\Trips_Month_October.csv',index=False)


# In[38]:


createTripCountMonth()


# In[39]:


def createTripDensityMonth():
    day=pd.read_csv('C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\Trips_Month_October.csv')
    day['tripDensity']=day['numPoints']/day['AREASQKM21']
    day.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\TripDensity_Month_October.csv',index=False)


# In[40]:


createTripDensityMonth()


# In[68]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\Trips_Month_October.csv')


# In[56]:


map_=gpd.read_file(r'C:\Melbourne_Escooter\RealDataset\shapefiles\CityofMelbourne\COM_TrialArea.shp')


# In[69]:


SA_list=df['SA1_CODE21'].unique()


# In[70]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\count\with date\Trips_Month_October.csv')
for i in SA_list:
    df1=df[df['SA1_CODE21']==i]
    df1.to_csv(r'C:\SA similarity\TripStops\October\{}.csv'.format(i), index=False)


# In[71]:


path = r'C:\SA similarity\TripStops\October'
all_files = glob.glob(path + "/*.csv")


# In[72]:


for f in all_files:
    df = pd.read_csv(f)
    if 'date' in df.columns:
        df.rename(columns={'date': 'day'}, inplace=True)
        df['month']=10
        df['year']=2022
        df['date_time'] =  pd.to_datetime(df[[ 'year','month', 'day', 'hour']])
        df.to_csv(f, index=False)
        


# In[74]:


#SA_list -> all 350 SA
for SA in SA_list:
    df1=pd.read_csv(r'C:\SA similarity\TripStops\August\{}.csv'.format(SA))
    df2=pd.read_csv(r'C:\SA similarity\TripStops\September\{}.csv'.format(SA))
    df3=pd.read_csv(r'C:\SA similarity\TripStops\October\{}.csv'.format(SA))
    df=pd.concat([df1,df2,df3], axis=0)
    df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\{}.csv'.format(SA),index=False)


# In[ ]:


#weekday


# In[75]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[76]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[77]:


df['total_trip_density']=df['total_trip_count']/df['area']


# In[78]:


df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday.csv', index=False)


# In[79]:


static_features=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\static features.csv')
overallDataWeekday=static_features.merge(df, on='SA1_CODE21')
overallDataWeekday.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\DF-weekday.csv',index=False)


# In[ ]:


#weekend


# In[84]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[85]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[86]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend.csv', index=False)


# In[87]:


static_features=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\static features.csv')
overallDataWeekday=static_features.merge(df, on='SA1_CODE21')
overallDataWeekday.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\DF-weekend.csv',index=False)


# In[88]:


#time 0:00-5:59


# In[90]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[91]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[92]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-0_5.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-0_5.csv',index=False)


# In[93]:


#time 6:00-10:59


# In[95]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[97]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-6_10.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-6_10.csv',index=False)


# In[98]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[99]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-11_15.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-11_15.csv',index=False)


# In[100]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==16)|(df['hour']==17)|(df['hour']==18))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[101]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-16_18.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-16_18.csv',index=False)


# In[102]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[103]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-19_23.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-19_23.csv',index=False)


# In[105]:


#weekday_0-5
path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[107]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday-0_5.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekday-0_5.csv',index=False)


# In[108]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10))))]
    tripCount=df1['numPoints'].sum()
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[109]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday-6_10.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekday-6_10.csv',index=False)


# In[110]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15))))]
    tripCount=df1['numPoints'].sum()
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[111]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday-11_15.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekday-11_15.csv',index=False)


# In[112]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18))))]
    tripCount=df1['numPoints'].sum()
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[113]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday-16_18.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekday-16_18.csv',index=False)


# In[114]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23))))]
    tripCount=df1['numPoints'].sum()
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[115]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekday-19_23.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekday-19_23.csv',index=False)


# In[ ]:


#weekend_0-5


# In[116]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[117]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend-0_5.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-0_5.csv',index=False)


# In[118]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[119]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend-6_10.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-6_10.csv',index=False)


# In[120]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[121]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend-11_15.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-11_15.csv',index=False)


# In[122]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==16)|(df['hour']==17)|(df['hour']==18))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[123]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend-16_18.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-16_18.csv',index=False)


# In[124]:


path = r'C:\SA similarity\TripStops\3-months SA wise'
all_files = glob.glob(path + "/*.csv")
SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23))))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[125]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\TripStops\3-months SA wise\df -models\avgTripDensity350SA-weekend-19_23.csv', index=False)
overall=static_features.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-19_23.csv',index=False)


# In[ ]:





# In[ ]:





# In[ ]:


############ temporal ###########


# In[ ]:


#------August--------


# In[11]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly'
all_files = glob.glob(path + "/*.csv")


# In[12]:


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
result_df=pd.DataFrame({'month':8,'date':date_list,'time':time_list ,'tripCount':num_trips_list})
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\TotalCount\total.csv',index=False)

#result_df


# In[24]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\TotalCount\total.csv')


# In[25]:


df.replace({'day': {1: 'mon'}},inplace=True)
df.replace({'day': {8: 'mon'}},inplace=True)
df.replace({'day': {15: 'mon'}},inplace=True)
df.replace({'day': {22:'mon'}},inplace=True)
df.replace({'day': {29:'mon'}},inplace=True)

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
df.replace({'day': {21:'sun'}},inplace=True)
df.replace({'day': {28: 'sun'}},inplace=True)
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\TotalCount\total.csv',index=False)


# In[ ]:


#------------September--------------


# In[15]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Hourly'
all_files = glob.glob(path + "/*.csv")


# In[16]:


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
result_df=pd.DataFrame({'month':9,'date':date_list,'time':time_list ,'tripCount':num_trips_list})
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Hourly\TotalCount\total.csv',index=False)

#result_df


# In[30]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Hourly\TotalCount\total.csv')


# In[31]:


df.replace({'day': {5: 'mon'}},inplace=True)
df.replace({'day': {12: 'mon'}},inplace=True)
df.replace({'day': {19: 'mon'}},inplace=True)
df.replace({'day': {26:'mon'}},inplace=True)

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
df.replace({'day': {18:'sun'}},inplace=True)
df.replace({'day': {25: 'sun'}},inplace=True)
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Hourly\TotalCount\total.csv',index=False)


# In[ ]:


#------------October--------------


# In[19]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly'
all_files = glob.glob(path + "/*.csv")


# In[20]:


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
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\TotalCount\total.csv',index=False)

#result_df


# In[32]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\TotalCount\total.csv')


# In[33]:


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
df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\TotalCount\total.csv',index=False)


# In[34]:


AugTrip=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\TotalCount\total.csv')
SepTrip=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Hourly\TotalCount\total.csv')
OctTrip=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\TotalCount\total.csv')


# In[36]:


AugW=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\HourlyWeather\weather-Aug.csv')
SepW=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\HourlyWeather\weather-Sep.csv')
OctW=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\HourlyWeather\weather-Oct.csv')


# In[37]:


dfAug = pd.merge(AugW, AugTrip,  how='left', left_on=['MM','DD', 'HH24'], right_on = ['month','date','time'])
dfAug.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Aug_tripStop_weather.csv',index=False)
# remove month, date, time columns manually


# In[38]:


dfSep = pd.merge(SepW, SepTrip,  how='left', left_on=['MM','DD', 'HH24'], right_on = ['month','date','time'])
dfSep.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Sep_tripStop_weather.csv',index=False)
# remove month, date, time columns manually


# In[39]:


dfOct = pd.merge(OctW, OctTrip,  how='left', left_on=['MM','DD', 'HH24'], right_on = ['month','date','time'])
dfOct.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Oct_tripStop_weather.csv',index=False)
# remove month, date, time columns manually


# In[41]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Aug_tripStop_weather.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Sep_tripStop_weather.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\Oct_tripStop_weather.csv')
df_final= pd.concat([df1,df2,df3], axis=0)


# In[49]:


df_final.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\hourlyTripWeather.csv',index=False)


# In[52]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\hourlyTripWeather.csv')
df


# In[53]:


df.replace({'timeFrame': {0: '0_5'}},inplace=True)
df.replace({'timeFrame': {1: '0_5'}},inplace=True)
df.replace({'timeFrame': {2: '0_5'}},inplace=True)
df.replace({'timeFrame': {3:'0_5'}},inplace=True)
df.replace({'timeFrame': {4:'0_5'}},inplace=True)
df.replace({'timeFrame': {5:'0_5'}},inplace=True)

df.replace({'timeFrame': {6:'6_10'}},inplace=True)
df.replace({'timeFrame': {7:'6_10'}},inplace=True)
df.replace({'timeFrame': {8:'6_10'}},inplace=True)
df.replace({'timeFrame': {9:'6_10'}},inplace=True)
df.replace({'timeFrame': {10:'6_10'}},inplace=True)

df.replace({'timeFrame': {11:'11_15'}},inplace=True)
df.replace({'timeFrame': {12:'11_15'}},inplace=True)
df.replace({'timeFrame': {13:'11_15'}},inplace=True)
df.replace({'timeFrame': {14:'11_15'}},inplace=True)
df.replace({'timeFrame': {15:'11_15'}},inplace=True)

df.replace({'timeFrame': {16:'16_18'}},inplace=True)
df.replace({'timeFrame': {17:'16_18'}},inplace=True)
df.replace({'timeFrame': {18:'16_18'}},inplace=True)

df.replace({'timeFrame': {19:'19_23'}},inplace=True)
df.replace({'timeFrame': {20:'19_23'}},inplace=True)
df.replace({'timeFrame': {21:'19_23'}},inplace=True)
df.replace({'timeFrame': {22:'19_23'}},inplace=True)
df.replace({'timeFrame': {23:'19_23'}},inplace=True)


# In[54]:


df.to_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\hourlyTripWeather_timeFrames.csv',index=False)


# In[ ]:




