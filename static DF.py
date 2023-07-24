#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import glob
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import ckwrap


# In[2]:


#descriptive stat of static features


# In[2]:


df_static=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv')


# In[9]:


desc=df_static.describe()
desc.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF_description.csv')


# In[ ]:





# In[ ]:


# calculate avg trip densiy for each SA


# In[20]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[22]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    tripCount=df['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[24]:


df['total_trip_density']=df['total_trip_count']/df['area']


# In[25]:


df


# In[26]:


df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA.csv', index=False)


# In[27]:


#merge trip density and static features


# In[37]:


static=pd.read_csv(r'C:\SA similarity\static features.csv')


# In[29]:


overallData=static.merge(df, on='SA1_CODE21')


# In[31]:


overallData.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv',index=False)


# In[ ]:





# In[ ]:





# In[26]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\20604111702.csv')


# In[27]:


df


# In[ ]:


#weekday dataset


# In[44]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[33]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\20604111702.csv')
df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28))))]
tripCount=df1['numPoints'].sum()
tripCount


# In[45]:


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


# In[46]:


df['total_trip_density']=df['total_trip_count']/df['area']


# In[47]:


df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday.csv', index=False)


# In[48]:


overallDataWeekday=static.merge(df, on='SA1_CODE21')


# In[50]:


overallDataWeekday.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday.csv',index=False)


# In[ ]:





# In[ ]:


#weekend dataset


# In[34]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\20604111702.csv')
df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30))))]
tripCount=df1['numPoints'].sum()
tripCount


# In[51]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[52]:


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


# In[53]:


df['total_trip_density']=df['total_trip_count']/df['area']


# In[54]:


df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend.csv', index=False)


# In[55]:


overallDataWeekend=static.merge(df, on='SA1_CODE21')


# In[56]:


overallDataWeekend.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend.csv',index=False)


# In[ ]:





# In[57]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\20604111702.csv')


# In[59]:


df1=df[((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))]
tripCount=df1['numPoints'].sum()
tripCount


# In[ ]:


#time 0:00-5:59


# In[62]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[63]:


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


# In[64]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-0_5.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-0_5.csv',index=False)


# In[ ]:


#time 6:00-10:59


# In[68]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==0)|(df['hour']==6)|(df['hour']==7)|(df['hour']==8)|(df['hour']==9)|(df['hour']==10))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[69]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-6_10.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-6_10.csv',index=False)


# In[72]:


#time 11:00-15:59


# In[73]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==0)|(df['hour']==11)|(df['hour']==12)|(df['hour']==13)|(df['hour']==14)|(df['hour']==15))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[74]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-11_15.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-11_15.csv',index=False)


# In[75]:


#time 16:00-18:59


# In[76]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==0)|(df['hour']==16)|(df['hour']==17)|(df['hour']==18))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[77]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-16_18.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-16_18.csv',index=False)


# In[78]:


#time 19:00-23:59


# In[79]:


SA_list=[]
SA_area=[]
tripCountList=[]
for f in all_files:
    df = pd.read_csv(f)
    SA=df['SA1_CODE21'].iloc[0] 
    df1=df[((df['hour']==0)|(df['hour']==19)|(df['hour']==20)|(df['hour']==21)|(df['hour']==22)|(df['hour']==23))]
    tripCount=df1['numPoints'].sum()
    area=df['AREASQKM21'].iloc[0] 
    SA_list.append(SA)
    tripCountList.append(tripCount)
    SA_area.append(area)
df = pd.DataFrame(list(zip(SA_list, tripCountList,SA_area)),columns =['SA1_CODE21', 'total_trip_count','area']) 


# In[80]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-19_23.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-19_23.csv',index=False)


# In[ ]:





# In[ ]:


#weekday 0_5


# In[90]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[91]:


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


# In[92]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday-0_5.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-0_5.csv',index=False)


# In[ ]:


#weekday 6_10


# In[97]:


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


# In[98]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday-6_10.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-6_10.csv',index=False)


# In[ ]:


#weekday 11_15


# In[ ]:


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


# In[ ]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday-11_15.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-11_15.csv',index=False)


# In[ ]:


#weekday 16_18


# In[101]:


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


# In[102]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday-16_18.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-16_18.csv',index=False)


# In[ ]:


#weekday 19_23


# In[103]:


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


# In[104]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekday-19_23.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekday-19_23.csv',index=False)


# In[ ]:


#weekend 0_5


# In[111]:


path = r'C:\SA similarity\Trips\3-months SA wise'
all_files = glob.glob(path + "/*.csv")


# In[112]:


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


# In[113]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend-0_5.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-0_5.csv',index=False)


# In[ ]:


#weekend 6_10


# In[114]:


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


# In[115]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend-6_10.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-6_10.csv',index=False)


# In[ ]:


#weekend 11_15


# In[116]:


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


# In[117]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend-11_15.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-11_15.csv',index=False)


# In[ ]:


#weekend 16_18


# In[118]:


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


# In[119]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend-16_18.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-16_18.csv',index=False)


# In[ ]:


#weekend 19_23


# In[120]:


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


# In[121]:


df['total_trip_density']=df['total_trip_count']/df['area']
df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\avgTripDensity350SA-weekend-19_23.csv', index=False)
overall=static.merge(df, on='SA1_CODE21')
column=['SA_num','AREASQKM21','total_trip_count','area','House perc']
overall_df=overall.drop(column, axis=1)
overall_df.to_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-weekend-19_23.csv',index=False)


# In[ ]:





# In[ ]:





# In[88]:


df1=df[(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))))]
tripCount=df1['numPoints'].sum()
tripCount


# In[85]:


(((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))))


# In[89]:


df1=df[((((df['month']==8) & ((df['day']==1)|(df['day']==2)|(df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==8)|(df['day']==9)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==15)|(df['day']==16)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==22)|(df['day']==23)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==29)|(df['day']==30)|(df['day']==31)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==1)|(df['day']==2)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==8)|(df['day']==9)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==15)|(df['day']==16)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==22)|(df['day']==23)|(df['day']==26)|(df['day']==27)|(df['day']==28)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==3)|(df['day']==4)|(df['day']==5)|(df['day']==6)|(df['day']==7)|(df['day']==10)|(df['day']==11)|(df['day']==12)|(df['day']==13)|(df['day']==14)|(df['day']==17)|(df['day']==18)|(df['day']==19)|(df['day']==20)|(df['day']==21)|(df['day']==24)|(df['day']==25)|(df['day']==26)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))))]
tripCount=df1['numPoints'].sum()
tripCount


# In[106]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\20604111702.csv')
df1=df[(((df['month']==8) & ((df['day']==6)|(df['day']==7)|(df['day']==13)|(df['day']==14)|(df['day']==20)|(df['day']==21)|(df['day']==27)|(df['day']==28)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==9) & ((df['day']==3)|(df['day']==4)|(df['day']==10)|(df['day']==11)|(df['day']==17)|(df['day']==18)|(df['day']==24)|(df['day']==25)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5)))|((df['month']==10) & ((df['day']==1)|(df['day']==2)|(df['day']==8)|(df['day']==9)|(df['day']==15)|(df['day']==16)|(df['day']==22)|(df['day']==23)|(df['day']==29)|(df['day']==30)) &((df['hour']==0)|(df['hour']==1)|(df['hour']==2)|(df['hour']==3)|(df['hour']==4)|(df['hour']==5))))]
tripCount=df1['numPoints'].sum()
tripCount


# In[ ]:





# In[ ]:





# In[ ]:




