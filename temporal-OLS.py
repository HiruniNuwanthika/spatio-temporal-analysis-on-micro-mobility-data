#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error


# In[2]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\TemporalAnalysis\dataset\all3months.csv')


# In[4]:


df.head()


# In[5]:


import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
#data = np.random.randn(200)
res = sn.kdeplot(df['tripCount'])
plt.show()


# In[7]:


mean=df['tripCount'].mean()
var=df['tripCount'].var()
print('var = '+ str(var)+ ', mean = '+ str(mean))


# In[8]:


column=['date','month']
df=df.drop(column, axis=1)


# In[9]:


df


# In[ ]:





# In[ ]:


scale= StandardScaler()


# In[ ]:


#df_sc= scale.fit_transform(df)
#df_sc=pd.DataFrame(df_sc, columns=df.columns)


# In[10]:


y=df['tripCount']
X=df.drop(['tripCount'], axis=1)


# In[11]:


X = pd.get_dummies(data=X, drop_first=True)


# In[25]:


X_train


# In[26]:


X_test


# In[27]:


y_train


# In[28]:


y_test


# In[12]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


# In[17]:


regr = linear_model.LinearRegression()


# In[18]:


regr.fit(X_train, y_train)


# In[19]:


y_pred = regr.predict(X_test)


# In[29]:


y_pred


# In[20]:


print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))


# In[21]:


print("Coefficient of determination: %.2f" % r2_score(y_test, y_pred))


# In[35]:


plt.scatter(y_test, y_pred, color="black")
plt.plot(y_test, y_test, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()


# In[37]:


regr.coef_


# In[ ]:




