#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

import statsmodels.api as sm
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error,mean_absolute_percentage_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score
from math import sqrt


# In[14]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF.csv')


# In[15]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[17]:


scale= StandardScaler()


# In[5]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[18]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[20]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[22]:


from sklearn.svm import SVR
SVM_regression= SVR(kernel='rbf', gamma=0.01, C=5)
scores = cross_validate(SVM_regression, X, y, cv=5,scoring=('r2', 'neg_mean_absolute_error','neg_mean_squared_error', 'neg_root_mean_squared_error','neg_mean_absolute_percentage_error'),return_train_score=True)


# In[23]:


print(scores['test_neg_mean_squared_error'])
print("%0.2f MSE with a STD of %0.2f" % (scores['test_neg_mean_squared_error'].mean(), scores['test_neg_mean_squared_error'].std()))


# In[24]:


print(scores['test_neg_root_mean_squared_error'])
print("%0.2f RMSE with a STD of %0.2f" % (scores['test_neg_root_mean_squared_error'].mean(), scores['test_neg_root_mean_squared_error'].std()))


# In[25]:


print(scores['test_neg_mean_absolute_error'])
print("%0.2f MAE with a STD of %0.2f" % (scores['test_neg_mean_absolute_error'].mean(), scores['test_neg_mean_absolute_error'].std()))


# In[26]:


print(scores['test_neg_mean_absolute_percentage_error'])
print("%0.2f MAPE with a STD of %0.2f" % (scores['test_neg_mean_absolute_percentage_error'].mean(), scores['test_neg_mean_absolute_percentage_error'].std()))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




