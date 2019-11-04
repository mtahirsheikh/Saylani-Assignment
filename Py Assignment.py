#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")


# In[15]:


import sys
print(sys.version)


# In[19]:


import datetime
today = datetime.datetime.now()
print(today)


# In[28]:


radius_str = input("Enter the radius of the circle:\n")
radius = float(radius_str)
area = (22/7)* radius * radius
print('The area of the circle is: %.2f'%area)


# In[31]:


first_name = input('Enter your first name:\n')
last_name = input('Enter your last name:\n')
print(last_name,first_name)


# In[38]:


input_1 = input('Enter first value:\n')
input_2 = input('Enter second value:\n')
print(input_1+input_2)


# In[ ]:




