#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Calculates Love between you and your partner

person1 = (input("Enter your name:  ")).lower()
person2 = (input("Enter the name of your crush:  ")).lower()

names = person1 + person2

# Calculate number of times TRUE LOVE characters occur in the names
true = str(int(names.count("t")) + int(names.count("r")) + int(names.count("u")) + int(names.count("e")))
love = str(int(names.count("l")) + int(names.count("o")) + int(names.count("v")) + int(names.count("e")))

true_love = int(true + love)
true_love
# Showing use proper interpretation
if true_love < 10 or true_love > 90:
    print(f"Your love score is {true_love}, you go together like coke and mentos :)")
elif true_love < 50 and true_love > 40:
    print(f"Your love score is {true_love}, you are just right together")
else:
    print(f"Your love score is {true_love}")

