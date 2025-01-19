'''Exercise 4: Rivers :ballot_box_with_check:
Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
* Use a loop to print the name of each river included in the dictionary.
* Use a loop to print the name of each country included in the dictionary.'''

rivers = {
    'pasig': 'philippines',
    'amazon': 'brazil',
    'thames': 'United Kingdom',
    }

for river, country in rivers.items():
    print(f"The {river.title()} River flows through {country.title()}.")

print("\nRivers included in data set:")
for river in rivers.keys():
    print(f"- {river.title()}")

print("\nCountries included in data set:")
for country in rivers.values():
    print(f"- {country.title()}")