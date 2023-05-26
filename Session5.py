#!/usr/bin/env python
# coding: utf-8

# In[1]:


n=int(input("Enter a positive integer: "))
i=1
while i<=n:
    print(i)
    i=i+1


# In[6]:


lim=int(input("Enter the limit: "))

for n in range(2,lim+1,1):
    i=2
    while i<=n/2:
        if n%i==0:
            break
        i=i+1
    else:
        print(n)


# In[8]:


n=int(input("Enter an integer: "))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("The sum is:",sum)


# In[10]:


n=int(input("Enter an integer: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
print("The sum is:",sum)


# In[11]:


n=int(input("Enter an integer: "))
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n//=10
print("The reverse is:",reverse)


# In[ ]:




