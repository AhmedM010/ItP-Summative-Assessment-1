'''Exercise 5: No Pastrami :ballot_box_with_check:
Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.'''

sandwich_orders = ['casa', 'pastrami', 'grilled cheese', 'turkey', 'pastrami', 'chopped cheese', 'pastrami',]
finished_sandwiches = []

print("Sorry, were out of pastrami for today. Come back tomorrow when the shop resets!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\n")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich right now. One moment.")
    finished_sandwiches.append(current_sandwich)
print("\n")
for sandwich in finished_sandwiches:
    print(f"I made the {sandwich} sandwich. Order up!")