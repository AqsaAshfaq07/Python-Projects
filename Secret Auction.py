from replit import clear
from art import logo

print(logo)
print("Welcome to the Secret Auction Program!")

bid_auction = {}
max_bid = 0
start_over = True

while start_over:
  name = input("What is your name?: \n")
  bid_price = int(input("What's your bid amount?: \n$"))

  bid_auction[name] = bid_price

  #     print(bid_auction)
  remaining_bidders = input(
    "Are there any other bidders? Type 'yes' or 'no' \n")

  if remaining_bidders == "yes":
    clear()
    continue

  elif remaining_bidders == "no":
    start_over = False

    for key in bid_auction:
      if bid_auction[key] > max_bid:
        max_bid = bid_auction[key]
    print(f"The winner is {key} with a bid of ${max_bid}")




  else:
    print("Please enter correct word!!")
    start_over = False