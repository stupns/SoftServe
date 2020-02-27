# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!


def areYouPlayingBanjo(name):
    if name[:1] == 'r':
        return name + " plays banjo"
    elif name[:1] == 'R':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"
