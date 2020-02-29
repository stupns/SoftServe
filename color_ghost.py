from random import choice


# Color Ghost
# Create a class Ghost
# Ghost objects are instantiated without any arguments.
# Ghost objects are given a random color attribute of white" or "yellow" or "purple" or "red" when instantiated

class Ghost:
    colors = ['white', 'yellow', 'red', 'purple']
    color = print(choice(colors))


ghost = Ghost
ghost.color
