from art import logo
print(logo)
isbid = True
new_dict = {}
bids =[]
while isbid:
    name = input("What is your name? ")
    bid = input("What is your bid? ")
    new_dict[name]=bid
    decision = input("Are there any more bidders? Type yes or no ")
    if decision == 'no':
        isbid = False
maximum = max(new_dict.values())
maximum_key = max(new_dict, key=new_dict.get)
print(f'Winner is {maximum_key} with a bid of {maximum}')
