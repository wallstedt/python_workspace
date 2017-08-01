import random

def menu():
    # ASk player for numbers
    # calc lottery numbers
    # Print out the winnings
    player_numbers = get_player_numbers()
    lottery_numbers = create_lottery_numbers()
    winners = lottery_numbers.intersection(player_numbers)
    print("You won ${}!".format(100 ** len(winners)))

def get_player_numbers():
    number_csv = input("Enter your 6 numbers, separated by commas: ")
    # Now create a set of ints from this number_csv
    number_list = number_csv.split(",")
    integer_set = {int(number) for number in number_list}
    return integer_set

def create_lottery_numbers():
    values = set() # initialize an empty set
    while len(values) < 6: # run til values length == 6
        values.add(random.randint(1, 20))
    return values

menu()