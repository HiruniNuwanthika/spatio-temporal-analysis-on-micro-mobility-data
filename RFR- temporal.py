#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.metrics import mean_absolute_error,mean_squared_error, accuracy_score,mean_absolute_percentage_error


# In[69]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\TemporalAnalysis\dataset\20604111911.csv')


# In[70]:


column=['MM','DD','HH24']
df=df.drop(column, axis=1)


# In[71]:



df


# In[72]:


df=pd.get_dummies(df,drop_first=True)


# In[73]:


scale= StandardScaler()
df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[74]:


y=df_sc['tripCount']
X=df_sc.drop(['tripCount'], axis=1)


# In[75]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[76]:


model = RandomForestRegressor(n_estimators=200, criterion="squared_error", min_samples_leaf=2, min_samples_split=2, max_depth=19, max_features=1.0)


# In[77]:


LL_rf=model.fit(X_train, y_train)


# In[78]:


score = LL_rf.score(X_train, y_train)
score


# In[79]:


ypred = LL_rf.predict(X_test)


# In[80]:


test_score=LL_rf.score(X_test, y_test)
test_score


# In[81]:


mae =mean_absolute_error(y_test, ypred)
mae


# In[82]:


mse =mean_squared_error(y_test, ypred)
mse


# In[83]:


rmse=np.sqrt(mse)
rmse


# In[84]:


mape =mean_absolute_percentage_error(y_test, ypred)
mape


# In[25]:


from sklearn.pipeline import Pipeline


# In[85]:


feature_list=list(X.columns)
feature_importance = pd.Series(LL_rf.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_importance)


# In[ ]:




