from datetime import datetime
import locale
#pull and import data
print("Welcome to the Hotel Reservation program... \n")

again = "y"
while again.lower() == "y":
    # arrival date?
    while True:
        date_str = input("Please Enter your arrival date (YYYY-MM-DD): ")
        try: 
            # correct format data validation
            arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please Try again.")
            print()
            continue  # used skip next if statement and re-start loop

        # strip non-zero values from datetime object 
        now = datetime.now()
        today = datetime(now.year, now.month, now.day)        
        if arrival_date < today:
            print("Arrival date must be today or later. Please Try again.")
            print()
        else:
            break
      # remember to break while 

    # ask for their departure date
    while True:
        date_str = input("Please Enter departure date (YYYY-MM-DD): ")
        try:
            departure_date = datetime.strptime(date_str, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please try again.")
            print()
            continue  # skip next if statement and re-start loop
            
        if departure_date <= arrival_date:
            print("Departure date must be after arrival date. Please try again.")
            print()
        else:
            break
        # remember to break while
    print()

    # Rate and cost
    rate = 125.0
    rate_message = ""
    if arrival_date.month == 8:    # August is peak season
        rate = 165.0
        rate_message = "(Peak season rate)"
    total_nights = (departure_date - arrival_date).days
    total_cost = rate * total_nights

    # show formated results
    date_format = "%B %d, %Y"
    locale.setlocale(locale.LC_ALL, "en_US")
    print(f"Arrival Date:    {arrival_date:{date_format}}")
    print(f"Departure Date:  {departure_date:{date_format}}")
    print(f"Nightly rate:    {locale.currency(rate)} {rate_message}")
    print(f"Total nights:    {total_nights}")
    print(f"Total price:     {locale.currency(total_cost)}")
    print()

    again = input("Would you like to continue? (y/n): ")
    print()
        
print("Thank you for your reservation! Have a great day.")
