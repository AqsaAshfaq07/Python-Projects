#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# BMI - Body Mass Index

weight = float(input("Enter your weight in kg:  "))
height = float(input("Enter your height in m:  "))
bmi = round(weight / (height*height))

if bmi < 18.5:
    print(f"Your BMI is {bmi} and You're Underweight")
elif bmi < 25:
    print(f"Your BMI is {bmi} and You have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {bmi} and You're slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {bmi} and You're obese")
else :
    print(f"Your BMI is {bmi} and You're clinically obese!!")

