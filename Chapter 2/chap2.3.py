## Exercise 3: Stripping Names :ballot_box_with_check:
# Tidy up the code to make it easier to understand, 
# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. 
# Make sure you use each character combination, “\t” and “\n”, at least once.
# Print the name once, so the whitespace around the name is displayed. 
# Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = "\tChamber\n"

print("no change")
print(name)

print("going for lstrip()")
print(name.lstrip())

print("going for rstrip()")
print(name.rstrip())

print("going for strip()")
print(name.strip())
