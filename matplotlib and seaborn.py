#!/usr/bin/env python
# coding: utf-8

# In[28]:


import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")


# In[29]:


df=pd.read_csv("World Happiness Report.csv")


# In[30]:


df.sample(5)


# In[31]:


df.shape


# In[32]:


df.describe(include="all")


# In[33]:


df.describe()


# In[34]:


df.describe(include="all")


# In[35]:


df.info()


# In[36]:


df.isnull().sum()


# In[37]:


df.hist(figsize=(20,30))


# In[39]:




pd.crosstab(df['Family'],df['Health'] )


# In[119]:




sns.countplot(x="Economy", hue="Region", data=df)


# In[44]:


plt.hist(x=df["Family"],color='orchid')
plt.title('Happiness')
plt.xlabel('Family')
plt.show()


# In[46]:


plt.boxplot(x=df["Family"])
plt.title('Happiness')
plt.xlabel('Family')
plt.show()


# In[51]:


plt.boxplot([df["Family"],df["Health"]])
plt.title('Happiness')
plt.xlabel('Family')
plt.ylabel("Health")
plt.show()


# In[65]:


df["Region"].value_counts().plot(kind="bar",color="red")
plt.title('Happiness')
plt.xlabel('Region')
plt.ylabel("Count")
plt.show()


# In[64]:


df["Region"].value_counts().plot(kind="barh",color="brown")
plt.title('Happiness')
plt.xlabel('Count')
plt.ylabel("Region")
plt.show()


# In[67]:


plt.bar("Region","Economy",data=df,color="red")
plt.title('Happiness')
c


# In[77]:


pymarks=(50,65,40,35,77)
rmarks=(55,72,94,70,85)

index=np.arange(5)
plt.bar(x=index,height=pymarks,width=0.35,label="Python",color='r')
plt.bar(x=index+0.35,height=rmarks,width=0.35,label='R',color='y')

plt.title('Students')
plt.xlabel('Scores')
plt.ylabel("Scores by students")
plt.xticks(ticks=index+0.35/2,labels=('A','B','C','D','E'))
plt.show()


# In[80]:


pymarks=(50,65,40,35,77)
rmarks=(55,72,94,70,85)

index=np.arange(5)
plt.bar(x=index,height=pymarks,label="Python")
plt.bar(x=index,height=rmarks,bottom=pymarks,label='R')

plt.title('Students')
plt.xlabel('Scores')
plt.ylabel("Scores by students")
plt.xticks(ticks=index,labels=('A','B','C','D','E'))
plt.show()


# In[111]:


freqbyregion=df["Country"].value_counts()
keys=freqbyregion.keys().to_list()
counts=freqbyregion.to_list()

plt.pie(x=counts,labels=keys,autopct='%1.1f%%')
plt.title("Regions")
plt.show


# In[87]:


freqbyregion=df["Region"].value_counts()
keys=freqbyregion.keys().to_list()
counts=freqbyregion.to_list()
mylist=[1,0.1,0.1,0.1,0.1,0.1,0.1]
plt.pie(x=counts,labels=keys,autopct='%1.1f%%',explode=mylist)
plt.title("Regions")
plt.show


# In[97]:


freqbyregion=df["Country"].value_counts()
keys=freqbyregion.keys().to_list()
counts=freqbyregion.to_list()
mylist=[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
plt.pie(x=counts,labels=keys,autopct='%1.1f%%',explode=mylist)
plt.title("Regions")
plt.show


# In[107]:


freqbyreg=df['Region'].value_counts()
keys=freqbyreg.keys().to_list()
counts=freqbyreg.to_list()
plt.pie(x=counts,labels=keys,autopct='%1.1f%%')
circle=plt.Circle(xy=(0,0),radius=0.4,color='white')
plt.gcf()
plt.gca().add_artist(circle)
plt.title("Region wise distribution")
plt.show()


# In[108]:


plt.scatter(x="Family",y="Health",data=df)
plt.title("Scatter plot")
plt.xlabel("Family")
plt.ylabel("Health")
plt.show()


# In[112]:


sns.catplot(x="Economy", y="Family", data=df)


# In[114]:


sns.catplot(x="Economy", y="Family", hue = "Region",data=df) 


# In[117]:


sns.catplot(x="Economy", y="Family", hue = "Region",kind = "violin", data=df)


# In[124]:


sns.catplot(x="Family", y="Economy", hue = "Region", kind = "violin", data=df)


# In[131]:


sns.catplot(x="Family", y="Economy", hue = "Region", kind = "bar", data=df)


# In[132]:



sns.catplot(x="Family", y="Economy", hue = "Region", kind = "point", data=df)


# In[136]:


sns.distplot(df.Economy)


# In[139]:


sns.distplot(df.Economy, kde=False, rug = True)


# In[140]:


sns.jointplot(x=df.Economy, y=df.Family, kind="hex", data = df)


# In[141]:


sns.jointplot(x="Family", y="Economy", data=df, kind="kde");


# In[142]:


corrmat = df.corr()
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(corrmat, vmax=.8, square=True)


# In[144]:


sns.pairplot(df)


# In[ ]:




