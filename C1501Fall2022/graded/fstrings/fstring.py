GST = 0.05

amount = float(input("Enter the pre-tax total of your order: "))
total = amount * (1 + GST)

# Modify the following line to display the total with exactly 2 decimal places.
# Include a comment citing your source!
print("Before tax: $", amount)
print("Total:      $", total)