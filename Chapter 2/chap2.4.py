## Exercise 4: Favorite Number :ballot_box_with_check:
# Use a variable to represent your favorite number. Then,using that variable, create a message that reveals your favorite number. Print that message.
x = 101
reveal=str(input("Would you like to know my favorite number? (y/n)"))
if reveal=="y":
    print (f"It's {x}!! Becuase its the smallest Cyclops Number!")
elif reveal=="n":
    print('aww :C')
else:
    print('Please pick between y or n!')

