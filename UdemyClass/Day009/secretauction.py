auctionlogo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(auctionlogo)

print("Welcome to the secret auction program.")

auctionover = False

bid_dictionary = {}

while auctionover == False:
    bidder_name = input("What is your name?: ")
    bid_amount = int(input("What's your bid?: $"))
    
    bid_dictionary[bidder_name] = bid_amount
    
    morebidders = input("Are there many more bidders? Type 'yes' or 'no'.\n")
    
    if morebidders.lower() == "no":
        auctionover = True
    else:
        print("\n" * 100)
        
#print(bid_dictionary)

#find the winner
#can use max() = max(bid_dictionary, key=bid_dictionary.get)
high_bid = 0
high_bidder = ""
for bidder in bid_dictionary:
   if bid_dictionary[bidder] > high_bid:
       high_bid = bid_dictionary[bidder]
       high_bidder = bidder
       
print(f"The winner is {high_bidder} with a bid of ${bid_dictionary[high_bidder]} ")

#2nd way for highest bidder
high_bidder = max(bid_dictionary, key=bid_dictionary.get)
high_bid = bid_dictionary[high_bidder ]
print(f"The winner is {high_bidder} with a bid of ${high_bid} ")