
# coding: utf-8

# In[19]:


fibCache = {}

def fib(n):
    """It returns fibonacci series for n numbers"""
    if n in fibCache:
        return fibCache[n]
    
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        value = fib(n-1)+fib(n-2)
        
    fibCache[n] = value
    return value


# In[23]:


import datetime

t = datetime.datetime.now()
for i in range(1,10):
    print(i,':',fib(i))
    
t1 = datetime.datetime.now()
print('Timetaken : ',t1-t)
    


# In[10]:


# Example for inbuilt LRU cache
from functools import lru_cache

@lru_cache(maxsize = 30)
def fib1(n):
    """Returns the fibonnaci series for n numbers"""
    if type(n) != int:
        raise TypeError("n must be positive int")
    if n < 1:
        raise ValueError("n must be positive int")
        
    if n == 1:
        return 1
    elif n ==2:
        return 1
    elif n > 2:
        return fib1(n-1) + fib1(n-2)
    

import datetime

t = datetime.datetime.now()
for i in range(1,10):
    print(i,':',fib1(i))

print("fibonnaci number at ",fib1(-22))
t1 = datetime.datetime.now()
print('Timetaken : ',t1-t)

