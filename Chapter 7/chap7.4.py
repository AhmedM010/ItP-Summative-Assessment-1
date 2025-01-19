'''Exercise 4:  Large Shirts :ballot_box_with_check:
Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different message.'''

def make_shirt(size='large', message='I Love Python'):
    '''Makes ... shirts... like it just prints the message you want on it...'''
    print (f"\nI'm gonna make a {size} shirt")
    print (f'''and it'll say "{message}"''')

make_shirt()
make_shirt(size='medium')
make_shirt(size='small', message="I'm potato")