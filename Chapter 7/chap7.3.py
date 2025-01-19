'''Exercise 3: T-Shirt  :ballot_box_with_check:
Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function 
should print a sentence summarizing the size of the shirt and the message printed on it. Call the function once using positional 
arguments to make a shirt. Call the function a second time using keyword arguments.'''

def make_shirt(size, message):
    '''Makes ... shirts... like it just prints the message you want on it...'''
    print (f"\nI'm gonna make a {size} shirt")
    print (f'''and it'll say "{message}"''')

make_shirt('Extra Large', 'This is a small shirt')
make_shirt(message= "That shirt doesn't seem right", size='Small')