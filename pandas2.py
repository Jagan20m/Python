#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[5]:


import pandas as pd


# In[6]:


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)


# In[7]:


df=pd.read_csv("https://raw.githubusercontent.com/Gokhul12/Datasets/main/auto-mpg.csv")


# In[8]:


df.head()


# In[9]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.describe(include="all")


# In[8]:


df.dtypes


# In[9]:


df.isnull().sum()


# In[10]:


df["horsepower"].value_counts()


# In[11]:


df["horsepower"]=df["horsepower"].replace("?",np.nan)
median1=df["horsepower"].median()
df["horsepower"]=df["horsepower"].replace(np.nan,median1)
df.isnull().sum()


# In[12]:


df["horsepower"].value_counts()


# In[ ]:




