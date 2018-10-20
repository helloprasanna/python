
# coding: utf-8

# In[4]:


fl = lambda fn, ln: fn.strip()+ ' ' +ln.strip()

print(fl(" hello"," jd "))


# In[10]:


authors=['add ajo','iss newton','sidney sheldon','mmmm nnnn','aaa zzz']

authors.sort(key=lambda name: name.split(' ')[0].lower())

authors

