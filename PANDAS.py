#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


df=pd.read_csv("CardioGoodFitness-1.csv")


# In[3]:


df.head()


# In[4]:


df.head(10)


# In[5]:


df.tail()


# In[6]:


df.tail(10)


# In[7]:


df.shape df.info


# In[ ]:


df.columns


# In[ ]:


df.dtypes


# In[ ]:


df.info()


# In[ ]:


df.isnull().sum()


# In[ ]:


df.describe


# In[ ]:


df.describe()


# In[ ]:


df.describe(include="all")


# In[ ]:




