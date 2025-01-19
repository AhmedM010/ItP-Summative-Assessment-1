## Exercise 3: Print date and Time :ballot_box_with_check:

#Write a Python program to display the current date and time.

import datetime

now = datetime.datetime.now()

print("The date and time right now is")

print(now.strftime("%d-%m-%Y %H:%M:%S"))