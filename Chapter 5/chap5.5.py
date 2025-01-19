'''Exercise 5: Pets :ballot_box_with_check:
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, 
print everything you know about each pet'''

# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'animal': 'cat',
    'name': 'Señora',
    'owner': 'janfe',
}
pets.append(pet)

pet = {
    'animal type': 'dog',
    'name': 'mini',
    'owner': 'sean',
}
pets.append(pet)

pet = {
    'animal type': 'parrot',
    'name': 'ari',
    'owner': 'jaiden',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")