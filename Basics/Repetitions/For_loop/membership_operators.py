# Ask user for a phrase
print("\nWhat phrase can you see?")
phrase = input ()


print("\nReversing...\nThe phrase is:\t", end="")

reversed = ""

# For loop
for letter in phrase:
    reversed = letter + reversed

print(reversed)
