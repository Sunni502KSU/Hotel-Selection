# Hotel Selection Program
# This program helps users find hotels based on:
# destination, amenities, rating, and budget
# ----------------------------------------------------------

# ----------------------------------------------------------
# FUNCTION: Create hotel database to be used for this program
# ----------------------------------------------------------
# Creates the hotel data file
def create_file_if_needed():

    # Try to open the hotel file to check if it exists
    try:
        with open("hotels.txt", "r"):  # r = read mode
            pass              #file exists, so no new file needs to be created 

    # Create file if missing
    except FileNotFoundError:

      with open("hotels.txt", "w") as file:  #w = write mode, opens the file so that data can be written into it

    # Hotel data format:
    # Name, City, Amenities, Rating, Price

        file.write("Grand Atlanta Hotel,atlanta,wifi|breakfast|pool,4.5,180\n")
        file.write("Peach Tree Inn,atlanta,wifi|parking,4.0,120\n")
        file.write("Luxury Suites,miami,wifi|breakfast|pool|parking,4.8,250\n")
        file.write("Budget Stay,miami,wifi,3.5,80\n")
        file.write("City Comfort Hotel,new york,wifi|breakfast,4.3,200\n")
        file.write("Sunset Resort,los angeles,wifi|pool|parking,4.6,220\n")
        file.write("Metro Suites,chicago,wifi|breakfast|parking,4.2,160\n")
        file.write("Ocean Breeze Hotel,miami,wifi|pool|parking,4.7,150\n")
        file.write("Downtown Luxury,new york,wifi|breakfast|parking,4.9,300\n")
        file.write("Comfort Inn,chicago,wifi|breakfast,4.1,110\n")
        file.write("Beach Paradise,miami,wifi|breakfast|pool,4.4,175\n")
        file.write("Southern Suites,atlanta,wifi|parking|breakfast,4.3,140\n")
        file.write("Miami Grand Resort,miami,wifi|parking|pool,4.7,200\n")

        # ----------------------------------------------------------
# FUNCTION: Load hotel data from file
# ----------------------------------------------------------
def load_hotels():

    hotels = []      #creates an empty list called hotels 

    # Open hotel file
    with open("hotels.txt", "r") as file:

        # Read each line
        for line in file:

            # Remove extra spaces/new lines
            line = line.strip()

            if line == "":   #tells program to skip any blank lines 
                continue

            # Split line into pieces
            data = line.split(",")

            # Store hotel information
            hotel = {
                "name": data[0],
                "location": data[1].lower(),
                "amenities": data[2].lower().split("|"),
                "rating": float(data[3]),
                "price": float(data[4])
            }

            # Add hotel to list
            hotels.append(hotel)    #the program reads the file and adds the hotel information 

    return hotels   #sends hotel list back to the function call 


# ----------------------------------------------------------
# FUNCTION: Find hotels matching user preferences
# ----------------------------------------------------------
def find_hotels(hotels, destinations,
                amenities, min_rating, max_price):

    matches = []     #creates an empty list called matches 

    # Check every hotel
    for hotel in hotels:

        # Check destination
        if hotel["location"] in destinations:

            # Check rating
            if hotel["rating"] >= min_rating:

                # Check budget
                if hotel["price"] <= max_price:

                    has_all = True

                    # Check amenities
                    for item in amenities:

                        if item not in hotel["amenities"]:
                            has_all = False

                    # Add matching hotel to the list 
                    if has_all:
                        matches.append(hotel)

    return matches


# ----------------------------------------------------------
# FUNCTION: Sort hotels by rating
# ----------------------------------------------------------
def sort_hotels(hotel_list):    #defines a function to sort hotels by rating 

    return sorted(              #sorts hotels from highest to lowest rating
        hotel_list,
        key=lambda x: x["rating"],   #tells the program to sort by rating 
        reverse=True
    )


# ----------------------------------------------------------
# FUNCTION: Safe numeric input
# Prevents crashes from bad user input
# ----------------------------------------------------------
def get_float_input(message):     #allows the ratings to be entered with decimals 

    while True:

        try:
            value = float(input(message))

            # Prevent negative numbers
            if value < 0:                      #checks to see if the number is positive 
                print("Please enter a positive number.")

            else:                                 #if the number is valid, the program continues
                return value

        # Handle invalid number input
        except ValueError:
            print("Invalid entry. Numbers only please.")


# ----------------------------------------------------------
# FUNCTION: Display matching hotels
# ----------------------------------------------------------
def display_hotels(results):

    print("\n" + "=" * 45)     #prints 45 equal signs to look like the long separator line 
    print("MATCHING HOTELS")
    print("=" * 45)

    # No hotels found
    if len(results) == 0:

        print("No hotels found matching your criteria.")

    else:

        # Display all matching hotels
        for hotel in results:

            print("Hotel Name :", hotel["name"])
            print("Location   :", hotel["location"].title())
            print("Amenities  :", ", ".join(hotel["amenities"]))
            print("Rating     :", hotel["rating"])
            print("Price      : $", hotel["price"])

            print("-" * 45)


# ----------------------------------------------------------
# MAIN PROGRAM
# ----------------------------------------------------------
def main():

    # Create hotel file
    create_file_if_needed()

    while True:

        print("\n" + "=" * 45)
        print("WELCOME TO THE HOTEL SELECTION PROGRAM")
        print("=" * 45)

        # Get destination city
        city_input = input(
            "\nEnter destination city "
            "(or multiple cities separated by commas): "
        ).lower()

        # Prevent blank city input
        if city_input == "":
            print("Please enter at least one city.")
            continue

        # Split city list
        destinations = city_input.split(",")

        # Remove extra spaces
        for i in range(len(destinations)):
            destinations[i] = destinations[i].strip()

        # Get desired amenities
        amenity_input = input(
            "Enter desired amenities "
            "(wifi, breakfast, pool, parking)\n"
            "Press Enter for none: "
        ).lower()

        # Allow empty amenities
        if amenity_input == "":
            amenities = []

        else:

            amenities = amenity_input.split(",")

            # Remove extra spaces
            for i in range(len(amenities)):
                amenities[i] = amenities[i].strip()

        # Get minimum rating
        min_rating = get_float_input(
            "Enter minimum rating (1 to 5): "
        )

        # Prevent ratings above 5
        if min_rating > 5:
            print("Rating cannot be higher than 5.")
            continue

        # Get maximum budget
        max_price = get_float_input(
            "Enter maximum nightly budget: $"
        )

        # Load hotel data
        hotel_data = load_hotels()

        # Find matching hotels
        results = find_hotels(
            hotel_data,
            destinations,
            amenities,
            min_rating,
            max_price
        )

        # Sort results
        sorted_results = sort_hotels(results)

        # Display results
        display_hotels(sorted_results)

        # Ask user if they want another search
        while True:

            again = input(
                "\nWould you like to search again? "     #\n starts a new line
                "(yes/no): "                             #message that is displayed to user
            ).lower()                                    #converts the answer into lowercase

            # Continue program if user chooses 
            if again == "yes":
                break                                    #stops the questioning cycle 

            # Exit program
            elif again == "no":

                print(
                    "\nThank you for using the Hotel Selection Program."
                )

                return

            # Handle invalid answers
            else:
                print(
                    "Invalid entry. Please type yes or no."      
                )


# ----------------------------------------------------------
# RUN PROGRAM
# ----------------------------------------------------------
main()