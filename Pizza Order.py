#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Facing difficulty getting the user requirements and processin them???
# Use this Pizza Order Automator!!

size = input("What size pizza do you want?  (S, M, L)")
pepperoni = input("Do you want to add pepperoni?  (Y, n)")
extra_cheese = input("Do you want to add extra cheese?  (Y, n)")
price = 0

if size == "S":
    price = 15
    if pepperoni == "Y":
        price += 2
    if extra_cheese == "Y":
            price += 1
    
elif size == "M":
    price = 20
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
            price += 1
            
elif size == "L":
    price = 25
    if pepperoni == "Y":
        price += 3
    if extra_cheese == "Y":
            price += 1
            
print(f"Please pay ${price}")

