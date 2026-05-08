# Hotel Selection Program

## Project Overview

The Hotel Selection Program is a Python-based application designed to help travelers find hotels that best match their personal preferences and travel needs. The program allows users to search for accommodations by entering a destination city, desired hotel amenities, minimum customer rating, and maximum nightly budget. Based on the user’s input, the program filters available hotels and displays matching results sorted from highest-rated to lowest-rated hotels.

This project demonstrates the use of Python programming concepts including functions, loops, conditional statements, lists, dictionaries, file handling, sorting, exception handling, and user input validation. The system also uses a centralized hotel database file to store and retrieve hotel information efficiently.

---

# Project Goals

The main goal of this project is to simplify the hotel search process by providing travelers with personalized hotel recommendations based on their preferences. The program is designed to be beginner-friendly, easy to use, and capable of handling invalid user input without crashing.

The project also focuses on demonstrating proper software development practices such as:
- Modular programming using functions
- Reusable and organized code
- Error handling
- User-friendly interface design
- File management
- Program documentation and comments

---

# Features

## Hotel Search by Destination
Users can enter one or multiple destination cities to search for hotels in specific locations.

Example:
```text
atlanta
miami
new york
```

---

## Amenity Filtering
Users can filter hotels based on amenities such as:
- Wi-Fi
- Breakfast
- Parking
- Pool

The program checks hotel amenities and only displays hotels that match the user's requested features.

---

## Customer Rating Filter
Users can enter a minimum customer rating between 1 and 5. Hotels below the selected rating are excluded from the search results.

Example:
```text
Minimum Rating: 4.5
```

---

## Budget Filtering
Users can enter a maximum nightly budget to find affordable hotel options within their price range.

Example:
```text
Maximum Budget: $200
```

---

## Hotel Sorting
Matching hotels are automatically sorted by customer rating from highest to lowest using Python's `sorted()` function and a lambda expression.

---

## File Handling
The program uses a text file named `hotels.txt` as a hotel database. The file stores:
- Hotel names
- Locations
- Amenities
- Ratings
- Prices

The program automatically creates the file if it does not already exist.

---

## Error Handling
The program includes error handling to prevent crashes caused by invalid user input. Users are prompted to correct mistakes such as:
- Entering letters instead of numbers
- Negative numbers
- Invalid yes/no responses
- Blank city entries

---

# Technologies Used

- Python
- VS Code
- GitHub
- File Handling
- Dictionaries
- Lists
- Functions
- Loops
- Exception Handling

---

# Program Structure

The project is organized into several functions:

| Function | Purpose |
|---|---|
| `create_file_if_needed()` | Creates the hotel database file if missing |
| `load_hotels()` | Reads hotel data from the file |
| `find_hotels()` | Filters hotels based on user preferences |
| `sort_hotels()` | Sorts hotels by customer rating |
| `get_float_input()` | Safely handles numeric user input |
| `display_hotels()` | Displays matching hotel results |
| `main()` | Controls overall program flow |

---

# Sample Program Output

```text
=============================================
WELCOME TO THE HOTEL SELECTION PROGRAM
=============================================

Enter destination city: miami
Enter desired amenities: wifi
Enter minimum rating: 4
Enter maximum nightly budget: 200

=============================================
MATCHING HOTELS
=============================================

Hotel Name : Ocean Breeze Hotel
Location   : Miami
Amenities  : wifi, pool, parking
Rating     : 4.7
Price      : $150
```

---

# Future Improvements

Possible future improvements for this project include:
- Graphical User Interface (GUI)
- Online hotel API integration
- Hotel reservation system
- Customer review submission
- Search history tracking
- Database integration using SQL
- Advanced hotel ranking system
- Mobile application version

---

# Conclusion

The Hotel Selection Program successfully demonstrates how Python can be used to create a practical and user-friendly hotel recommendation system. The project combines multiple programming concepts into a single application that is functional, organized, and easy to maintain. By using file handling, functions, sorting, and input validation, the program provides travelers with a simplified way to search for hotels based on their individual preferences and budget requirements.

---

# Author

Adrienne Rodgers/Jaqaesa Mays
