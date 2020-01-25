#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
import seaborn as sns

import plotly


# In[11]:


df = pd.read_csv('Life expectancy data.csv')


# In[12]:


df.head()


# In[15]:


df.describe()


# In[18]:


data = df['Adult Mortality']
data.describe()


# In[21]:


sns.set(style="whitegrid")
ax = sns.violinplot(x=df["Adult Mortality"])


# In[22]:


sns.set(style = "whitegrid")
ax = sns.violinplot(x = df["infant deaths"])


# In[ ]:




