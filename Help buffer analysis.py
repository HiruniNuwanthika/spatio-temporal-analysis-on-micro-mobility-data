#!/usr/bin/env python
# coding: utf-8

# In[1]:


#create 1 day files combining 0-23 hour files


# In[2]:


import pandas as pd
import os
import glob
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point
import numpy as np


# In[9]:


for day in range (1,31):
    df_list=[]
    for i in range(0,24):
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Hourly\{}_{}.csv'.format(day,i))
        df_list.append(df)
        fina_df=pd.concat(df_list,axis=0)
    result_df= pd.DataFrame (fina_df)
    result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\{}.csv'.format(day),index=False)


# In[29]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekday'
all_files = glob.glob(path + "/*.csv")


# In[30]:


weekday_list=[]
for f in all_files:
    df = pd.read_csv(f)
    weekday_list.append(df)
    fina_df=pd.concat(weekday_list,axis=0)
result_df= pd.DataFrame (fina_df)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekday\weekdayTrips.csv'.format(day),index=False)


# In[31]:


path = r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekend'
all_files = glob.glob(path + "/*.csv")


# In[32]:


weekend_list=[]
for f in all_files:
    df = pd.read_csv(f)
    weekend_list.append(df)
    fina_df=pd.concat(weekend_list,axis=0)
result_df= pd.DataFrame (fina_df)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekend\weekendTrips.csv'.format(day),index=False)


# In[55]:


#concat weekdays of 3 months and weekends of 3 months


# In[35]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekday\weekdayTrips.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekday\weekdayTrips.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekday\weekdayTrips.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-stop.csv',index=False)


# In[36]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekend\weekendTrips.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\Weekend\weekendTrips.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\weekendTrips.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop.csv',index=False)


# In[71]:


df1


# In[128]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Melbourne-buildings\Recreation\recreations.csv')


# In[129]:


df


# In[ ]:


#count points in polygon


# In[47]:


map_=gpd.read_file(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekday\60m buffer.shp')
unique_map=map_.drop_duplicates()


# In[48]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Melbourne-buildings\houses.csv')
df['coords'] = list(zip(df['x coordinate'],df['y coordinate']))
df['coords'] = df['coords'].apply(Point)
points = gpd.GeoDataFrame(df, geometry='coords', crs=unique_map.crs)
pointInPolys = gpd.tools.sjoin(points, unique_map, op="within", how='left')

count=pointInPolys.groupby(['bike_id','latitude','longitude','datetime']).size().reset_index(name='count')
#count.to_csv(r'C:\Buffer Analysis\Python-results\recreation\weekend-stop60m_time19_23.csv',index=False)


# In[49]:


tripCount=len(unique_map)
print('total unique trips ='+ str(tripCount))


# In[50]:


print('non-zero trip count='+ str(len(count)))


# In[68]:


print('non-zero trip count='+ str(len(count)))


# In[68]:


print('non-zero trip count='+ str(len(count)))


# In[60]:


#analysis


# In[387]:


df=pd.read_csv(r'C:\Buffer Analysis\Python-results\cafe\weekday-start60m_time0_5.csv')


# In[388]:


df.head()


# In[389]:


df['count'].unique()


# In[390]:


inBuffer_zero=len(df[df['count']==0])
inBuffer_1_10=len(df[(df['count']>0) &(df['count']<=10)])
inBuffer_11_20=len(df[(df['count']>10) &(df['count']<=20)])
inBuffer_21_30=len(df[(df['count']>20) &(df['count']<=30)])
inBuffer_31_40=len(df[(df['count']>30) &(df['count']<=40)])
inBuffer_41_50=len(df[(df['count']>40) &(df['count']<=50)])
inBuffer_more50=len(df[(df['count']>=51)])


# In[391]:


print( '0 :' +str(inBuffer_zero) + '\n1-10 :' +str(inBuffer_1_10)+'\n11-20 :' +str(inBuffer_11_20)+ '\n21-30 :' +str(inBuffer_21_30)+ '\n31-40 :' +str(inBuffer_31_40)+ '\n41-50 :' +str(inBuffer_41_50)+ '\nmore50 :' +str(inBuffer_more50))


# # plotting no go zones on map
# 

# In[ ]:


import requests
from requests.structures import CaseInsensitiveDict
import json 
from datetime import datetime
import time
from retry import retry
from json import JSONDecodeError
import pandas as pd


with open(r'C:/Melbourne_Escooter/Lime/Scheduled_downloads/Zones.json','r') as f:
    data = json.loads(f.read())
df_normalized=pd.json_normalize(data, ['data','geofencing_zones','features'])
df_normalized.to_csv(r'C:\Melbourne_Escooter\RealDataset\shapefiles\trial zones\allZones.csv',index=False)
#df_rules= pd.json_normalize(data, ['data','geofencing_zones','features','properties','rules'])
#no_parking=df_rules[df_rules['ride_end_allowed']==False]
#no_parking
#df_normalized_escooter=df_normalized[df_rules[df_rules['ride_end_allowed']==False]]
#df_normalized_escooter


# In[ ]:





# In[320]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\shapefiles\trial zones\no parking zones.csv')
df['geometry.coordinates']


# In[321]:


from shapely.geometry import Polygon

geometry =df['geometry.coordinates'].apply(lambda x: Polygon(eval(x)))


# In[322]:


polygon_ = gpd.GeoDataFrame(df, crs={'init': 'epsg:4326'},geometry=geometry)


# In[325]:


polygon_.to_file(r"C:\Melbourne_Escooter\RealDataset\shapefiles\trial zones\noPark.shp")


# In[ ]:





# # plot % pois in buffer

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[27]:


df=pd.DataFrame({'x_values':['0_5','6_10','11_15','16-18','19_23'], 'weekday_start':[31,27,32,32,30], 'weekday_stop': [31,31,33,31,29],'weekend_start': [31,29,31,29,30] ,'weekend_stop':[30,32,31,29,30]})


# In[40]:


plt.plot( 'x_values', 'weekday_start', data=df, marker='', color='green', linewidth=2)
plt.plot( 'x_values', 'weekday_stop', data=df, marker='', color='red', linewidth=2)
plt.plot( 'x_values', 'weekend_start', data=df, marker='', color='green', linewidth=2, linestyle='dashed')
plt.plot( 'x_values', 'weekend_stop', data=df, marker='', color='red', linewidth=2, linestyle='dashed')

plt.legend()
plt.title('% trips having Tram stops in 60m buffer')
plt.xlabel("Time of the day")
plt.ylabel("% trips with in 60m buffer")

plt.legend(loc=(1.05, 0.5))
plt.tight_layout()
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
  
N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [31.3,27.3,32.1,31.6,29.9]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [30.8,30.7,33.0,30.8,29.4]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [31.1,28.8,31.3,28.9,30.2]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [29.6,31.7,31.4,28.8,30.5]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=35) #ymax is your value
plt.ylim(bottom=25) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffe')
plt.title("Trips having Tram stops in 60m buffer")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[5]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [61.4,48.7,54.3,52.8,57.8]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [59.9,54.0,54.9,52.9,56.5]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [60.3,50.4,49.5,48.8,53.1]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [57.6,52.6,50.2,49.2,53.6]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=65) #ymax is your value
plt.ylim(bottom=40) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffe')
plt.title("Trips having Cafes in 60m buffer")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[47]:


# weekday only around houses

N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [67.9,64.2,54.4,56.3,59.3]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [69.9,57.3,55.3,58.6,61.7]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  

plt.ylim(top=75) #ymax is your value
plt.ylim(bottom=45) #ymin is your value
 
plt.xlabel("Time frame (0-23 hours)",fontsize=14)
plt.ylabel('Trips % within 60m buffer',fontsize=14)
#plt.title("Trips having houses in 60m buffer")
plt.yticks(fontsize=15)
plt.xticks(ind+width,['0-5', '6-10', '11-15','16-18','19-23'],fontsize=15)
plt.legend( (bar1, bar2), ('Trip-start', 'Trip-stop'), loc=(1.05, 0.5),fontsize=18)
plt.show()


# In[7]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [67.9,64.2,54.4,56.3,59.3]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [69.9,57.3,55.3,58.6,61.7]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [61.6,62.4,52.3,53.4,54.6]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [64.1,58.5,52.1,53.4,56.0]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=75) #ymax is your value
plt.ylim(bottom=45) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffe')
plt.title("Trips having houses in 60m buffer")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[45]:


# office 60m only weekdays

N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [43.7,35.7,40.2,39.0,41.9]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [42.4,41.3,39.9,38.3,40.9]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  

plt.ylim(top=50) #ymax is your value
plt.ylim(bottom=30) #ymin is your value

plt.xlabel("Time frame (0-23 hours)",fontsize=14)
plt.ylabel('Trips % within 60m buffer',fontsize=14)
#plt.title("Trips having offices in 60m buffer")
plt.yticks(fontsize=14)
plt.xticks(ind+width,['0-5', '6-10', '11-15','16-18','19-23'],fontsize=15)
plt.legend( (bar1, bar2), ('start', 'stop'), loc=(1.05, 0.5))
plt.show()


