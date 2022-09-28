#!/usr/bin/env python
# coding: utf-8

# In[18]:


#蒙特卡罗求积分
import random 
import math
S = 1*2
N = 10000000
C=0
for i in range(N):
    x = random.uniform(0.0,1.0)
    y = random.uniform(0.0,2.0)
   
    if y <= x*x+x*x*x:
        C += 1 
I=C/N*S
print(I)

