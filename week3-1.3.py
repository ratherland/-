#!/usr/bin/env python
# coding: utf-8

# In[12]:


#统计字符串中连续的重复字符个数
strs=input()
n=len(strs)
maxlen=1
length=1
maxstr=[]
for i in range(n-1): 
    if strs[i]==strs[i+1]:
        length+=1
        maxstr.append(strs[i+1])
        if length>maxlen:
            maxlen=length
    else:
        length=1
print(maxlen)


# In[17]:


#删空格
string=input()
print(string.replace(" ",""))


# In[ ]:




