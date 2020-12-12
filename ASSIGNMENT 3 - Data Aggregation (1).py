#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Set imports
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
import pymysql


# In[2]:


# PyMySQL
#Create engine and connect


# In[3]:


#Read SQL from a DataFrame
frame = pd.read_sql("SELECT * FROM `vgsales-2016 (1)`;", conn)
print(frame.head())


# In[4]:


#Numeric Description
print(frame.describe())


# In[5]:


#info
print(frame.info())


# In[6]:


#WHERE for finding no. of values for each condition

yearofrelease_greater_df = frame[frame["Year_of_Release"] > 2005]
yearofrelease_less_df = frame[frame["Year_of_Release"] <= 2005]
print(len(yearofrelease_greater_df))
print(len(yearofrelease_less_df))


# In[7]:


#groupby on yearofrelease and mean values for Global_Sales

df_yearofrelease = (frame.groupby(["Year_of_Release"])["Global_Sales"].mean().reset_index())
print(df_yearofrelease)


# In[8]:


#Was the average of global sales higher before or after 2005 ?

#WHERE on grouped Year_of_Release

df_yor_before = df_yearofrelease[df_yearofrelease["Year_of_Release"] < 2005]
print("Mean of Year Of Release before 2005: " + str(df_yor_before.Global_Sales.mean()*100))

df_yor_after = df_yearofrelease[df_yearofrelease["Year_of_Release"] >= 2005]
print("Mean of Year Of Release on and after 2005: " + str(df_yor_after.Global_Sales.mean()*100
                                                         ))

#print(df_yor_before)
#print(df_yor_after)


# ### Hence, average of global sales is higher before 2005 with a value of 139.92, which is approx 96 units greater than the after 2005 value, i.e., 43.93.

# In[9]:


#Create a new column that labels records before 2005 as 'pre-2005' and after 2005 as 'post-2005'

df_yearofrelease.loc[(df_yearofrelease["Year_of_Release"] < 2005), "Status"] = "Pre-2005"
df_yearofrelease.loc[(df_yearofrelease["Year_of_Release"] >= 2005), "Status"] = "Post-2005"
print(df_yearofrelease)


# In[ ]:




