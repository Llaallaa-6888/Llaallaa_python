
Bids = {}
def find_highest_bidder(Bids):
    highest_bidder = 0
    winner = ""
    for bidder in Bids:
        bid = Bids[bidder]
        if bid > highest_bidder:
          highest_bidder = bid
          winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bidder}")        

bidding = True
while bidding:
  name = input("What is your name?\n")
  bid = int(input(f"Hello {name}, what is your bid?\n $"))
  Bids[name] = bid
  to_bid = input("Are there more bidders? Type 'yes' or 'no'")
  if to_bid == "no":
    bidding = False
    find_highest_bidder(Bids)
  
                 


          
