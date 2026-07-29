# Artistofall Producxionz - Client Rate & Budget Estimator
print("--- Artistofall Producxionz: Quote Generator ---")

# Step A: Collect Client & Project Details
client_name = input("Enter client name: ")
print(f"Generating estimate for: {client_name}")

print("\nSelect Service Tier:")
print("1. Photography Portrait Session ($150 flat rate)")
print("2. Commercial Video Production ($75 per hour)")
choice = input("Enter option number (1 or 2): ")

# Step B: Process Conditional Logic & Calculations
if choice == "1":
    service_type = "Photography Portrait Session"
    total_cost = 150.0
    print(f"Selected: {service_type}")

elif choice == "2":
    service_type = "Commercial Video Production"
    hours = float(input("Enter total production hours: "))
    hourly_rate = 75.0
    total_cost = hours * hourly_rate
    print(f"Selected: {service_type} ({hours} hours @ ${hourly_rate}/hr)")

else:
    service_type = "Custom Media Package"
    total_cost = 300.0
    print("Invalid option selected. Defaulting to Custom Media Package base rate.")

# Step C: Output Final Professional Quote Summary
print("\n" + "="*40)
print(f" OFFICIAL QUOTE: ARTISTOFALL PRODUCXIONZ")
print("="*40)
print(f" Client: {client_name}")
print(f" Service: {service_type}")
print(f" Total Estimated Cost: ${total_cost:.2f}")
print("="*40)
print(" Thank you for doing business with us!")