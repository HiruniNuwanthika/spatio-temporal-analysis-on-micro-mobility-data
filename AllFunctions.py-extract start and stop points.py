#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import json
import numpy as np
import datetime
from functools import reduce


# In[2]:


def dateSetPerHour(day):
    for hour in range(0,24):
#first part of the data
        data_frames1 = []
        files1=[]
        for file_id in range(1,16):
            try:
                with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t{}_{}.json'.format(day,hour,file_id),'r') as f:
                    data = json.loads(f.read())
                df_normalized=pd.json_normalize(data, ['data', 'bikes'])
                df_normalized_escooter=df_normalized[df_normalized['vehicle_type']=='scooter']
                df_normalized_escooter.drop(['is_reserved', 'is_disabled','vehicle_type_id','pricing_plan_id','last_reported','vehicle_type'], axis=1, inplace=True)
                df=pd.DataFrame(df_normalized_escooter)
                data_frames1.append(df)
                files1.append(file_id)
            except FileNotFoundError:
                continue
        if(len(data_frames1)!=0):
            df_merged1 = reduce(lambda  left,right: pd.merge(left,right,on=['bike_id'],suffixes=('_a', '_b'),
                                                   how='outer'), data_frames1)
            #create dynamic column names
            columns1=['bike_id']
            for i in files1:
                columns1.append('lat_%s' %i)
                columns1.append('lon_%s' %i)
                columns1.append('range_%s' %i)
            #print(columns)
            #add created colunm names
            df_merged1.columns = columns1
            #save file
            df_merged1.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part1.csv'.format(day,hour), index=False)
#second part of the data
        data_frames2= []
        files2=[]
        for file_id in range(16,31):
            try:
                with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t{}_{}.json'.format(day,hour,file_id),'r') as f:
                    data = json.loads(f.read())
                df_normalized=pd.json_normalize(data, ['data', 'bikes'])
                df_normalized_escooter=df_normalized[df_normalized['vehicle_type']=='scooter']
                df_normalized_escooter.drop(['is_reserved', 'is_disabled','vehicle_type_id','pricing_plan_id','last_reported','vehicle_type'], axis=1, inplace=True)
                df=pd.DataFrame(df_normalized_escooter)
                data_frames2.append(df)
                files2.append(file_id)
            except FileNotFoundError:
                continue
        if(len(data_frames2)!=0):
            df_merged2 = reduce(lambda  left,right: pd.merge(left,right,on=['bike_id'],suffixes=('_a', '_b'),
                                                   how='outer'), data_frames2)
            #create dynamic column names
            columns2=['bike_id']
            for i in files2:
                columns2.append('lat_%s' %i)
                columns2.append('lon_%s' %i)
                columns2.append('range_%s' %i)
            #add created colunm names
            df_merged2.columns = columns2
            #save file
            df_merged2.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part2.csv'.format(day,hour), index=False)
#Third part of the dataset
        data_frames3= []
        files3=[]
        for file_id in range(31,46):
            try:
                with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t{}_{}.json'.format(day,hour,file_id),'r') as f:
                    data = json.loads(f.read())
                df_normalized=pd.json_normalize(data, ['data', 'bikes'])
                df_normalized_escooter=df_normalized[df_normalized['vehicle_type']=='scooter']
                df_normalized_escooter.drop(['is_reserved', 'is_disabled','vehicle_type_id','pricing_plan_id','last_reported','vehicle_type'], axis=1, inplace=True)
                df=pd.DataFrame(df_normalized_escooter)
                data_frames3.append(df)
                files3.append(file_id)
            except FileNotFoundError:
                continue
        if(len(data_frames3)!=0):
            df_merged3 = reduce(lambda  left,right: pd.merge(left,right,on=['bike_id'],suffixes=('_a', '_b'),
                                                   how='outer'), data_frames3)
            #create dynamic column names
            columns3=['bike_id']
            for i in files3:
                columns3.append('lat_%s' %i)
                columns3.append('lon_%s' %i)
                columns3.append('range_%s' %i)
            #add created colunm names
            df_merged3.columns = columns3
            #save file
            df_merged3.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part3.csv'.format(day,hour), index=False)
