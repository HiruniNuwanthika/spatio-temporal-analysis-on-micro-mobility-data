#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import os
import glob
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point


# In[4]:


df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\Weekday\1.csv')


# In[106]:


#test single  file
df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\Weekday\20.csv'.format(i))
df0=df[df['datetime'].str.contains(':0:')]
list_0.append(df0)
fina_df_0=pd.concat(list_0,axis=0)


# In[ ]:


#weekday---------start ----------------stop


# In[140]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
for i in range(1,31):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':0:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':1:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':2:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':3:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':4:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    df5=df[df['datetime'].str.contains(':5:')]
    list_5.append(df5)
    fina_df_5=pd.concat(list_5,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4,fina_df_5], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\0_5.csv',index=False)
    
    
    


# In[141]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,31):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':6:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':7:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':8:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':9:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':10:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\time_6_10.csv',index=False)
    
    
    


# In[142]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':11:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':12:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':13:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':14:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':15:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\time_11_15.csv',index=False)
    
    
    


# In[143]:


list_0=[]
list_1=[]
list_2=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':16:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':17:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':18:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\Weekday\time_16_18.csv',index=False)
    
    
    


# In[160]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekday\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':19:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':20:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':21:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':22:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':23:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekday\time_19_23.csv',index=False)
    
    
    


# In[112]:


#weekend


# In[154]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
for i in range(1,31):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':0:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':1:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':2:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':3:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':4:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    df5=df[df['datetime'].str.contains(':5:')]
    list_5.append(df5)
    fina_df_5=pd.concat(list_5,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4,fina_df_5], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\time_0_5.csv',index=False)
    
    
    


# In[194]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,31):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\Weekend\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':6:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':7:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':8:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':9:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':10:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\Weekend\time_6_10.csv',index=False)
    
    
    


# In[156]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':11:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':12:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':13:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':14:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':15:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\time_11_15.csv',index=False)
    
    
    


# In[157]:


list_0=[]
list_1=[]
list_2=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':16:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':17:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':18:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\time_16_18.csv',index=False)
    
    
    


# In[159]:


list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
for i in range(1,32):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\{}.csv'.format(i))
    except:
        continue
    print(i)
    df0=df[df['datetime'].str.contains(':19:')]
    list_0.append(df0)
    fina_df_0=pd.concat(list_0,axis=0)
    df1=df[df['datetime'].str.contains(':20:')]
    list_1.append(df1)
    fina_df_1=pd.concat(list_1,axis=0)
    df2=df[df['datetime'].str.contains(':21:')]
    list_2.append(df2)
    fina_df_2=pd.concat(list_2,axis=0)
    df3=df[df['datetime'].str.contains(':22:')]
    list_3.append(df3)
    fina_df_3=pd.concat(list_3,axis=0)
    df4=df[df['datetime'].str.contains(':23:')]
    list_4.append(df4)
    fina_df_4=pd.concat(list_4,axis=0)
    final=pd.concat([fina_df_0, fina_df_1,fina_df_2,fina_df_3,fina_df_4], axis=0)
result_df= pd.DataFrame (final)
result_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\Weekend\time_19_23.csv',index=False)
    
    
    


# In[ ]:


#time framed starts(stops) - weekday


# In[178]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\weekday\time_0_5.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\weekday\time_0_5.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\weekday\time_0_5.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-0_5.csv',index=False)


# In[179]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\weekday\time_6_10.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\weekday\time_6_10.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\weekday\time_6_10.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-6_10.csv',index=False)


# In[180]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\weekday\time_11_15.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\weekday\time_11_15.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\weekday\time_11_15.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-11_15.csv',index=False)


# In[181]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\weekday\time_16_18.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\weekday\time_16_18.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\weekday\time_16_18.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-16_18.csv',index=False)


# In[182]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Daily\weekday\time_19_23.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Started\Daily\weekday\time_19_23.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Started\Daily\weekday\time_19_23.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekdayTrips-start-19_23.csv',index=False)


# In[183]:


#time framed starts(stops) - weekend


# In[189]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekend\time_0_5.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekend\time_0_5.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekend\time_0_5.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop-0_5.csv',index=False)


# In[195]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekend\time_6_10.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekend\time_6_10.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekend\time_6_10.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop-6_10.csv',index=False)


# In[196]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekend\time_11_15.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekend\time_11_15.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekend\time_11_15.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop-11_15.csv',index=False)


# In[197]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekend\time_16_18.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekend\time_16_18.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekend\time_16_18.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop-16_18.csv',index=False)


# In[198]:


df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Daily\weekend\time_19_23.csv')
df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\September\Stopped\Daily\weekend\time_19_23.csv')
df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Daily\weekend\time_19_23.csv')
final_df=pd.concat([df1,df2,df3], axis=0)
final_df.to_csv(r'C:\Buffer Analysis\Python-results\weekendTrips-stop-19_23.csv',index=False)


# In[ ]:




