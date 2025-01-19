'''Exercise 5: Cities
Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
such as Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the efault country.
'''

def describe_city(city, country='United Arab Emirates'):
    '''just prints the city and country with the default being the UAE'''
    msg=f"\n {city.title()} is in {country.title()}"
    print (msg)

describe_city(city='abu dhabi')
describe_city('paris', 'france')
describe_city('Manila')