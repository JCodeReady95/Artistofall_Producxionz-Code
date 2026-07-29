# Artistofall Producxionz - Equipment Inventory & Asset Logger
print("--- Artistofall Producxionz: Equipment Tracker ---")

# Step A: Define the Equipment List
studio_equipment = [
    "Canon EOS Rebel T7 Camera Body",
    "Canon EFS 18-55mm Lens",
    "Canon Zoom Lens EF 75-300mm III",
    "7 SD Cards",
    "2 Camera Batteries with Charger"
]

# Step B: Display Total Asset Count
total_items = len(studio_equipment)
print(f"\nTotal Tracked Inventory Items: {total_items}")
print("="*45)
print("CURRENT REGISTERED STUDIO GEAR:")
print("="*45)

# Step C: Loop Through and Print Each Item
for index, item in enumerate(studio_equipment, start=1):
    print(f"[{index}] {item} - Status: Secure & Verified")

print("="*45)
print("Inventory check completed successfully.")