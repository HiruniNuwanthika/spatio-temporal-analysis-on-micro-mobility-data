#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
#from scikeras.wrappers import KerasClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
#from sklearn.model_selection import cross_validate
#from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error,mean_squared_error, accuracy_score,f1_score,mean_absolute_percentage_error


# In[3]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv')


# In[4]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[12]:


scale= StandardScaler()


# In[13]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[14]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[7]:





# In[15]:


from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


# In[16]:


model=Sequential()


# In[17]:


model.add(Dense(units=8, input_dim=22,kernel_initializer='normal',activation='relu'))


# In[18]:


model.add(Dense(units=8, kernel_initializer='normal',activation='tanh'))


# In[19]:


model.add(Dense(1, kernel_initializer='normal'))


# In[20]:


model.compile(loss='mean_squared_error', optimizer='adam')


# In[24]:


keras_clf = KerasClassifier(model = model, optimizer="adam", epochs=100, verbose=0)

#predictions = cross_val_predict(keras_clf, X_train, y_train, cv=3)

scores = cross_validate(keras_clf, X, y, cv=5,scoring=('r2', 'neg_mean_absolute_error','neg_mean_squared_error', 'neg_root_mean_squared_error','neg_mean_absolute_percentage_error'),return_train_score=True)


# In[ ]:


#calculate errors


# In[47]:


y_test=y_test.to_numpy()


# In[48]:


model.predict(X_test)


# In[49]:



print("MAE %f" %mean_absolute_error(y_test,model.predict(X_test)))


# In[50]:


print("MSE %f" %mean_squared_error(y_test,model.predict(X_test)))


# In[53]:


mse=mean_squared_error(y_test,model.predict(X_test))
rmse=round(np.sqrt(0.352472))
print("RMSE %f" %rmse)


# In[56]:


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




