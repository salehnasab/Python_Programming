#!/usr/bin/env python
# coding: utf-8

# In[1]:


L=list([5,2,3])


# In[2]:


L


# In[3]:


L[0]


# In[4]:


L[1]


# In[5]:


L[3]


# In[6]:


L[2]


# In[7]:


len(L)


# In[8]:


L


# In[9]:


for i in L:
    print(i)


# In[10]:


L=[2,3,4,5,1,0,4,5,6,7]


# In[11]:


for i in L:
    print(i)


# In[12]:


L=[5,2,3]


# In[13]:


5 in L


# In[14]:


4 in L


# In[15]:


4 not in L


# In[16]:


L=[5,2,3,2]


# In[17]:


len(L)


# In[18]:


L.count(5)


# In[19]:


L.count(2)


# In[20]:


L.count(4)


# In[21]:


L


# In[22]:


L.index(2)


# In[23]:


L.index(4)


# In[24]:


L


# In[25]:


L.index(2,2)


# In[26]:


L.index(3,0,2)


# In[27]:


L.index(3,0,3)


# In[28]:


L


# In[29]:


L[1:3]


# In[30]:


L[1:]


# In[31]:


L[:3]


# In[32]:


L[:4]


# In[33]:


L


# In[34]:


L[:]


# In[35]:


L[1:3]=[3,0,0,2]


# In[36]:


L


# In[37]:


L=[5, 2, 3, 2] equal L=list([5,2,3,2])


# In[38]:


L=[5, 2, 3, 2]


# In[39]:


L


# In[40]:


L.append(4)


# In[41]:


L


# In[42]:


L[len(L):]=[6]


# In[43]:


L


# In[44]:


L[len(L):]=[6,4,5,4,3]


# In[45]:


L


# In[46]:


L1=[5,2,3]
L2=[7,8,9]


# In[47]:


L1


# In[48]:


L2


# In[49]:


L1.extend(L2)


# In[50]:


L1


# In[51]:


L=[5,2,3]


# In[52]:


L.insert(2,9)


# In[53]:


L


# In[54]:


L=[5,2,3,7,8,9]


# In[55]:


L1=[5,2,3]


# In[56]:


del L[0]


# In[57]:


L


# In[58]:


L1


# In[59]:


del L1[0]


# In[60]:


L1


# In[61]:


del L1


# In[62]:


L1


# In[63]:


L=[5,2,3,2]


# In[64]:


L.remove(2)


# In[65]:


L


# In[66]:


L.remove(2)


# In[67]:


L


# In[68]:


L1=[1,2,3]
L2=[4,5,6]
L3=L1+L2


# In[69]:


L1


# In[70]:


L2


# In[71]:


L3


# In[72]:


L


# In[73]:


L=[5,2,3]


# In[74]:


L*3


# In[75]:


L*5


# In[76]:


L1


# In[77]:


L2=L1


# In[78]:


L2


# In[79]:


L1=[5,2,3]


# In[80]:


L2=L1.copy()


# In[81]:


L2


# In[82]:


min(L2)


# In[83]:


max(L2)


# In[84]:


L2.reverse()


# In[85]:


L2


# In[86]:


L=[5,2,3]


# In[87]:


L


# In[88]:


L.sort()


# In[89]:


L


# In[90]:


L.sort(reverse=True)


# In[91]:


L


# In[92]:


L=[5,2,3]


# In[93]:


L


# In[94]:


L.sort(reverse=True)


# In[95]:


L


# In[96]:


L1=[1,2,3]
L2=[4,5]
L3=[6,7,8,9]
L=[0,L1,L2,L3,100]


# In[97]:


L


# In[98]:


type(L)


# In[ ]:




