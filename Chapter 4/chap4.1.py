'''Exercise 1:  Alien Colors #1 :ballot_box_with_check:
Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
•Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.
•Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)'''

#passing version
alien_color = "green"

if alien_color == "green":
    print ('That was a green alien! You earn 5 Points!')

#failing version
alien_color = "red"

if alien_color == "green":
    print ('That was a green alien! You earn 5 Points!')