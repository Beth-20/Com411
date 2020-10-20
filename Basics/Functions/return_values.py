def run():
  def sum_weights(beep_weight, bop_weight):
    total_weight = beep_weight + bop_weight
    return total_weight

  def calc_avg_weight(beep_weight, bop_weight):
    avg_weight = (beep_weight + bop_weight) / 2
    return avg_weight

  def run():
    # Ask user for weight
    print("What is the weight of Bop?")
    bop_weight = float(input())

    print("What is the weight of Beep?")
    beep_weight = float(input())

    print("What would you like to calculate (sum or average)?")
    calculation = input()

    # Carry out calculation
    if (calculation == "sum"):
        answer = sum_weights(beep_weight, bop_weight)
        print("The sum of Beep's and Bop's weight is {:.2f}".format(answer))
    elif (calculation == "average"):
        answer = calc_avg_weight(beep_weight, bop_weight)
        print("The average of Beep's and Bop's weight is {:.2f}".format(answer))
    else:
        print("I am not sure what you would like to do.")
# Call the function
run()