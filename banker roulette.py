import random

names = input("Enter names of all the peeps having a meal here! \n ")
names_list = names.split(" ")
n = len(names_list)

num = random.randint(0, n)
payer = names_list[num]
print(f"{payer} will pay the whole bill today!")