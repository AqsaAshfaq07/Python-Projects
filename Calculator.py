from replit import clear
from art import logo
print(logo)

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2


operations = {
  '+' : add,
  '-' : subtract,
  '*' : multiply,
  '/' : divide
}


def calculator():
  
  n1 = int(input("Enter first number: \n"))
  should_continue = True

  while should_continue:
    operation_symbol = input("+, -, *, / \nPick an operation: ")
    n2 = int(input("Enter second number: \n"))
    calculate= operations[operation_symbol]
    answer = calculate(n1, n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")

    repeat = input("Type 'yes' if you want to perform another operation else 'no'.")

    if repeat == "yes":
      n1 = answer
      should_continue = True

    elif repeat == "no":
      should_continue = False
      clear()
      calculator()

    else:
      print("Please enter a valid input!")

calculator()