# Ask user for book cover type
def run():
  print("What type of cover does this book have?")
  book = input()

# Display appropriate message according to book cover
  if (book.lower() == "soft"):
    print("Is the book perfect-bound?")
    bound = input()

    if (bound.lower() == "yes"):
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with a perfect bound create perfect and clean edges, you should definitely purchase one!") 
  else:
    print("Did you know that, books with hard covers can be more expensive! .. just something to consider")

  
















