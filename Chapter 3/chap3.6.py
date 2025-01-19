## Exercise 6: Shrinking Guest List :ballot_box_with_check:
# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# •Start with your program from Exercise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
# •Use pop() to remove guests from your list one at a time until only two names remain in your list. 
# Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# •Print a message to each of the two people still on your list, letting them know they’re still invited.
# •Use del to remove the last two names from your list, so you have an empty list. 
# Print your list to make sure you actually have an empty list at the end of your program.

names = ['ZJ', 'Bahri', 'Luigi']
print(f"Yo {names [0]}, come over, lets make some food. im hungry")
print(f"{names [1]}, come over and help ZJ and I, were making hella food right now ")
print(f"Yoooo {names [2]}, come make food with us, were eating good tonight!!\n")

print(f'Sorry guys, apparently {names[2]} cant make it\n')

del (names [2])
names.insert (2, "Janfe")

print(f"Yo {names [0]}, come over, lets make some food. im hungry")
print(f"{names [1]}, come over and help ZJ and I, were making hella food right now ")
print(f"Yoooo {names [2]}, come make food with us :)\n")

print('Apparently only two people will fit on the table!')
print(f"sorry {names[1]} we can't invite you to dinner\n")
names.pop(1)

print(f"hey {names [0]}, something came up but youre still invited dont worry")
print(f"{names [1]}, youre still invited, so please do come over\n")

del (names [0])
del (names [0])
print(names)
