#!/usr/bin/env python
# coding: utf-8

# In[ ]:


L=list([])
T=tuple([])
S=set([])


# In[1]:


S=set([1,2,3,4,5])


# In[2]:


S


# In[3]:


L=list([1,2,3,4,5,6])
T=tuple([1,2,3,4,5,6])


# In[5]:


L


# In[6]:


T


# In[7]:


S


# In[8]:


L[3]


# In[9]:


T[3]


# In[10]:


S=set(range(1,6))


# In[11]:


S


# In[12]:


S=set([1,2,3,4,5])


# In[13]:


S


# In[14]:


for i in S:
    print(i)


# In[15]:


2 in S


# In[16]:


S 


# In[17]:


9 in S


# In[18]:


9 not in S


# In[19]:


S


# In[20]:


S.add(5)


# In[21]:


S


# In[22]:


S.add(9)


# In[23]:


S


# In[14]:


S1={2,4,6,8}
S2={1,3,5,7}
S1.update(S2)


# In[25]:


S1


# In[3]:


S1


# In[4]:


S1.pop()


# In[5]:


S1


# In[6]:


S1.pop()


# In[7]:


S1


# In[9]:


S1


# In[10]:


S1.remove(5)


# In[11]:


S1


# In[12]:


S1.remove(7)


# In[13]:


S1


# In[15]:


S1


# In[16]:


S1.discard(9)


# In[17]:


S1


# In[18]:


S1.remove(9)


# In[19]:


S1


# In[24]:


S1.discard(5)


# In[25]:


S1


# In[26]:


S1.clear()


# In[27]:


S1


# In[28]:


S1={1,2}


# In[29]:


S2=S1.copy()


# In[30]:


S2


# In[31]:


S3=S1


# In[32]:


S3


# In[33]:


S1={1,2}
S2={2,3}


# In[34]:


S1.union(S2) # = S1|S2


# In[35]:


S1|S2


# In[36]:


{1,2}.union({2,3})


# In[37]:


{1,2}|{2,3}


# In[38]:


S1.update(S2)


# In[39]:


S1


# In[46]:


S1={1,2}
S2={2,3}


# In[42]:


S1.intersection(S2)


# In[43]:


S1 & S2


# In[44]:


{1,2,3}.intersection({2,3,4},{1,3,5})


# In[45]:


{1,2,3}& {2,3,4} & {1,3,5}


# In[47]:


S1={1,2}
S2={2,3}


# In[48]:


S1.difference(S2)


# In[49]:


S1-S2


# In[50]:


S1={1,2}
S2={2,3}


# In[51]:


S1.symmetric_difference(S2)


# In[52]:


S1.symmetric_difference_update(S2)


# In[53]:


S1


# In[56]:


S1={1,2}
S2={2,3}
S3={3,4}


# In[55]:


S1.isdisjoint(S2)


# In[57]:


S1.isdisjoint(S3)


# In[58]:


S2.isdisjoint(S3)


# In[59]:


S1={1,2}
S2={1,2,3}


# In[60]:


S1.issubset(S2)


# In[61]:


S1<=S2


# In[62]:


S1.issuperset(S2)


# In[63]:


S2.issuperset(S1)


# In[64]:


S2>=S1


# In[ ]:




