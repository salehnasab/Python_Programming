#!/usr/bin/env python
# coding: utf-8

# In[2]:


name=input("Enter your name: ")
age = int(input("Enter youe age: "))
print("Hi {}, you are {:d} years old!".format(name,age))


# In[4]:


import math
x = int(input("Enter an integer: "))
print("x={}".format(x));
print("x lies between {} and {}".format(x-1,x+1))
print("square(x)={} cube(x)={}".format(x**2,pow(x,3)))
print("sqrt(x)={}".format(math.sqrt(x)))
print("factorial(x)={}".format(math.factorial(x)))


# In[5]:


# Logarithms and anti-logarithms
import math
x = float(input("Enter a real number: "))
print("Natural logarithm and anti-logarithm")
print("ln(x)={} exp(ln(x))={}".format(math.log(x), math.exp(math.log(x))))
print("\nCommon logarithm and anti-logarithm")
print("log(x)={} antilog(log(x))={}".format(math.log10(x), pow(10,math.log10(x))))
print("\nBase 2 logarithm and anti-logarithm")
print("log2(x)={} antilog2(log2(x))={}".format(math.log(x,2), pow(2,math.log(x,2))))


# In[7]:


name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18: print("Hi {}! You can vote!".format(name))
if age < 18: print("Sorry {}! You can’t vote!".format(name))


# In[9]:


name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print("Hi {}! You can vote!".format(name))
else:
    print("Sorry {}! You can’t vote!".format(name))


# In[13]:


x= int(input("Enter an integer:"))
if x>0:
    print("{} is positive".format(x))
elif x<0:
    print("{} is negetive".format(x))
else:
    print("{} is zero".format(x))


# In[15]:


#!/usr/bin/python
# Script to classify and determine
# the roots of a quadratic equation
import math
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))
discriminant = b**2 - 4*a*c
if discriminant == 0:
    print("The roots are real and equal")
    x = -b/(2*a)
    print("The root is",x)
elif discriminant > 0:
    print("The roots are real and distinct")
    part1 = -b/(2*a)
    part2 = math.sqrt(discriminant)/(2*a)
    x1 = part1 + part2
    x2 = part1 - part2
    print("The roots are", x1, "and", x2)
else:
    print("The roots are imaginary")
    part1 = -b/(2*a)
    part2 = math.sqrt(-discriminant)/(2*a)
    x1 = complex(part1, part2)
    x2 = complex(part1, -part2)
    print("The roots are", x1, "and", x2)


# In[ ]:





# In[ ]:




