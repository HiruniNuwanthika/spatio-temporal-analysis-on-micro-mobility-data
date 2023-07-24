#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

from sklearn.metrics import mean_absolute_error,mean_squared_error, accuracy_score,mean_absolute_percentage_error


# In[3]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\df -models\staticDF-weekend-6_10.csv')


# In[4]:


df.isna().sum()


# In[5]:


df=df.dropna() #drop 96 records without pedestrian count


# In[6]:


df


# In[7]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[8]:


scale= StandardScaler()


# In[9]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[10]:


df.columns

#print(len(df.columns)) = 33


# In[11]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[13]:


print("max=",y_test.max() )
print("min=",y_test.min() )
print("mean=",y_test.mean() )
print("std=",np.sqrt(y_test.mean()) )


# In[14]:


model = RandomForestRegressor(n_estimators=419, criterion="squared_error", min_samples_leaf=19, min_samples_split=17, max_depth=24, max_features=1.0)


# In[15]:


LL_rf=model.fit(X_train, y_train)


# In[16]:


score = LL_rf.score(X_train, y_train)
score


# In[17]:


ypred = LL_rf.predict(X_test)


# In[18]:


test_score=LL_rf.score(X_test, y_test)
test_score


# In[19]:


mae =mean_absolute_error(y_test, ypred)
mae


# In[20]:


mse =mean_squared_error(y_test, ypred)
mse


# In[21]:


rmse=np.sqrt(mse)
rmse


# In[22]:


mape =mean_absolute_percentage_error(y_test, ypred)
mape


# In[23]:


from sklearn.pipeline import Pipeline


# In[24]:


feature_list=list(X.columns)
feature_importance = pd.Series(LL_rf.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_importance)


# In[29]:


from sklearn.model_selection import RandomizedSearchCV


# In[26]:


param_grid={
    'bootstrap': [True],
    'max_depth': [29,32],
    'max_features': [20,25,30],
    'min_samples_leaf': [12,13,14],
    'min_samples_split': [32,33],
    'max_leaf_nodes':[10,20,30],
    'n_estimators': [500]
}


# In[27]:


rf = RandomForestRegressor()


# In[31]:


grid_search = GridSearchCV(estimator = rf, param_grid = param_grid, cv = 5, n_jobs = -1, verbose = 2)
#grid=RandomizedSearchCV(estimator = rf, param_distributions = param_grid, n_iter=num_iterations, cv = 5)


# In[33]:


grid_search.fit(X_train, y_train)
#grid_results=grid.fit(X_train, y_train)


# In[29]:


grid_search.best_params_ 
'''
param_grid={
    'bootstrap': [True],
    'max_depth': [27,28,29],
    'max_features': [10,11,12],
    'min_samples_leaf': [25,26],
    'min_samples_split': [30,31],
    'n_estimators': [800]
}'''


# In[36]:


grid_search.best_params_ 
'''
param_grid={
    'bootstrap': [True],
    'max_depth': [29,32],
    'max_features': [12,15,20],
    'min_samples_leaf': [15,20,23],
    'min_samples_split': [31,32],
    'n_estimators': [800]
}'''


# In[52]:


grid_search.best_params_ 


# In[55]:


grid_search.best_params_ 

'''
param_grid={
    'bootstrap': [True],
    'max_depth': [29,32],
    'max_features': [20,25,30],
    'min_samples_leaf': [12,13,14],
    'min_samples_split': [32,33],
    'n_estimators': [800]
}
'''


# In[ ]:




