#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
import numpy as np


# In[64]:


df = pd.read_fwf('C:/aocd1.txt', header = None)


# In[65]:


df.head()


# In[70]:


diff = df[0] - df[0].shift(1)


# In[71]:


print(diff)


# In[73]:


result = sum(i>0 for i in diff)


# In[74]:


print(result)


# In[ ]:




