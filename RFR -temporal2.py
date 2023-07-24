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


# In[75]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\2. Stopped Exploratory Analysis\dataset\df -models\staticDF-weekend-19_23.csv')


# In[76]:


df.isna().sum()


# In[77]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[78]:


scale= StandardScaler()


# In[79]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[80]:


df.columns


# In[81]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[82]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[83]:


model = RandomForestRegressor(n_estimators=41, criterion="squared_error", min_samples_leaf=16, min_samples_split=26, max_depth=40, max_features=1.0)


# In[84]:


LL_rf=model.fit(X_train, y_train)


# In[85]:


score = LL_rf.score(X_train, y_train)
score


# In[86]:


ypred = LL_rf.predict(X_test)


# In[87]:


test_score=LL_rf.score(X_test, y_test)
test_score


# In[88]:


mae =mean_absolute_error(y_test, ypred)
mae


# In[89]:


mse =mean_squared_error(y_test, ypred)
mse


# In[90]:


rmse=np.sqrt(mse)
rmse


# In[91]:


mape =mean_absolute_percentage_error(y_test, ypred)
mape


# In[18]:


from sklearn.pipeline import Pipeline


# In[92]:


feature_list=list(X.columns)
feature_importance = pd.Series(LL_rf.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_importance)


# In[ ]:




