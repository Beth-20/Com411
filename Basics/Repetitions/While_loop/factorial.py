# Ask user for a number
print("\nPlease enter a number")
number = int(input())

# Variable
count = 0
total = 1 

while ( count < number):
  count = count + 1
  total = total * count

print("the factorial is", total)
