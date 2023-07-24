#!/usr/bin/env python
# coding: utf-8

# In[89]:


import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error,mean_squared_error, accuracy_score,f1_score,mean_absolute_percentage_error


# In[90]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv')


# In[91]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[92]:


scale= StandardScaler()


# In[94]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[95]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[96]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[97]:


print(X_train.shape)


# In[41]:


X_test


# In[16]:


print(X_test.shape)


# In[98]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[99]:


model=Sequential()


# In[100]:


model.add(Dense(units=8, input_dim=22,kernel_initializer='normal',activation='relu'))


# In[101]:


model.add(Dense(units=8, kernel_initializer='normal',activation='tanh'))


# In[102]:


model.add(Dense(1, kernel_initializer='normal'))


# In[103]:


model.compile(loss='mean_squared_error', optimizer='adam')


# In[104]:


model.fit(X_train, y_train, batch_size=25, epochs=20, verbose=1)


# In[73]:


def FunctionFindBestParams(X_train, y_train, X_test, y_test):
    batch_size_list=[10,15,20,25,30]
    epoch_list=[10,15,20,25,30,40]
    
    import pandas as pd
    SearchResultsData=pd.DataFrame(columns=['TrialNumber', 'Parameters', 'MAE'])
    
    TrailNum=0
    for batch_size_trial in batch_size_list:
        for epoch_trial in epoch_list:
            TrailNum+=1
            model=Sequential()
            model.add(Dense(units=10, input_dim=22,kernel_initializer='normal',activation='relu'))
            model.add(Dense(units=10, kernel_initializer='normal',activation='relu'))
            model.add(Dense(1, kernel_initializer='normal'))
            model.compile(loss='mean_squared_error', optimizer='adam')
            model.fit(X_train, y_train, batch_size=10, epochs=10, verbose=0)
            #y_test=y_test.flatten()
            MAPE = np.mean(np.abs(y_test-model.predict(X_test).flatten()))
            print(TrailNum, 'Parameters:','batch_size:', batch_size_trial,'-', 'epochs:',epoch_trial, 'MAE:', MAPE)
            SearchResultsData=SearchResultsData.append(pd.DataFrame(data=[[TrailNum, str(batch_size_trial)+'-'+str(epoch_trial), MAPE]],columns=['TrialNumber', 'Parameters', 'MAE'] ))
    return(SearchResultsData)


# In[74]:


ResultsData=FunctionFindBestParams(X_train, y_train, X_test, y_test)


#df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred})


# In[75]:


get_ipython().run_line_magic('matplotlib', 'inline')
ResultsData.plot(x='Parameters', y='MAE', figsize=(15,4), kind='line')


# In[ ]:


#calculate errors


# In[47]:


y_test=y_test.to_numpy()


# In[106]:


y_pred=model.predict(X_test)


# In[107]:


mae =mean_absolute_error(y_test, y_pred)
mae


# In[108]:


mse=mean_squared_error(y_pred, y_test)
mse


# In[109]:


rmse=np.sqrt(mse)
rmse


# In[110]:


mape =mean_absolute_percentage_error(y_test, model.predict(X_test))
mape


# In[52]:



from sklearn.metrics import r2_score
print("r2 test %f" %r2_score(y_test,model.predict(X_test)))


# In[ ]:





# In[59]:


#Predictions=model.predict(X_test)


# In[ ]:


#find coficient values


# In[158]:


arr=model.get_weights()
features_weights=arr[0]


# In[159]:


m_0=np.mean(features_weights[0])
m_0


# In[160]:


for i in range(0,24):
    print(np.mean(features_weights[i]))


# In[ ]:




