print("\nProgram started!")
print("\nPlease enter a letter")
letter = input()

if len(letter) == 1:
    print("The ASCII code for {} is {}".format(letter,ord(letter)))
else:
    print("Error, more than one character entered")
    
    
print("Program ended!")
