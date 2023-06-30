#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# There are some prerequisites for someone to buy a ticket to ride the roller coster

height = int(input("Your height in cm: "))
age = int(input("What's your age?  "))
bill = 0
photo = input("Want photos?  Y or n")

if height >= 120:
    print("Go ahead")
    
    if age < 12:
        bill = 5
    elif age <= 18 and age >= 12:
        bill = 7
    elif age <= 55 and age >= 45:
        print("Everything is free. Have a good ride :)")
        bill = 0
    else:
        bill = 12
        
# Adding an Option of Photos
    if photo == "Y":
        print(f"Please pay ${bill + 3}")
    else:
        print(f"Please pay ${bill}")
        
else:
    print("You can't ride the roller coster")

