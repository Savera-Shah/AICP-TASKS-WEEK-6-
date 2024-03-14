# Constants
ADULT_ONE_DAY = 20.00
CHILD_ONE_DAY = 12.00
SENIOR_ONE_DAY = 16.00
FAMILY_ONE_DAY = 60.00
GROUP_ONE_DAY = 15.00

ADULT_TWO_DAYS = 30.00
CHILD_TWO_DAYS = 18.00
SENIOR_TWO_DAYS = 24.00
FAMILY_TWO_DAYS = 90.00
GROUP_TWO_DAYS = 22.50

LION_FEEDING = 2.50
PENGUIN_FEEDING = 2.00
BARBECUE = 5.00

def display_one_day_options():
    print("One-Day Ticket Options:")
    print("1. Adult - $%.2f" % ADULT_ONE_DAY)
    print("2. Child - $%.2f" % CHILD_ONE_DAY)
    print("3. Senior - $%.2f" % SENIOR_ONE_DAY)
    print("4. Family - $%.2f" % FAMILY_ONE_DAY)
    print("5. Group (6 or more people) - $%.2f" % GROUP_ONE_DAY)
    print("Attractions:")
    print("a. Lion Feeding - $%.2f" % LION_FEEDING)
    print("b. Penguin Feeding - $%.2f" % PENGUIN_FEEDING)

def display_two_day_options():
    print("Two-Day Ticket Options:")
    print("1. Adult - $%.2f" % ADULT_TWO_DAYS)
    print("2. Child - $%.2f" % CHILD_TWO_DAYS)
    print("3. Senior - $%.2f" % SENIOR_TWO_DAYS)
    print("4. Family - $%.2f" % FAMILY_TWO_DAYS)
    print("5. Group (6 or more people) - $%.2f" % GROUP_TWO_DAYS)
    print("Attractions:")
    print("a. Lion Feeding - $%.2f" % LION_FEEDING)
    print("b. Penguin Feeding - $%.2f" % PENGUIN_FEEDING)
    print("c. Evening Barbecue - $%.2f (Only available with two-day tickets)" % BARBECUE)

def display_booking_days():
    print("Days Available for Booking:")
    print("Monday")
    print("Tuesday")
    print("Wednesday")
    print("Thursday")
    print("Friday")
    print("Saturday")
    print("Sunday")

def main():
    print("Welcome to the Wildlife Park Ticket Booking System\n")
    display_one_day_options()
    print("\n")
    display_two_day_options()
    print("\n")
    display_booking_days()

main()