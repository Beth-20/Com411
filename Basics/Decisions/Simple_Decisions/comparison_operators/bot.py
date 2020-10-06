# Ask the user for a number
print("Please enter a number")
number1 = int(input())
print("please enter another number")
number2 = int(input())

# Determine which message to display for smallest number
if (number1 < number2):
    print("\nThe first number is the smallest.")
elif (number1 > number2):
    print("\nThe second number is the smallest.")
else:
    print("\nThe two numbers are equal.")