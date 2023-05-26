#!/usr/bin/env python
# coding: utf-8

# In[1]:


T=tuple([5,2,3])


# In[2]:


T


# In[3]:


L=list([5,2,3])


# In[4]:


L


# In[5]:


T


# In[6]:


L=[5,2,3]
T=(5,2,3)


# In[7]:


T


# In[8]:


T1=tuple()


# In[9]:


T1


# In[10]:


T=(5,2,3)


# In[11]:


T2=()


# In[12]:


T2


# In[13]:


type(T2)


# In[14]:


L2=[]


# In[15]:


type(L2)


# In[16]:


T


# In[17]:


T[0]


# In[18]:


len(T)


# In[19]:


T


# In[20]:


for i in T:
    print(i)


# In[21]:


for i in L:
    print(i)


# In[22]:


3 in L


# In[23]:


3 in T


# In[24]:


T=(5,2,3,2)


# In[25]:


T.count(2)


# In[26]:


T.count(3)


# In[27]:


T.index(3)


# In[28]:


T


# In[29]:


T.index(3)


# In[30]:


T.index(2,2)


# In[31]:


T


# In[32]:


T.index(3,0,2)


# In[33]:


T.index(3,0,3)


# In[34]:


T=(5,2,3,2)


# In[35]:


T[1:3]


# In[36]:


T


# In[37]:


T[:]


# In[38]:


T1=(1,3)


# In[40]:


T2=(7,8)


# In[41]:


T3=T1+T2


# In[42]:


T3


# In[43]:


T=(1,3)


# In[ ]:


T+= equal/means T=T+


# In[44]:


T+=(7,8)


# In[45]:


T


# In[46]:


T=(5,2,3)*3


# In[47]:


T


# In[48]:


x=y=5


# In[49]:


x


# In[50]:


y


# In[51]:


x,y=2,3


# In[52]:


x


# In[53]:


y


# In[54]:


T=(5,2,3)


# In[55]:


min(T)


# In[56]:


max(T)


# In[57]:


T


# In[58]:


L


# In[59]:


L.sort()


# In[60]:


L


# In[61]:


L.sort(reverse=True)


# In[62]:


L


# In[63]:


T


# In[64]:


sorted(T)


# In[65]:


sorted(T,reverse=True)


# In[ ]:




