# Start
print("\nHello its me Beep! After all that you have helped me with so far I think I should get to know you more!")
print("\n Can you please remind me of your name?")
Name = input ()

print("\nThank you!, Now", Name, "do you live in the Northern or Southern Hemisphere?")
Hemisphere = input ()

# If, Elif, Else
if (Hemisphere.lower() == "southern"):
    print("\nBeep understands that the weather tends to be colder in this region!")
elif (Hemisphere.lower() == "northern"):
    print("\nBeep understands that the weather tends to be warmer in this region!")
else: 
    print("\nBeep does not understand where this is?")

# Nested Hobbies with or operator, If, Elif and else
print("\nWhat is one of your Interets / Hobbies? Sport, Music or Gaming?")
Hobbie = input ()

# Sport
if (Hobbie.lower() == "sport"):
    print("\nWhich sport do you like?")
    Sport = input()

    if (Sport.lower() == "football") or (Sport.lower() == "tennis"):
        print("\nWow! Beep loves this too!")
    else: 
        print("\nBeep only usually likes to watch sport, taking part is very tiring")

# Music
elif (Hobbie.lower() == "music"):
    print("\nWhat tpye of instrument do you play?")
    Music = input()

    if (Music.lower() == "guitar" or Music.lower() == "violin"):
        print("\nBeep loves the strings, so inspiring!")
    else:
       print("\nBeep loves music, but only tends to listen to this style and not play")

# Gaming
elif (Hobbie.lower() == "gaming"):
    print("\nWhat type of games do you play?")
    Game = input()

    if (Game.lower() == "horror" or Game.lower() == "puzzle"):
        print("\nBeep avoids these games, they are too difficult!")
    else:
       print("\nBeep loves to play these too but only if they are not too challenging!")

# And operator, or operator, if and else
print("\n After participating in your hobbie do you prefer to relax with a cup of Tea or coffee", Name,"?")
Prefer = input ()

print("\nDo you have sugar, Yes or no?")
Sugar = input()

if ((Prefer.lower() == "tea" or "coffee") and (Sugar.lower() == "yes")):
    print("\nIn that case make sure to brush your teeth well!")
else:
    print("\nNot many people drink Tea or Coffee without sugar!")

# End and Not operator
print("\nThank you for talking with me, Beep! Getting to know you has been good fun, do you consider us friends?")
Friend = input ()
if not (Friend.lower() == "yes"):
  print("Oh, Beep apoligises for wasting your time")
else:
    print("\nHooray! Beep now has 2 friends! Bop and", Name)

print("\nHow many friends do you have",Name,"?")
Total = int(input())

if (Total % 2 == 0):
    print("\nThe number {} is an even number, Beep loves even numbers and would also love to meet your friends!.".format(Total))
else:
    print("\nThe number {} is an odd number, Beep wonders if your friends are also odd!.".format(Total))

