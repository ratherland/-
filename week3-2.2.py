#!/usr/bin/env python
# coding: utf-8

# In[21]:


#循环求根号2
def Square_root_1():
    c=2
    i=0
    g=0
    for j in range(0,c+1):
        if(j*j>c and g==0):
            g=j-1
    while (abs(g*g-c)>0.0001):
        g+=0.00001
        i=i+1
    print(g)
Square_root_1()


# In[22]:


#二分法求根号2
def Square_root_2():
    c=2
    i=0
    m_max=c
    m_min=0
    g=(m_max+m_min)/2
    while (abs(g*g-c)>0.00000000001):
        if(g*g<c):
            m_min=g
        else:
            m_max=g
        g=(m_max+m_min)/2
        i=i+1
    print(g)
Square_root_2()


# In[24]:


#蒙特卡罗求根号2
import random 
import math
L = 2
N = 10000000
C=0
for i in range(N):
    x = 2
    y = random.uniform(0.0,2.0)
   
    if y <= math.sqrt(x):
        C += 1 
I=C/N*L
print(I)

