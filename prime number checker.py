# prime number - that can only be divided by itself

n = int(input("Check this number:  \n"))

def prime_checker(number):
    if number%2 != 0 and number%3 != 0 and number%5 != 0:
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")

prime_checker(n)