import random

magic_numbers = []
greatest = -1
# generate 10 random numbers
for number in range(0, 9):
    num = random.randint(0, 9)
    magic_numbers.insert(num, number)
    if num > greatest:
        greatest = num
# magic_numbers = [random.randint(0, 9), random.randint(0,9)]

print("The greatest number is {}".format(greatest))

chances = 3

for attempt in range(chances): # range(chances) is [0,1,2]
    print("This is attempt {}".format(attempt))
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:
        print("You got it right!")
    if user_number not in magic_numbers:
        print("You didn't get it")