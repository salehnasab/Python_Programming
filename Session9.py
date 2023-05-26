#!/usr/bin/env python
# coding: utf-8

# In[1]:


D=dict([('apple','red'),('grapes','green')])


# In[2]:


print(D)


# In[3]:


D


# In[4]:


D['apple']


# In[5]:


D['grapes']


# In[6]:


D['mango']


# In[7]:


D['grapes']='purple'


# In[8]:


D


# In[9]:


len(D)


# In[10]:


for K in D:
    print(K)


# In[11]:


K=D.keys()


# In[12]:


K


# In[13]:


for i in K:
    print(i)


# In[14]:


V=D.values()


# In[15]:


V


# In[16]:


K


# In[17]:


for i in V:
    print(i)


# In[18]:


for K,V in D.items():
    print(K,V)


# In[19]:


'apple' in D


# In[20]:


'grapes' in D


# In[21]:


'grapes' not in D


# In[22]:


K='apple'
V=D[K]
print(V)


# In[23]:


D


# In[24]:


D.get(K)


# In[25]:


D.get('apple')


# In[26]:


D.get('apple','blue')


# In[27]:


D.get('mango','blue')


# In[35]:


D={'apple':'red','mango':'green',   'banana':'yellow','grapes':'green'}


# In[38]:


D


# In[37]:


V='green'
for K in D:
    if D[K]==V:
        print(K)
        


# In[39]:


D=dict([('apple','red'),('grapes','green')])


# In[40]:


D


# In[41]:


'mango' in D


# In[42]:


D['mango']='yellow'


# In[43]:


D


# In[44]:


D.setdefault('orange','yellow')


# In[45]:


D


# In[46]:


del D['orange']


# In[47]:


D


# In[48]:


D.popitem()


# In[49]:


D


# In[50]:


D.popitem()


# In[51]:


D


# In[52]:


D=dict([('apple','red'),('grapes','green')])


# In[ ]:




