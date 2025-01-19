'''Exercise 1: Pizza Toppings :ballot_box_with_check:
Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.'''

prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nType 'quit' to end interaction: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"  I'll add {topping} to your pizza.")
    else:
        break