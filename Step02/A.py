PIZZA_PRICE = 12.99
SLICE_PRICE = 2.25

host_name = str(input("Name: "))
num_people = int(input("Number of People: "))
slice_per_person = int(input("Slices per person: "))

slices_needed = num_people * slice_per_person
total_cost = ((slices_needed // 8) * PIZZA_PRICE) + ((slices_needed % 8) * SLICE_PRICE)
cost_per_person = total_cost / num_people

print(f"=== Pizza Plan for {host_name}'s Party ===")
print(f"Slices needed: {num_people * slice_per_person}")
print(f"Whole pizzas: {slices_needed // 8}")
print(f"Extra slices: {slices_needed % 8}")
print(f"Total cost: ${total_cost:.2f}")
print(f"Cost per person: ${cost_per_person:.2f}")
