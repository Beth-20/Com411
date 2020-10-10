# Ask use for phrase
print("\nWhat phrase can you see?")
phrase = input ()

print("\nReversing...\nThe phrase is: \t", end="")

#For loop
for position in range(len(phrase) - 1, -1, -1):
    print(phrase[position], end="")