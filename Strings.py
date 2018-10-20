
# coding: utf-8

# In[32]:



a = 3
b = 1
fl = 3.3837373
ll = 23234343434343434343
print(type(ll))
ll = 3.83838
print(type(ll))

print(a+b)
print(type(a))
print(a)
type(b) # output goes to terminal
print(type(fl))
print('hello')

# Complex numbers
z = 2 - 6.1j
print(z)
print(type(z))
print(z.real)
print(z.imag)


# In[ ]:


c="hello "+str(a+b)
print(c)
print(len(c))
type(c)


# In[ ]:


for i in range(2,5):
    print(i)


# In[ ]:


string = 'string'
for i in range(11):
    string += str(i)
print (string)


# In[ ]:


s = "foo bar"
s = 'foo bar'
s = r"c:\dir\new"                     # raw (== 'c:\\dir\\new')
s = """Hello
       world"""
s.join(" baz")  # don't know
n = len(s)
"Ala ma {} psy i {} koty".format(2,3)
"Square root of 2 is equal to {:.2f}".format(math.sqrt(2))


# In[ ]:


# substring
s = "1234567890"
print(s[:3]+'-'+s[3:5]+"-"+s[5:])    # start(Exclusive):End index
print(s[-2:])
print(s[:-2])

# Index
print(s[0])

# formatt
print("Ala ma {} psy i {} {} koty".format(2,3,'x'))
print("Currency Formatting {:.2f}".format(16.3834774))


# In[ ]:


# Lists
list = [1,8,3,4,'hi']
list.append('hello')
list.remove(8)
print(list.pop())
print('index '+str(list.index('hi')))
for i in list:
    print(i)

