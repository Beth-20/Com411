# Ask the user for whole numbers
print("Please enter a whole number")
number1 = int(input())
print("Please enter another whole number")
number2 = int(input())
print("Please print another whole number")
number3 = int(input())

evennumbers = 0
oddnumbers = 0 

# Determine which numbers are even and which are odd
if (number1 % 2 == 0):
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1

if (number2 % 2 == 0):
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1

if (number3 % 2 == 0):
    evennumbers = evennumbers + 1
else:
    oddnumbers = oddnumbers + 1

# Display result
print("There were {} even and {} odd numbers.".format(evennumbers, oddnumbers))