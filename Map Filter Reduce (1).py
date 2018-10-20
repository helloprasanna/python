
# coding: utf-8

# Demonstrates the Map function
#     which applies function to list of values

# In[4]:


import math

def area(n):
    return math.pi * (n**2)

radii=[3,4,5,8,10,38]

print(radii)

print(list(map(area,radii)))


# ### Applying Map

# In[5]:


li = [('a',1),('b',2),('c',3)]

conv = lambda data: (data[0],data[1]**2)

print(list(map(conv,li)))


# ### Apply Filter
#     Filter the list containing more than average

# In[10]:


import statistics

data = [1,3,4,5,6,7,3,4,6,8,9]
avg = statistics.mean(data)

print(list(filter(lambda x: x>avg,data)))


# ### Filter None 

# In[12]:


countries=['hello.py','american','russia','','hell']

print(list(filter(None,countries)))


# ### Apply reduce to data set

# In[ ]:


data = [1,3,4,5,6,7,3,4,6,8,9]

