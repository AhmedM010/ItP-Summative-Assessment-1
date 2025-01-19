## Exercise 5: Change Guest List :ballot_box_with_check:
# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite
# •Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
# •Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
# •Print a second set of invitation messages, one for each person who is still in your list.

names = ['ZJ', 'Bahri', 'Luigi']
print(f"Yo {names [0]}, come over, lets make some food. im hungry")
print(f"{names [1]}, come over and help ZJ and I, were making hella food right now ")
print(f"Yoooo {names [2]}, come make food with us, were eating good tonight!!")

print(f'Sorry guys, apparently {names[2]} cant make it')

del (names [2])
names.insert (2, "Janfe")

print(f"Yo {names [0]}, come over, lets make some food. im hungry")
print(f"{names [1]}, come over and help ZJ and I, were making hella food right now ")
print(f"Yoooo {names [2]}, come make food with us :)")