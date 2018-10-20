
# coding: utf-8

# In[12]:


import datetime
dob = '20110101'


today = datetime.datetime.now()
yyyy = int(dob[0:4])
mm = int(dob[4:6])
dd = int(dob[6:8])
dob = datetime.datetime(yyyy,mm,dd)
age_in_days = (today - dob).days
age_in_years = age_in_days/365
print(int(age_in_years))


# In[16]:


# Formatt date
dob1 = datetime.date(2011,1,1)
print(dob1)

frm = 'year {:%A, %B, %d, %Y}'
print(dob1.strftime('%A, %B, %d, %Y')) # old method
print(frm.format(dob1))

dob3 = datetime.datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
print(dob3)

