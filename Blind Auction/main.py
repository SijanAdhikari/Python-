import art
print(art.logo)
next=True
bid_details={}


def highest_bid(bidding_dictionary):
    max_bidder=""
    max_bid=0
    for key in bid_details:
        bid_amount=bid_details[key]
        if bid_amount > max_bid:
            max_bidder = key
            max_bid = bid_amount
    print(f"The winner is {max_bidder} with a bid of ${max_bid}")


while next:
    name=input("What is your name?:")
    bid=int(input("What is your bid?: $"))
    bid_details[name]=bid
    other_bids=input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if other_bids=="yes":
        print("\n"*200)
    elif other_bids=="no":
        next=False
        highest_bid(bid_details)

    else:
        print("Invalid Input**********")





