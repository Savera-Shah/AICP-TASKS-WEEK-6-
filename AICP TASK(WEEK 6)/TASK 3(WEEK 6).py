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

# Function to process a booking
def process_booking():
    print("Processing Booking...\n")
    
    # Input tickets and attractions required
    one_day_tickets = int(input("Enter the number of one-day tickets required: "))
    two_day_tickets = int(input("Enter the number of two-day tickets required: "))
    lion_feeding = int(input("Enter the number of lion feeding attractions required: "))
    penguin_feeding = int(input("Enter the number of penguin feeding attractions required: "))
    barbecue = 0
    if two_day_tickets > 0:
        barbecue = int(input("Enter the number of evening barbecue attractions required: "))
    
    # Calculate total cost for each option
    total_cost_one_day = (one_day_tickets * (ADULT_ONE_DAY + CHILD_ONE_DAY + SENIOR_ONE_DAY) +
                          lion_feeding * LION_FEEDING + penguin_feeding * PENGUIN_FEEDING)
    total_cost_two_day = (two_day_tickets * (ADULT_TWO_DAYS + CHILD_TWO_DAYS + SENIOR_TWO_DAYS) + lion_feeding * LION_FEEDING + 
                          penguin_feeding * PENGUIN_FEEDING + barbecue * BARBECUE)
    
    # Determine the best value option
    if total_cost_one_day <= total_cost_two_day:
        print("\nBest Value Booking: One-Day Ticket")
        total_cost = total_cost_one_day
    else:
        print("\nBest Value Booking: Two-Day Ticket")
        total_cost = total_cost_two_day
    
    # Allocate a unique booking number (just using a simple incrementing number)
    global booking_number
    booking_number += 1
    
    # Display booking details
    print("Total Cost: $%.2f" % total_cost)
    print("Booking Number: %d" % booking_number)

def main():
    print("Welcome to the Wildlife Park Ticket Booking System\n")
    display_one_day_options()
    print("\n")
    display_two_day_options()
    print("\n")
    display_booking_days()
    print("\n")
    
    global booking_number
    booking_number = 0
    
    while True:
        process_booking()
        print("\n")
        cont = input("Do you want to make another booking? (yes/no): ").lower()
        if cont != 'yes':
            print("Thank you for using the Wildlife Park Ticket Booking System. Goodbye!")
            break
main()