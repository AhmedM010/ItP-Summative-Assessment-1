'''Exercise 4: Stages of Life :ballot_box_with_check:
Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:
•If the person is less than 2 years old, print a message that the person is a baby.
•If the person is at least 2 years old but less than 4, print a message that the person is a toddler.
•If the person is at least 4 years old but less than 13, print a message that the person is a kid.
•If the person is at least 13 years old but less than 20, print a message that the person is a teenager.
•If the person is at least 20 years old but less than 65, print a message that the person is an adult.
•If the person is age 65 or older, print a message that the person is an elder.'''

age=int(input("Enter your age here"))

if age >=0 and age <=125:
    if age > 125:
        print (f'{age} is not a valid age. Please enter an age between 0 add 125')
    elif age < 2:
        print (f'You are a {age} year old baby')
    elif 2<=age<4:
        print (f'You are a {age} year old toddler')
    elif 4<=age<13:
        print (f'You are a {age} year old kid')
    elif 13<=age<20:
        print (f'You are a {age} year old teenager')
    elif 20<=age<65:
        print (f'You are a {age} year old adult')
    else:
        print (f'You are a {age} year old elder')
else:
    print (f'{age} is not a valid age. Please enter an age between 0 add 125')