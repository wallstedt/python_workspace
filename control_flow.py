words = ['cat', 'window', 'defenestrate', 'st']

# print the words
for word in words:
    print(word)

# if:s in loop
for word in words:
    if len(word) > 3:
        print(word + " longer than 3")
    elif len(word) < 3:
        print(word + " shorter than 3")
    else:
        print(word + " is exactly 3")

# ranges

print("Print 5..9")
# prints 5..9
for i in range(5, 10):
    print(i)

print("Print every other number")
# prints every other
for i in range(0, 10, 2):
    print(i)