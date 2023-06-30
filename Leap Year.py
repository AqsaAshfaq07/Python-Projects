#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Check every year using highly effective computations 

year = int(input("Which year do you want to check?  "))

if year %4 == 0:
    if (year %100 != 0):
        if year %400 == 0:
            print("Leap year")
        else:
            print("Not Leap year")
    else:
        print("Leap year")
else:
    print("Not Leap year")