#fourth part of the dataset
        data_frames4= []
        files4=[]
        for file_id in range(46,60):
            try:
                with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t{}_{}.json'.format(day,hour,file_id),'r') as f:
                    data = json.loads(f.read())
                df_normalized=pd.json_normalize(data, ['data', 'bikes'])
                df_normalized_escooter=df_normalized[df_normalized['vehicle_type']=='scooter']
                df_normalized_escooter.drop(['is_reserved', 'is_disabled','vehicle_type_id','pricing_plan_id','last_reported','vehicle_type'], axis=1, inplace=True)
                df=pd.DataFrame(df_normalized_escooter)
                data_frames4.append(df)
                files4.append(file_id)
            except FileNotFoundError:
                continue
        if(len(data_frames4)!=0):
            df_merged4 = reduce(lambda  left,right: pd.merge(left,right,on=['bike_id'],suffixes=('_a', '_b'),
                                                   how='outer'), data_frames4)
            #create dynamic column names
            columns4=['bike_id']
            for i in files4:
                columns4.append('lat_%s' %i)
                columns4.append('lon_%s' %i)
                columns4.append('range_%s' %i)
            #add created colunm names
            df_merged4.columns = columns4
            #save file
            df_merged4.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour), index=False)
#new minute (next_hour:00) data merge to fourth part of the dataset
            try:
                if((hour+1)!=24):
                    with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t{}_0.json'.format(day,(hour+1)),'r') as f:
                        data = json.loads(f.read())
                else:
                    with open(r'C:\Melbourne_Escooter\RealDataset\August\8_{}t0_0.json'.format(day+1),'r') as f:
                        data = json.loads(f.read())
            except FileNotFoundError:
                continue
            df_normalized=pd.json_normalize(data, ['data', 'bikes'])
            df_normalized_escooter=df_normalized[df_normalized['vehicle_type']=='scooter']
            df_normalized_escooter.drop(['is_reserved', 'is_disabled','vehicle_type_id','pricing_plan_id','last_reported','vehicle_type'], axis=1, inplace=True)
            df=pd.DataFrame(df_normalized_escooter)
            df.columns = ['bike_id', 'lat_60', 'lon_60', 'range_60']
            part4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour))
            df_4=part4.merge(df, how='outer', on='bike_id')
            df_4.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour), index=False)


# In[4]:


dateSetPerHour(31)


# # Starts

# In[22]:


def tripStarts(day):
    for hour in range(0,24):
#1-15 minutes dataset
        try:
            if hour==0:
                df1_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_23hour_part4.csv'.format(day-1))
                df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part1.csv'.format(day,hour))
                df1__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part2.csv'.format(day,hour))
            else:   
                df1_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour-1))
                df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part1.csv'.format(day,hour))
                df1__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part2.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        started_list1=[]
        if((df1['bike_id'].isin(df1_['bike_id']).any()) & (df1['bike_id'].isin(df1__['bike_id']).any())):
            for i in range(2,14):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        started=df1[(df1['lat_%s' %i].isnull()==False) & (df1['lat_%s' %(i+1)].isnull()==True)]
                        started_list1.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df1['bike_id'].isin(df1_['bike_id']).any()):
            for i in range(2,15):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        started=df1[(df1['lat_%s' %i].isnull()==False) & (df1['lat_%s' %(i+1)].isnull()==True)]
                        started_list1.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df1['bike_id'].isin(df1__['bike_id']).any()):
            for i in range(1,14):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        started=df1[(df1['lat_%s' %i].isnull()==False) & (df1['lat_%s' %(i+1)].isnull()==True)]
                        started_list1.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(1,15):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        started=df1[(df1['lat_%s' %i].isnull()==False) & (df1['lat_%s' %(i+1)].isnull()==True)]
                        started_list1.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        started_df1= pd.DataFrame()
        for item in started_list1:
            started_df1 =  started_df1.append(item, ignore_index=True)
        started_df1.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\{}_{}hour_part1.csv'.format(day,hour),index=False)
