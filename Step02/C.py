# Road Trip Calculator
# Calculates gas usage, cost, and driving time for a road trip.

AVERAGE_SPEED = 55

# Input
destination = input("Destination: ")
miles = float(input("Trip distance (miles): "))
miles_per_gallon = float(input("Car's miles per gallon: "))
gas_price = float(input("Gas price per gallon: "))
people = int(input("Number of people splitting the cost: "))

# Processing
gallons = miles / miles_per_gallon
gas_cost = gallons * gas_price
cost_per_person = gas_cost / people
minutes = int(miles / AVERAGE_SPEED * 60)
hours = minutes // 60
leftover_minutes = minutes % 60
round_trip_gas = gas_cost * 2

# Output
print()
print(f"--- Trip to {destination} ---")
print(f"Gallons of gas:   {gallons:.1f}")
print(f"Gas cost:         ${gas_cost:.2f}")
print(f"Cost per person:  ${cost_per_person:.2f}")
print(f"Driving time:     {hours} hr {leftover_minutes} min (at {AVERAGE_SPEED} mph)")
print(f"Round trip gas:   ${round_trip_gas:.2f}")