from replit import clear
from art import logo


bidders = {}

def check_winner(bidders):

    winner_name = ""
    winning_bid = 0

    for name in bidders:
        if bidders[name] > winning_bid:
            winner_name = name
            winning_bid = bidders[name]

    print(f"The winner is {winner_name} with a bid of ${winning_bid}. ")




print(logo)
continue_bidding = "yes"
print("Welcome to the silent auction.\n")
while continue_bidding == "yes":

    
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    continue_bidding = input("Are there more bidders? (yes or no):")

    if continue_bidding == "yes":
        clear()
    else:
        check_winner(bidders)
        break

 




