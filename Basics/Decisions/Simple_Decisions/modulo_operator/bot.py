# Asking the user for a whole number
print("Please enter a whole number")
number = int(input())

# Display necessary message for even and odd numbers
if (number % 2 == 0):
    print("\nThe number {} is an even number.".format(number))
else:
    print("\nThe number {} is an odd number.".format(number))