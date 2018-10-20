
# coding: utf-8

# In[39]:


import math

def isPrime(n):
    if n == 1:
        return False;
    elif n%2 == 0 or n==2 :
        return True
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
        #for i in range(2,n):
            if n % i == 0:
                return False
        return True
    

isPrime(13)             


# In[24]:


for i in range(1,10):
    print(i)
    if isPrime(i):
        print(i,' is Prime')


# In[75]:


from datetime import datetime

t = datetime.now()
print(isPrime(1000099))
t1 = datetime.now()

print('Time taken', (t1-t).microseconds, t1-t)


# In[58]:


# Another prime generation method
import sympy
is_prime = lambda x: sympy.isprime(x)


t = datetime.now()
print(is_prime(1000099))
t1 = datetime.now()
print('Time taken', (t1-t).microseconds, t1-t)

