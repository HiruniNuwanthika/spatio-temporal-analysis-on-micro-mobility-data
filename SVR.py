#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import statsmodels.api as sm

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from math import sqrt


# In[18]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv')


# In[19]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[20]:


scale= StandardScaler()


# In[22]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[6]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[23]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[24]:


from sklearn.svm import SVR
SVM_regression= SVR(kernel='rbf', gamma=0.01, C=5)
SVM_regression.fit(X_train, y_train)


# In[25]:


y_pred= SVM_regression.predict(X_test)


# In[26]:


SVM_regression.score(X_test, y_test)


# In[27]:


SVM_regression.score(X_train, y_train)


# In[28]:


mae =mean_absolute_error(y_test, y_pred)
mae


# In[29]:


mse=mean_squared_error(y_pred, y_test)
mse


# In[30]:


rmse=np.sqrt(mse)
rmse


# In[31]:


mape =mean_absolute_percentage_error(y_test, y_pred)
mape


# In[13]:


import numpy as np
rmse=np.sqrt(mse)
rmse


# In[20]:


r2_score(y_test,y_pred)


# In[22]:


mean_absolute_error(y_pred, y_test)


# In[40]:


### GRID search C, gamma and kernel function


# In[9]:


my_param_grid = {'C':[1,5,10,50,100], 'gamma':[1,0.9,0.1,0.01], 'kernel':['rbf']}


# In[10]:


from sklearn.model_selection import GridSearchCV


# In[11]:


GridSearchCV(estimator=SVR(), param_grid=my_param_grid, refit=True, verbose=3, cv=5)


# In[12]:


grid =GridSearchCV(estimator=SVR(), param_grid=my_param_grid, refit=True, verbose=3, cv=5)


# In[14]:


result=grid.fit(X_train, y_train)


# In[16]:


result.best_params_


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