# In[8]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [43.7,35.7,40.2,39.0,41.9]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [42.4,41.3,39.9,38.3,40.9]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [43.6,36.5,34.9,34.5,37.8]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [41.3,38.8,34.8,35.0,38.1]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=50) #ymax is your value
plt.ylim(bottom=30) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffe')
plt.title("Trips having offices in 60m buffer")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[50]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [11.2,14.4,16.0,16.5,13.4]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [13.1,17.2,17.5,16.0,13.8]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [12.5,14.1,14.2,12.9,13.1]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [13.8,15.5,15.8,13.7,13.6]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=20) #ymax is your value
plt.ylim(bottom=10) #ymin is your value
plt.yticks(fontsize=15)
plt.xlabel("Time frame (0-23 hours)",fontsize=14)
plt.ylabel('Trips % within 10m buffer',fontsize=14)
#plt.title("Trips within 10m buffer from bike lanes")
  
plt.xticks(ind+width,['0-5', '6-10', '11-15','16-18','19-23'],fontsize=15)
plt.legend( (bar1, bar2, bar3,bar4), ('Weekday Trip-start', 'Weekday Trip-stop', 'Weekend Trip-start','Weekend Trip-stop'), loc=(1.05, 0.5),fontsize=18)
plt.show()


# In[26]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [69.0,71.9,72.6,74.7,73.0]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [74.1,71.3,74.8,76.8,75.7]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [68.7,70.6,69.8,70.6,68.9]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [73.7,76.1,75.5,73.3,71.6]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

#plt.ylim(top=80) #ymax is your value
plt.ylim(bottom=60) #ymin is your value
plt.yticks(fontsize=13)
plt.xlabel("Time frame (0-23 hours)",fontsize=13)
plt.ylabel('Trips % within 10m buffer',fontsize=13)
#plt.title("Trips within 10m buffer from foot paths")
  
plt.xticks(ind+width,['0-5', '6-10', '11-15','16-18','19-23'],fontsize=14)
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[30]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [2.4,3.3,4.5,4.3,4.0]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [3.3,4.2,4.4,4.0,3.5]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [3.6,4.2,4.9,5.3,4.8]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [3.8,4.7,5.2,5.5,4.4]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

plt.ylim(top=7) #ymax is your value
plt.ylim(bottom=1) #ymin is your value
plt.yticks(fontsize=14)
plt.xlabel("Time frame (0-23 hours)",fontsize=13)
plt.ylabel('Trips % within 10m buffer',fontsize=13)
#plt.title("Trips within 10m buffer from shared path")
  
plt.xticks(ind+width,['0-5', '6-10', '11-15','16-18','19-23'],fontsize=14)
plt.legend( (bar1, bar2, bar3,bar4), ('wd_start', 'wd_stop', 'we_start','we_stop'), loc=(1.05, 0.5))
plt.show()


# In[1]:


#Diffrence graphs


# In[58]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [-1.6,6.9,-0.9,-2.2,-2.4]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekday trips : Houses")
plt.show()


# In[59]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [-2.4,3.9,0.2,0.0,-1.3]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekend trips : Houses")
plt.show()


# In[60]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [1.5,-5.3,-0.5,-0.1,1.3]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekday trips : Cafes")
plt.show()


# In[61]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [2.7,-2.2,-0.7,-0.4,-0.5]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekend trips : Cafes")
plt.show()


# In[64]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [1.3,-5.6,0.3,0.7,1.0]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekday trips : Offices")
plt.show()


# In[65]:


import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [2.3,-2.3,0.1,-0.5,-0.3]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekend trips : Offices")
plt.show()


# In[66]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [0.5,-3.5,-0.8,0.8,0.5]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekday trips : Tram stops")
plt.show()


# In[67]:



import matplotlib.pyplot as plt
fig = plt.figure(figsize=(3, 3))
ax = fig.add_axes([0,0,1,1])
x=['0_5', '6_10', '11_15','16_18','19_23']
y = [1.4,-2.9,-0.2,0.1,-0.3]
ax.axhline(0, color='black')
ax.bar(x,y,width=0.4)
plt.xlabel("Time frame")
plt.ylabel('differnece of trip%')
plt.title("Outflow-Inflow weekend trips : Tram stops")
plt.show()


# In[68]:


#comparing trips around bike lanes, walking tracks and shared paths


# In[71]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [33.1,38.3,42.5,42.8,37.3]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [10.6,11.0,15.3,14.7,13.8]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [10.8,14.4,18.6,17.4,16.4]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')



plt.ylim(top=45) #ymax is your value
plt.ylim(bottom=5) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffer')
plt.title("Weekday Trip starts within 60m buffer from different paths")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3), ('bike lane', 'walking track','shared path'), loc=(1.05, 0.5))
plt.show()


# In[72]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [34.3,42.8,42.0,39.1,36.4]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [10.3,13.2,15.9,14.5,12.7]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [12.1,16.1,17.8,17.0,15.5]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')



plt.ylim(top=45) #ymax is your value
plt.ylim(bottom=5) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffer')
plt.title("Weekday Trip stops within 60m buffer from different paths")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3), ('bike lane', 'walking track','shared path'), loc=(1.05, 0.5))
plt.show()


# In[73]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [34.8,37.2,37.7,34.9,34.8]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [12.5,15.0,19.1,16.3,14.5]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [14.7,17.0,20.7,21.4,19.7]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')



plt.ylim(top=45) #ymax is your value
plt.ylim(bottom=5) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffer')
plt.title("Weekend Trip starts within 60m buffer from different paths")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3), ('bike lane', 'walking track','shared path'), loc=(1.05, 0.5))
plt.show()


# In[74]:


N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [35.9,39.6,39.2,34.8,34.9]
bar1 = plt.bar(ind, xvals, width, color = 'r')
  
yvals = [12.9,18.1,20.5,17.0,14.0]
bar2 = plt.bar(ind+width, yvals, width, color='g')
  
zvals = [15.0,19.3,21.6,21.7,18.5]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'b')



plt.ylim(top=45) #ymax is your value
plt.ylim(bottom=5) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in 60m buffer')
plt.title("Weekend Trip stops within 60m buffer from different paths")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3), ('bike lane', 'walking track','shared path'), loc=(1.05, 0.5))
plt.show()


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
  
N = 5
ind = np.arange(N) 
width = 0.2
      
xvals = [49,53,53,53,53]
bar1 = plt.bar(ind, xvals, width, color = 'g')
  
yvals = [20,19,19,20,20]
bar2 = plt.bar(ind+width, yvals, width, color='r')
  
zvals = [49,52,52,53,51]
bar3 = plt.bar(ind+width*2, zvals, width, color = 'g', hatch="/")

kvals = [20,19,18,18,18]
bar4 = plt.bar(ind+width*3, kvals, width, color = 'r', hatch="/")

#plt.ylim(top=35) #ymax is your value
#plt.ylim(bottom=25) #ymin is your value
 
plt.xlabel("Time frame")
plt.ylabel('% trips with in buffer')
plt.title("Trip Starts around footpaths")
  
plt.xticks(ind+width,['0_5', '6_10', '11_15','16_18','19_23'])
plt.legend( (bar1, bar2, bar3,bar4), ('wd start 5m buffer', 'wd start 5m-10m buffer', 'we start 5m buffer','we start 5m-10m buffer'), loc=(1.05, 0.5))
plt.show()


# In[1]:


#combine POIs


# In[2]:


df1=pd.read_csv(r'C:\Buffer Analysis\Python-results\house\weekday-start60m_time0_5.csv')
df1.rename(columns = {'count':'houseCount'}, inplace = True)
df2=pd.read_csv(r'C:\Buffer Analysis\Python-results\office\weekday-start60m_time0_5.csv')
df2.rename(columns = {'count':'officeCount'}, inplace = True)
house_office=pd.merge(df1,df2,how='outer',on=['bike_id','latitude','longitude','datetime'])


# In[3]:


house_office


# In[4]:


df3=pd.read_csv(r'C:\Buffer Analysis\Python-results\cafe\weekday-start60m_time0_5.csv')
df3.rename(columns = {'count':'cafeCount'}, inplace = True)
df4=pd.read_csv(r'C:\Buffer Analysis\Python-results\tram\weekday_start60m_time0_5.csv')
df4.rename(columns = {'count':'tramCount'}, inplace = True)
cafe_tram=pd.merge(df3,df4,how='outer',on=['bike_id','latitude','longitude','datetime'])


# In[5]:


cafe_tram


# In[28]:


df_final=pd.merge(cafe_tram,house_office, on=['bike_id','latitude','longitude'],how='outer')
df_final.drop('datetime_y', inplace=True, axis=1)
df_final.drop('datetime_x', inplace=True, axis=1)
df=df_final.drop_duplicates(subset=['bike_id', 'latitude','longitude','cafeCount','tramCount','houseCount','officeCount'])
df


# In[30]:


df.to_csv(r'C:\Buffer Analysis\Python-results\buffers\weekday-start60m_time0_5.csv',index=False)


# In[43]:


df.notna().sum()# least among these tells us count having all POIs


# In[48]:


subdf=df[['cafeCount','tramCount','houseCount','officeCount']]
subdf['max']=subdf.idxmax(axis=1)
subdf.to_csv()


# In[34]:


df.count(axis=1)


# In[41]:


df.query('cafeCount == cafeCount & tramCount==tramCount')


# In[ ]:




