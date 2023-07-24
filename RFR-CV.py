#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold
from sklearn.metrics import mean_absolute_error,mean_squared_error, accuracy_score,mean_absolute_percentage_error


# In[45]:


df=pd.read_csv(r'C:\SA similarity\Trips\3-months SA wise\df -models\staticDF-6_10.csv')


# In[40]:


df


# In[4]:


#descrip=df.describe()


# In[5]:


#descrip.to_csv(r'C:\features35SA\DF_to_models\description.csv')


# In[3]:


df.isna().sum()


# In[7]:


#df=df.dropna()


# In[8]:


# save and rename the NA dropped stat_dynamic feture file
#df.to_csv(r'C:\features35SA\DF_to_models\Final Datasets\static_dynamic_noNA.csv')


# In[ ]:





# In[46]:


column=['SA1_CODE21', ]
df=df.drop(column, axis=1)


# In[47]:


scale= StandardScaler()


# In[48]:


df_sc= scale.fit_transform(df)
df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[49]:


y=df_sc['total_trip_density']
X=df_sc.drop(['total_trip_density'], axis=1)


# In[50]:



#n_estimators': 402, 'min_sample_leaf': 18, 'min_sample_split': 36, 'max_features': 1.0, 'max_depth': 21
model = RandomForestRegressor(n_estimators=223, criterion="squared_error", min_samples_leaf=6, min_samples_split=4, max_depth=40, max_features=1.0)

#model = RandomForestRegressor()


# In[51]:


scores = cross_validate(model, X, y, cv=5,scoring=('r2', 'neg_mean_absolute_error','neg_mean_squared_error', 'neg_root_mean_squared_error','neg_mean_absolute_percentage_error'),return_train_score=True)


# In[52]:


print(scores['test_neg_mean_squared_error'])
print("%0.2f MSE with a STD of %0.2f" % (scores['test_neg_mean_squared_error'].mean(), scores['test_neg_mean_squared_error'].std()))


# In[53]:


print(scores['test_neg_root_mean_squared_error'])
print("%0.2f RMSE with a STD of %0.2f" % (scores['test_neg_root_mean_squared_error'].mean(), scores['test_neg_root_mean_squared_error'].std()))


# In[54]:


print(scores['test_neg_mean_absolute_error'])
print("%0.2f MAE with a STD of %0.2f" % (scores['test_neg_mean_absolute_error'].mean(), scores['test_neg_mean_absolute_error'].std()))


# In[55]:


print(scores['test_neg_mean_absolute_percentage_error'])
print("%0.2f MAPE with a STD of %0.2f" % (scores['test_neg_mean_absolute_percentage_error'].mean(), scores['test_neg_mean_absolute_percentage_error'].std()))


# In[15]:


from sklearn.pipeline import Pipeline


# In[16]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=24)


# In[17]:


LL_rf=model.fit(X_train, y_train)


# In[18]:


feature_list=list(X.columns)
feature_importance = pd.Series(LL_rf.feature_importances_, index=feature_list).sort_values(ascending=False)
print(feature_importance)


# ###### 
