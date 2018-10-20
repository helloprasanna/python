
# coding: utf-8

# In[35]:


class User:
    pass


user1 = User()
user1.f = 'Prasanna'
user1.s = 'Jay'

print(user1.f+' '+user1.s)

user2 = User()
user2.f = 'hello'
user2.s = 'b'

print(user2.f+' '+user2.s)


# In[3]:


import datetime

class Userx:
    """
    This is a test class. and this part is documentation
    """
    def __init__(self,f,dob):
        """Constructor method
        self refers to new object
        """
        self.f = f
        self.dob = dob
        
        fp=f.split(' ')
        self.fn = fp[0]
        last = fp[-1] 
        self.last = fp[-1] 
        
    def age(self):
        """returns the age"""
        today = datetime.datetime.now()
        yyyy = int(self.dob[0:4])
        mm = int(self.dob[4:6])
        dd = int(self.dob[6:8])
        dob = datetime.datetime(yyyy,mm,dd)
        age_in_days = (today - dob).days
        age_in_years = age_in_days/365
        return int(age_in_years)

user3 = Userx('nila pras','20110502')
print(user3.f)
print(user3.dob)
print(user3.fn)
print(user3.last)

print(user3.age())

#help(Userx)

