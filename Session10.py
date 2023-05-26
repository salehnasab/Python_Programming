#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hi():
    print("Hello World")


# In[2]:


hi()


# In[3]:


hi()


# In[4]:


def hi():
    print("Heya!")


# In[5]:


hi()


# In[6]:


def hi():
    print("Hello World")


# In[7]:


greeting=hi


# In[8]:


greeting()


# In[9]:


def f(a,b,c=2,d=3):
    print(a,b,c,d)


# In[10]:


f(10,20,30,40)


# In[11]:


f(10,20,30)


# In[12]:


f(10,20)


# In[13]:


f(10)


# In[14]:


f(10,20,d=30)


# In[ ]:


def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0: return False    
    return True
n = int(input("Enter a positive integer: "))
if isPrime(n):
    print("Prime")
else:
    print("Composite")


# In[18]:


def isPrime(n):
    for i in range(2,int(n/2)+1):
        if n%i==0: return False    
    return True
n = int(input("Enter a positive integer: "))
if isPrime(n):
    print("Prime")
else:
    print("Composite")


# In[ ]:




