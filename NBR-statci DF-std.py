#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from patsy import dmatrices
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error,mean_absolute_percentage_error


# In[17]:


df=pd.read_csv(r'C:\Melbourne_Escooter\Lime\1. Exploratory Analysis\dataset\df -models\staticDF-NBR.csv')


# In[18]:


df.head()


# In[20]:


import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np
#data = np.random.randn(200)
res = sn.kdeplot(df['total_trip_density'])
plt.show()


# In[21]:


mean=df['total_trip_density'].mean()
var=df['total_trip_density'].var()
print('var = '+ str(var)+ ', mean = '+ str(mean))


# In[22]:


column=['SA1_CODE21']
df=df.drop(column, axis=1)


# In[23]:


df.columns


# In[24]:


mask = np.random.rand(len(df)) < 0.8
df_train = df[mask]
df_test = df[~mask]
print('Training data set length='+str(len(df_train)))
print('Testing data set length='+str(len(df_test)))


# In[31]:


#expr = """total_trip_density ~  trainDensity +busDensity+ tramDensity + Cafe perc+ Office perc + Shops perc + entropy + mxi + recreationCount + campusCount + 5-14 % + 15-29 % + 30-39 %"""

expr = """total_trip_density ~  trainDensity +busDensity+ tramDensity + CafePerc + OfficePerc + ShopsPerc + entropy + mxi + recreationCount + campusCount + age5_14 + age15_29 + age30_39 + age40_49 + age50_64 + ageAbove65 + femalePerc + malePerc + PopulationDensity + carOwnerPerc + withoutChildPerc + withChildPerc"""


# In[32]:



y_test, X_test = dmatrices(expr, df_test, return_type='dataframe')
y_train, X_train = dmatrices(expr, df_train, return_type='dataframe')


# In[35]:


poisson_training_results = sm.GLM(y_train, X_train, family=sm.families.Poisson()).fit()


# In[36]:


print(poisson_training_results.summary())


# In[37]:


print(poisson_training_results.mu)
print(len(poisson_training_results.mu))


# In[38]:


import statsmodels.formula.api as smf


# In[39]:


df_train['BB_LAMBDA'] = poisson_training_results.mu


# In[41]:


df_train['AUX_OLS_DEP'] = df_train.apply(lambda x: ((x['total_trip_density'] - x['BB_LAMBDA'])**2 - x['BB_LAMBDA']) / x['BB_LAMBDA'], axis=1)


# In[42]:


ols_expr = """AUX_OLS_DEP ~ BB_LAMBDA - 1""" # -1 is donot fit intercept


# In[43]:


aux_olsr_results = smf.ols(ols_expr, df_train).fit()


# In[44]:


print(aux_olsr_results.params)


# In[45]:


aux_olsr_results.tvalues   #calculated t-value for DF 280 is 1.650314. our t-val is larger than that


# In[46]:


nb2_training_results = sm.GLM(y_train, X_train,family=sm.families.NegativeBinomial(alpha=aux_olsr_results.params[0])).fit()


# In[47]:


print(nb2_training_results.summary())


# In[48]:


nb2_predictions = nb2_training_results.get_prediction(X_test)


# In[49]:


predictions_summary_frame = nb2_predictions.summary_frame()
print(predictions_summary_frame)


# In[50]:


predicted_test_count=predictions_summary_frame['mean']
predicted_test_count


# In[51]:


predicted_counts=predictions_summary_frame['mean']
actual_counts = y_test['total_trip_density']
fig = plt.figure()
fig.suptitle('Predicted versus actual trip density')
predicted, = plt.plot(X_test.index, predicted_counts, 'go-', label='Predicted counts')
actual, = plt.plot(X_test.index, actual_counts, 'ro-', label='Actual counts')
plt.legend(handles=[predicted, actual])
plt.show()


# In[52]:


print("MAE %f" %mean_absolute_error(y_test, predicted_test_count))


# In[53]:


print("MAPE %f" %mean_absolute_percentage_error(y_test, predicted_test_count))


# In[54]:


rmse=np.sqrt(mean_squared_error(y_test, predicted_test_count))
print("RMSE %f" %rmse)


# In[55]:


print("MSE %f" %mean_squared_error(y_test, predicted_test_count))


# In[ ]:




