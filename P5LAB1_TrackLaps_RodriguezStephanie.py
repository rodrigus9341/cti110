# Define your function here 
def main():

    user_miles = float(input())

    laps = miles_to_laps(user_miles)

    print("{:.2f}".format(laps))
  


def miles_to_laps(user_miles):

    laps = user_miles / 0.25

    return laps


if __name__ == '__main__':
    main()
    # Type your code here. Your code must call the function. 