#16-30 minutes dataset
        try:
            df2_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part1.csv'.format(day,hour))
            df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part2.csv'.format(day,hour))
            df2__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part3.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        started_list2=[]
        if((df2['bike_id'].isin(df2_['bike_id']).any()) & (df2['bike_id'].isin(df2__['bike_id']).any())):
            for i in range(17,29):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        started=df2[(df2['lat_%s' %i].isnull()==False) & (df2['lat_%s' %(i+1)].isnull()==True)]
                        started_list2.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df2['bike_id'].isin(df2_['bike_id']).any()):
            for i in range(17,30):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        started=df2[(df2['lat_%s' %i].isnull()==False) & (df2['lat_%s' %(i+1)].isnull()==True)]
                        started_list2.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif(df2['bike_id'].isin(df2__['bike_id']).any()):
            for i in range(16,29):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        started=df2[(df2['lat_%s' %i].isnull()==False) & (df2['lat_%s' %(i+1)].isnull()==True)]
                        started_list2.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(16,30):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        started=df2[(df2['lat_%s' %i].isnull()==False) & (df2['lat_%s' %(i+1)].isnull()==True)]
                        started_list2.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        started_df2= pd.DataFrame()
        for item in started_list2:
            started_df2 =  started_df2.append(item, ignore_index=True)
        started_df2.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\{}_{}hour_part2.csv'.format(day,hour),index=False)
#31-45 minutes dataset
        try:
            df3_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part2.csv'.format(day,hour))
            df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part3.csv'.format(day,hour))
            df3__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        started_list3=[]
        if((df3['bike_id'].isin(df3_['bike_id']).any()) & (df3['bike_id'].isin(df3__['bike_id']).any())):
            for i in range(32,44):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        started=df3[(df3['lat_%s' %i].isnull()==False) & (df3['lat_%s' %(i+1)].isnull()==True)]
                        started_list3.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df3['bike_id'].isin(df3_['bike_id']).any()):
            for i in range(32,45):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        started=df3[(df3['lat_%s' %i].isnull()==False) & (df3['lat_%s' %(i+1)].isnull()==True)]
                        started_list3.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif(df3['bike_id'].isin(df3__['bike_id']).any()):
            for i in range(31,44):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        started=df3[(df3['lat_%s' %i].isnull()==False) & (df3['lat_%s' %(i+1)].isnull()==True)]
                        started_list3.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(31,45):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        started=df3[(df3['lat_%s' %i].isnull()==False) & (df3['lat_%s' %(i+1)].isnull()==True)]
                        started_list3.append(started)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        started_df3= pd.DataFrame()
        for item in started_list3:
            started_df3 =  started_df3.append(item, ignore_index=True)
        started_df3.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\{}_{}hour_part3.csv'.format(day,hour),index=False)
#46-00 minutes dataset
        try:
            if hour==23:
                df4_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part3.csv'.format(day,hour))
                df4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour))
                df4__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_0hour_part1.csv'.format(day+1))
            else:
                df4_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part3.csv'.format(day,hour))
                df4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part4.csv'.format(day,hour))
                df4__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\{}_{}hour_part1.csv'.format(day,hour+1))
        except FileNotFoundError:
            continue
        started_list4=[]
        if((df4['bike_id'].isin(df4_['bike_id']).any()) & (df4['bike_id'].isin(df4__['bike_id']).any())):
            for i in range(47,59):
                if 'lat_%s' %(i+1) in df4.columns:
                    started=df4[(df4['lat_%s' %i].isnull()==False) & (df4['lat_%s' %(i+1)].isnull()==True)]
                    started_list4.append(started)
        elif (df4['bike_id'].isin(df4_['bike_id']).any()):
            for i in range(47,60):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        started=df4[(df4['lat_%s' %i].isnull()==False) & (df4['lat_%s' %(i+1)].isnull()==True)]
                        started_list4.append(started)
                except:
                    continue
        elif(df4['bike_id'].isin(df4__['bike_id']).any()):
             for i in range(46,59):
                if 'lat_%s' %(i+1) in df4.columns:
                    started=df4[(df4['lat_%s' %i].isnull()==False) & (df4['lat_%s' %(i+1)].isnull()==True)]
                    started_list4.append(started)
        else:
            for i in range(46,60):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        started=df4[(df4['lat_%s' %i].isnull()==False) & (df4['lat_%s' %(i+1)].isnull()==True)]
                        started_list4.append(started)
                except:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
                    continue
        started_df4= pd.DataFrame()
        for item in started_list4:
            started_df4 =  started_df4.append(item, ignore_index=True)
        started_df4.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\{}_{}hour_part4.csv'.format(day,hour),index=False)


# In[23]:


tripStarts(29)


# ## check for file size ( less than 20kb)

# In[24]:


def filteredTripStarts(day):
    for hour in range(0,24): 
        for partID in range(1,5):
            try:
                df= pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\{}_{}hour_part{}.csv'.format(day,hour,partID))
            except:
                continue
            column_num=len(df.columns)
            value_df = df.iloc[:, 1:column_num]
            new_list=[]
            for i in range(len(df)):
                row=value_df.loc[i]
                new_row=row[row.isnull().shift(-3).fillna(False)]
                new_list.append(new_row)

            new_df= pd.DataFrame()
            for item in new_list:
                new_df =  new_df.append(item, ignore_index=True)
            first_column= df.iloc[:, 0]
            #print(new_df)
            try:
                df_all_cols = pd.concat([first_column,new_df], axis = 1)
            except ValueError:
                print(str(hour)+"___"+str(partID))
                continue
            df_all_cols.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\Filtered_starts\{}_{}hour_part{}.csv'.format(day,hour,partID),index=False)


# In[31]:


#for i in range(23,29):
filteredTripStarts(29)


# In[5]:


def addDateTimeStarts(day):
    for hour in range(0,24): 
        for partID in range(1,5):
            try:
                df= pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\Filtered_starts\{}_{}hour_part{}.csv'.format(day,hour,partID))
            except FileNotFoundError:
                continue
            col_names=[]
            datetime_list=[]
            for col in df.columns:
                col_names.append(col)
            unique_col_names=col_names[1:][::3]
            #take only lat_ like names
            #uni_name_count=len(unique_col_names)
            for names in unique_col_names:
                minute=names.split("_")[1]
                date_time=str(day)+":"+str(hour)+":"+str(minute)
                datetime_list.append(date_time)
            #print(datetime_list)

            for item in datetime_list:
                col_common_name=item.split(":")[2]
                item_index=datetime_list.index(item)
                location =int(item_index+1)*4
                column_name="date:time_"+col_common_name
                value=item
                #df['date:time_1']=np.where(df['range_1'].notnull(),'value',np.NaN)
                #print(location)
                try:
                    df.insert(location, column_name, value)
                except ValueError:
                    print("value error in "+ str(day)+"_"+str(hour)+"hour_part"+str(partID)+" file. ->>>>"+str(value))
                    continue
                except IndexError:
                    print("index error in "+ str(day)+"_"+str(hour)+"hour_part"+str(partID)+" file. ->>>>"+str(value))
                    continue
                date_column_name="date:time_"+col_common_name
                range_column_name="range_"+col_common_name
                #df['date:time_1']=np.where(df['range_1'].notnull(),'value',np.NaN)
                df[date_column_name]=np.where(df[range_column_name].notnull(),value,np.NaN)
            df.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\Filtered_starts\WithDateTime\{}_{}hour_part{}_dateAdded.csv'.format(day,hour,partID),index=False)
           # print("added!!!!!!")
        


# In[34]:


addDateTimeStarts(29)


# In[2]:


def keep_first_valid(series):
    first_valid = series.first_valid_index()
    return series.mask(series.index!=first_valid)

def GetTripStartRecords(day):
    for hour in range(0,24):
        for fileID in range(1,5):
            try:
                df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\August\Started\Filtered_starts\WithDateTime\{}_{}hour_part{}_dateAdded.csv'.format(day,hour,fileID))
            except FileNotFoundError:
                continue
            df.drop_duplicates(inplace=True)
            col_set=df.columns[1:]
            #take column names except the first column
            df_new = df.dropna(how='all', subset=col_set)
            df_id=df_new.filter(like='bike_')
            #df_lat.flags.allows_duplicate_labels = False
            df_lat=df_new.filter(like='lat')
            df_lat = df_lat.apply(lambda series: keep_first_valid(series), axis=1)
            df_lat.columns = df_lat.columns.str.replace('lat_.*', 'latitude')
            s = df_lat.stack()
            df_lat_new = s.unstack()
            df_lon=df_new.filter(like='lon')
            df_lon = df_lon.apply(lambda series: keep_first_valid(series), axis=1)
            df_lon.columns = df_lon.columns.str.replace('lon_.*', 'longitude')
            s = df_lon.stack()
            df_lon_new = s.unstack()
            df_range=df_new.filter(like='range')
            df_range = df_range.apply(lambda series: keep_first_valid(series), axis=1)
            df_range.columns = df_range.columns.str.replace('range_.*', 'range')
            s = df_range.stack()
            df_range_new = s.unstack()
            df_datetime=df_new.filter(like='date:time')
            df_datetime = df_datetime.apply(lambda series: keep_first_valid(series), axis=1)
            df_datetime.columns = df_datetime.columns.str.replace('date:time_.*', 'datetime')
            s = df_datetime.stack()
            df_datetime_new = s.unstack()
            df_all = pd.concat([df_id,df_lat_new,df_lon_new,df_range_new,df_datetime_new],axis=1,sort=False)
            df_all.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\{}_{}hour_part{}_final.csv'.format(day,hour,fileID),index=False)


# In[38]:


#for day in range (24,30):
GetTripStartRecords(23)


# In[37]:


def GetHourlyStartTripRecords(day):
    for hour in range(0,24):
        df_list=[]
        for fileID in range(1,5):
            try:
                df =pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\{}_{}hour_part{}_final.csv'.format(day,hour,fileID))
            except FileNotFoundError:
                continue
            df_list.append(df)
        #print(df_list)
        try:
            all_df=pd.concat(df_list,ignore_index=True)
        except ValueError:
            print("value error -> "+str(day)+ " day_"+str(hour)+ " hour") # changed to see the days
            continue
        #print(all_df)
        all_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Hourly\{}_{}.csv'.format(day,hour), index=False)


# In[39]:


for day in range (23,30):
    GetHourlyStartTripRecords(day)


# In[40]:


def HourlyStartTripCounts(day):
    month=8
    year=2022
    tripDate = datetime.datetime(year, month, day)
    file_name=tripDate.strftime("%b %d %Y")
    row_count_list=[]
    hour_list=[]
    for hour in range(0,24):
        try:
            df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Hourly\{}_{}.csv'. format(day,hour))
            row_count=len(df)
            row_count_list.append(row_count)
            hour_list.append(hour)
        except FileNotFoundError:
            print("No file found "+str(hour))

    s1=pd.Series(hour_list, name="hour")
    s2=pd.Series(row_count_list, name="count")
    hourly_count=pd.concat([s1,s2], axis=1)
    #print(tripDate)
    hourly_count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Hourly\hourlyTripCount_{}.csv'.format(file_name), index=False)


# In[41]:


for day in range (23,30):
    HourlyStartTripCounts(day)


# # Stops

# In[154]:


def tripStops(day):
    for hour in range(0,24):  
