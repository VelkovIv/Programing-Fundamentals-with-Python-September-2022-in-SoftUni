import re

input_destinations = input()
real_destinations = []
travel_points = 0

pattern = r'(=|\/)([A-Z][A-za-z]{2,})\1'

destinations = re.finditer(pattern, input_destinations)

for destination in destinations:
    # print(destination.groups()[1])
    current_location = destination.groups()[1]
    travel_points += len(current_location)
    real_destinations.append(current_location)

print(f"Destinations: {', '.join(real_destinations)}")
print(f"Travel Points: {travel_points}")
