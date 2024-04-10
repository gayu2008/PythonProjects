#!/usr/bin/env python
# coding: utf-8

# ## Type 1

# In[5]:


import phonenumbers


# In[2]:


#pip install phonenumbers


# In[6]:


from phonenumbers import geocoder


# In[15]:


phone_number1 = phonenumbers.parse("+917294536271")
phone_number2 = phonenumbers.parse("+918878586271")
phone_number3 = phonenumbers.parse("+12136574429")
phone_number4 = phonenumbers.parse("+201234567890")
phone_number5 = phonenumbers.parse("+201234567890")

print("\n Phone Numbers Location \n")
print(geocoder.description_for_number(phone_number1, "en"));
print(geocoder.description_for_number(phone_number2, "en"));
print(geocoder.description_for_number(phone_number3, "en"));
print(geocoder.description_for_number(phone_number4, "en"));
print(geocoder.description_for_number(phone_number5, "en"));


# ## Type 2

# In[19]:


import phonenumbers
from phonenumbers import geocoder

def get_phone_number():
    phone_number_str = input("Enter the phone number (in international format, e.g., +1234567890): ")
    return phonenumbers.parse(phone_number_str)

def display_region(phone_number):
    region = geocoder.description_for_number(phone_number, "en")
    print(f"The region for the provided phone number is: {region}")

if __name__ == "__main__":
    print("\nPhone Number Location Finder\n")
    
    phone_number = get_phone_number()
    display_region(phone_number)


# In[ ]:




