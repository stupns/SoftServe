# You're re-designing a blog and the blog's posts have the following format for showing the date and time a post was
# made: Weekday Month Day, time e.g., Friday May 2, 7pm You're running out of screen real estate, and on some pages
# you want to display a shorter format, Weekday Month Day that omits the time.


def shorten_to_date(long_date):
    return long_date.split(',')[0]


if __name__ == '__main__':
    assert shorten_to_date("Monday February 2, 8pm") == "Monday February 2"
    assert shorten_to_date("Tuesday May 29, 8pm") == "Tuesday May 29"
    assert shorten_to_date("Wed September 1, 3am") == "Wed September 1"
    assert shorten_to_date("Friday May 2, 9am") == "Friday May 2"
    assert shorten_to_date("Tuesday January 29, 10pm") == "Tuesday January 29"
    print("Well job!")
