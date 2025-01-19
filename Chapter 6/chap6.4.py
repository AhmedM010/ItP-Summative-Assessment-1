'''Exercise 4: Deli :ballot_box_with_check:
Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.'''

sandwich_orders = ['casa', 'grilled cheese', 'turkey', 'chopped cheese']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm making your {current_sandwich} sandwich right now. One moment.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I made the {sandwich} sandwich. Order up!")
