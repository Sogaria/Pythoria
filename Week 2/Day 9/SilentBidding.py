import os
auction = {}
def MaxBid(name: str, bid: int) -> tuple:
    auction[name] = bid
    
    highestBidder = ""
    highestBid = 0
    for key in auction:
        if auction[key] > highestBid:
            highestBid = auction[key]
            highestBidder = key
    
    return (highestBidder, highestBid)

print("Welcome to the secret auction program.")
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    MaxBid(name, bid)
    nextBid = input("Are there any other bidders? Type 'yes' or 'no'.")
    if nextBid == "yes":
        os.system('cls')
    else:
        os.system('cls')
        break

name, bid = MaxBid("", 0)
print(f"{name} wins the auction with ${bid}!")


