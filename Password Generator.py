# Step - 1
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
           'l', 'm', 'n', 'o', 'p', 'q', 'r', 's' ,'t', 'u', 'v',
           'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Step - 2
print("Welcome to the Password Generator!")

num_letters = int(input("How many letters do you want in your password? \n"))
num_numbers = int(input("How many numbers would you like? \n"))
num_symbols = int(input("How many symbols would you like? \n"))

# print(f"Try this strong password!!  {password}")

# Step-3
# Easy Level

password = ""

for char in range(1, num_letters+1):
    password += random.choice(letters)
    
for num in range(1, num_numbers+1):
    password += random.choice(numbers)
    
for symb in range(1, num_symbols+1):
    password += random.choice(symbols)
    
# print(password)

# Step - 4
# Hard Level

password_list = []

for char in range(1, num_letters+1):
    password_list.append(random.choice(letters))
    
for num in range(1, num_numbers+1):
    password_list.append(random.choice(numbers))
    
for symb in range(1, num_symbols+1):
    password_list.append(random.choice(symbols))
    
# print(password_list)  # old one

random.shuffle(password_list)
# print(password_list)  # new one

#  Step - 5
# Gather the whole thing

password_ = ""

for char in password_list :
    password_ += char
    
print(password_)