

any_bid = False
bid = {}
while not any_bid:

    name = input("what's your name? ")
    bid_price = float(input("how much is your bid? $"))
    bid[name] = bid_price
    other_bid = input("is there any bid? (type your answer with y/n)").lower()
    
    if other_bid == "n":
        any_bid = True
        
s = 0      
for item in bid:
    if s < bid[item]:
        N = item 
        s = bid[item]
        
        
        
print(f"\nbid winner is {N} with ${s} which is the highest bid price.")
            