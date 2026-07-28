# Interactive Data Logger & Calculator
print("--- Welcome to Your First Python Script ---")

# Step A: Collect User Data
user_name = input("What is your name? ")
print(f"Hello, {user_name}! Let's do some quick calculations.")

# Step B: Collect Numbers for Processing
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Step C: Perform Mathematical Operations
total_sum = num1 + num2
product = num1 * num2

# Step D: Display the Results
print("\n--- Calculation Results ---")
print(f"The sum of {num1} and {num2} is: {total_sum}")
print(f"The product of {num1} and {num2} is: {product}")
print("------------------------------------------")