#1-15 minutes dataset
        try:
            if hour==0:
                df1_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_23hour_part4.csv'.format(day-1))
                #df1_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\September\30_23hour_part4.csv')
                df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part1.csv'.format(day,hour))
                df1__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part2.csv'.format(day,hour))
            else:
                df1_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part4.csv'.format(day,hour-1))
                df1=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part1.csv'.format(day,hour))
                df1__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part2.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        stopped_list1=[]
        if((df1['bike_id'].isin(df1_['bike_id']).any()) & (df1['bike_id'].isin(df1__['bike_id']).any())):
            for i in range(2,14):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        stopped=df1[(df1['lat_%s' %i].isnull()==True) & (df1['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list1.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df1['bike_id'].isin(df1_['bike_id']).any()):
            for i in range(2,15):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        stopped=df1[(df1['lat_%s' %i].isnull()==True) & (df1['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list1.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df1['bike_id'].isin(df1__['bike_id']).any()):
            for i in range(1,14):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        stopped=df1[(df1['lat_%s' %i].isnull()==True) & (df1['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list1.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(1,15):
                try:
                    if 'lat_%s' %(i+1) in df1.columns:
                        stopped=df1[(df1['lat_%s' %i].isnull()==True) & (df1['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list1.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        stopped_df1= pd.DataFrame()
        for item in stopped_list1:
            stopped_df1 =  stopped_df1.append(item, ignore_index=True)
        print(str(hour)+'done!!!')
        stopped_df1.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\{}_{}hour_part1.csv'.format(day,hour),index=False)
#16-30 minutes dataset
        try:
            df2_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part1.csv'.format(day,hour))
            df2=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part2.csv'.format(day,hour))
            df2__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part3.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        stopped_list2=[]
        if((df2['bike_id'].isin(df2_['bike_id']).any()) & (df2['bike_id'].isin(df2__['bike_id']).any())):
            for i in range(17,29):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        stopped=df2[(df2['lat_%s' %i].isnull()==True) & (df2['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list2.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df2['bike_id'].isin(df2_['bike_id']).any()):
            for i in range(17,30):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        stopped=df2[(df2['lat_%s' %i].isnull()==True) & (df2['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list2.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df2['bike_id'].isin(df2__['bike_id']).any()):
            for i in range(16,29):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        stopped=df2[(df2['lat_%s' %i].isnull()==True) & (df2['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list2.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(16,30):
                try:
                    if 'lat_%s' %(i+1) in df2.columns:
                        stopped=df2[(df2['lat_%s' %i].isnull()==True) & (df2['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list2.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        stopped_df2= pd.DataFrame()
        for item in stopped_list2:
            stopped_df2 =  stopped_df2.append(item, ignore_index=True)
        stopped_df2.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\{}_{}hour_part2.csv'.format(day,hour),index=False)
#31-45 minutes dataset
        try:
            df3_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part2.csv'.format(day,hour))
            df3=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part3.csv'.format(day,hour))
            df3__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part4.csv'.format(day,hour))
        except FileNotFoundError:
            continue
        stopped_list3=[]
        if((df3['bike_id'].isin(df3_['bike_id']).any()) & (df3['bike_id'].isin(df3__['bike_id']).any())):
            for i in range(32,44):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        stopped=df3[(df3['lat_%s' %i].isnull()==True) & (df3['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list3.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df3['bike_id'].isin(df3_['bike_id']).any()):
            for i in range(32,45):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        stopped=df3[(df3['lat_%s' %i].isnull()==True) & (df3['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list3.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        elif (df3['bike_id'].isin(df3__['bike_id']).any()):
            for i in range(31,44):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        stopped=df3[(df3['lat_%s' %i].isnull()==True) & (df3['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list3.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        else:
            for i in range(31,45):
                try:
                    if 'lat_%s' %(i+1) in df3.columns:
                        stopped=df3[(df3['lat_%s' %i].isnull()==True) & (df3['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list3.append(stopped)
                except KeyError:
                    print("Missing Values: hour "+str(hour)+"_minute "+str(i))
        stopped_df3= pd.DataFrame()
        for item in stopped_list3:
            stopped_df3 =  stopped_df3.append(item, ignore_index=True)
        stopped_df3.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\{}_{}hour_part3.csv'.format(day,hour),index=False)
#46-00 minutes dataset
        try:
            if hour==23:
                df4_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part3.csv'.format(day,hour))
                df4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part4.csv'.format(day,hour))
                df4__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_0hour_part1.csv'.format(day+1))
            else:
                df4_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part3.csv'.format(day,hour))
                df4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part4.csv'.format(day,hour))
                df4__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\{}_{}hour_part1.csv'.format(day,hour+1))
        except FileNotFoundError:
            continue
        stopped_list4=[]
        if((df4['bike_id'].isin(df4_['bike_id']).any()) & (df4['bike_id'].isin(df4__['bike_id']).any())):
            for i in range(47,59):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list4.append(stopped)
                except:
                    continue
        elif (df4['bike_id'].isin(df4_['bike_id']).any()):
            for i in range(47,60):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list4.append(stopped)
                except:
                    continue
        elif (df4['bike_id'].isin(df4__['bike_id']).any()):
            for i in range(46,59):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list4.append(stopped)
                except:
                        continue
        else:
            for i in range(46,60):
                try:
                    if 'lat_%s' %(i+1) in df4.columns:
                        stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                        stopped_list4.append(stopped)
                except:
                    continue
        stopped_df4= pd.DataFrame()
        for item in stopped_list4:
            stopped_df4 =  stopped_df4.append(item, ignore_index=True)
        stopped_df4.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\{}_{}hour_part4.csv'.format(day,hour),index=False)


# In[155]:


tripStops(2)


# In[24]:


for day in range (2,31):
    tripStops(day)


# In[ ]:


#below code only for a new month


# In[26]:


df4_=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\September\30_23hour_part3.csv')
df4=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\September\30_23hour_part4.csv')
df4__=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\1_0hour_part1.csv')
stopped_list4=[]
if((df4['bike_id'].isin(df4_['bike_id']).any()) & (df4['bike_id'].isin(df4__['bike_id']).any())):
    for i in range(47,59):
        if 'lat_%s' %(i+1) in df4.columns:
            stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
            stopped_list4.append(stopped)
elif (df4['bike_id'].isin(df4_['bike_id']).any()):
    for i in range(47,60):
        try:
            if 'lat_%s' %(i+1) in df4.columns:
                stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                stopped_list4.append(stopped)
        except:
            continue
elif (df4['bike_id'].isin(df4__['bike_id']).any()):
    for i in range(46,59):
        if 'lat_%s' %(i+1) in df4.columns:
            stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
            stopped_list4.append(stopped)
else:
    for i in range(46,60):
        try:
            if 'lat_%s' %(i+1) in df4.columns:
                stopped=df4[(df4['lat_%s' %i].isnull()==True) & (df4['lat_%s' %(i+1)].isnull()==False)]
                stopped_list4.append(stopped)
        except:
            continue
stopped_df4= pd.DataFrame()
for item in stopped_list4:
    stopped_df4 =  stopped_df4.append(item, ignore_index=True)
    stopped_df4.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\September\Stopped\31_23hour_part4.csv',index=False)


# In[142]:


def filteredTripStops(day):
    for hour in range(0,24): 
        for fileID in range(1,5):
            try:
                df= pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\{}_{}hour_part{}.csv'.format(day,hour,fileID))
            except:
                continue
            if not df.empty:
                Column_num=len(df.columns)
                value_df = df.iloc[:, 1:Column_num]
                new_list=[]

                for i in range((len(df)-1),-1,-1):
                    row=value_df.loc[i]
                    new_row=row[row.isnull().shift(3).fillna(False)]
                    new_list.append(new_row)

                new_df= pd.DataFrame(new_list)

                first_column= df.iloc[:, 0]
                rvs_first_column =first_column[::-1].reset_index(drop=True)
                df_all_cols = pd.concat([rvs_first_column,new_df], axis = 1)
                #print(df_all_cols)
                df_all_cols.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\Filtered_stops\{}_{}hour_part{}.csv'.format(day,hour,fileID),index=False)


# In[143]:


filteredTripStops(1)


# In[111]:


for day in range (1,31):
    filteredTripStops(day)


# In[144]:


def addDateTimeStops(day):
    for hour in range(0,24): 
        for partID in range(1,5):
            try:
                df= pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\Filtered_stops\{}_{}hour_part{}.csv'.format(day,hour,partID))
            except FileNotFoundError:
                continue
            col_names=[]
            datetime_list=[]
            for col in df.columns:
                col_names.append(col)
            unique_col_names=col_names[1:][::3]
            
            #take only lat_ like names
            #uni_name_count=len(unique_col_names)
            for names in unique_col_names:
                minute=names.split("_")[1]
                date_time=str(day)+":"+str(hour)+":"+str(minute)
                datetime_list.append(date_time)
            #print(datetime_list)

            for item in datetime_list:
                col_common_name=item.split(":")[2]
                item_index=datetime_list.index(item)
                location =int(item_index+1)*4
                column_name="date:time_"+col_common_name
                value=item
    #check type of value and make it string, not date time
                #df['date:time_1']=np.where(df['range_1'].notnull(),'value',np.NaN)
                #print(location)
                try:
                    df.insert(location, column_name, value)
                except ValueError:
                    print("value error in "+ str(day)+"_"+str(hour)+"hour_part"+str(partID)+" file. ->>>>"+str(value))
                    continue
                except IndexError:
                    print("index error in "+ str(day)+"_"+str(hour)+"hour_part"+str(partID)+" file. ->>>>"+str(value))
                    continue
                date_column_name="date:time_"+col_common_name
                range_column_name="range_"+col_common_name
                #df['date:time_1']=np.where(df['range_1'].notnull(),'value',np.NaN)
                df[date_column_name]=np.where(df[range_column_name].notnull(),str(value),np.NaN)
                ### change value to str in the above line. If breaks, remove str and keep just value
            df.to_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\Filtered_stops\WithDateTime\{}_{}hour_part{}_dateAdded.csv'.format(day,hour,partID),index=False)
           # print("added!!!!!!")
        


# In[145]:


addDateTimeStops(1)


# In[115]:


for day in range(1,32):
    addDateTimeStops(day)


# In[146]:


def keep_first_valid(series):
    first_valid = series.first_valid_index()
    return series.mask(series.index!=first_valid)

def GetTripStopRecords(day):
    for hour in range(0,24):
        for fileID in range(1,5):
            try:
                df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\Results\October\Stopped\Filtered_stops\WithDateTime\{}_{}hour_part{}_dateAdded.csv'.format(day,hour,fileID))
            except FileNotFoundError:
                continue
            df.drop_duplicates(inplace=True)
            col_set=df.columns[1:]
            #take column names except the first column
            df_new = df.dropna(how='all', subset=col_set)
            df_id=df_new.filter(like='bike_')
            #df_lat.flags.allows_duplicate_labels = False
            df_lat=df_new.filter(like='lat')
            df_lat = df_lat.apply(lambda series: keep_first_valid(series), axis=1)
            df_lat.columns = df_lat.columns.str.replace('lat_.*', 'latitude')
            s = df_lat.stack()
            df_lat_new = s.unstack()
            df_lon=df_new.filter(like='lon')
            df_lon = df_lon.apply(lambda series: keep_first_valid(series), axis=1)
            df_lon.columns = df_lon.columns.str.replace('lon_.*', 'longitude')
            s = df_lon.stack()
            df_lon_new = s.unstack()
            df_range=df_new.filter(like='range')
            df_range = df_range.apply(lambda series: keep_first_valid(series), axis=1)
            df_range.columns = df_range.columns.str.replace('range_.*', 'range')
            s = df_range.stack()
            df_range_new = s.unstack()
            df_datetime=df_new.filter(like='date:time')
            df_datetime = df_datetime.apply(lambda series: keep_first_valid(series), axis=1)
            df_datetime.columns = df_datetime.columns.str.replace('date:time_.*', 'datetime')
            s = df_datetime.stack()
            df_datetime_new = s.unstack()
            df_all = pd.concat([df_id,df_lat_new,df_lon_new,df_range_new,df_datetime_new],axis=1,sort=False)
            df_all.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\{}_{}hour_part{}_final.csv'.format(day,hour,fileID),index=False)


# In[147]:


GetTripStopRecords(1)


# In[124]:


for day in range (1,31):
    GetTripStopRecords(day)


# In[4]:


def GetHourlyStopTripRecords(day):
    for hour in range(0,24):
        df_list=[]
        for fileID in range(1,5):
            try:
                df =pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\{}_{}hour_part{}_final.csv'.format(day,hour,fileID))
            except FileNotFoundError:
                continue
            df_list.append(df)
        #print(df_list)
        try:
            all_df=pd.concat(df_list,ignore_index=True)
        except ValueError:
            print(str(day)+" -> value error -> "+str(hour)+ " hour")
            continue
        #print(all_df)
        all_df.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\October\Stopped\Hourly\{}_{}.csv'.format(day,hour), index=False)


# In[6]:


for day in range (1,31):
    GetHourlyStopTripRecords(day)


# In[99]:


def HourlyStopTripCounts(day):
    month=8
    year=2022
    tripDate = datetime.datetime(year, month, day)
    file_name=tripDate.strftime("%b %d %Y")
    row_count_list=[]
    hour_list=[]
    for hour in range(0,24):
        try:
            df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\{}_{}.csv'. format(day,hour))
            row_count=len(df)
            row_count_list.append(row_count)
            hour_list.append(hour)
        except FileNotFoundError:
            print("No file found "+str(hour))

    s1=pd.Series(hour_list, name="hour")
    s2=pd.Series(row_count_list, name="count")
    hourly_count=pd.concat([s1,s2], axis=1)
    #print(tripDate)
    hourly_count.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Stopped\Hourly\hourlyTripCount_{}.csv'.format(file_name), index=False)


# In[101]:


for day in range (8,23):
    HourlyStopTripCounts(day)


# In[ ]:


df_hour_list=[]
for hour in range (0,24):
    try:
        df=pd.read_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\Hourly\8_{}.csv'.format(hour))
    except FileNotFoundError:
        continue
    df_hour_list.append(df)
df_day_ = pd.concat(df_hour_list, axis=0).reset_index()
df_day_.to_csv(r'C:\Melbourne_Escooter\RealDataset\FinalResults\August\Started\PerDay\8\AllHours.csv',index=False)

