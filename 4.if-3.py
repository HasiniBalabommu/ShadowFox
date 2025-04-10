# Define city lists for each country
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

# Create a dictionary to map cities to their countries
city_to_country = {}

for city in Australia:
    city_to_country[city] = "Australia"
for city in UAE:
    city_to_country[city] = "UAE"
for city in India:
    city_to_country[city] = "India"

# Get user input
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()

# Check if both cities are in the dictionary
if city1 in city_to_country and city2 in city_to_country:
    if city_to_country[city1] == city_to_country[city2]:
        print(f"Both cities are in {city_to_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")
