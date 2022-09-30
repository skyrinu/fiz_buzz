# Greetings make program interactive.
print("Welcome to FizzBuzz Generator!")

# Input from user for a range of numbers in which FizzBuzz are wanted to be
# generated in.
user_input = input("Please enter the range of numbers in which you want to "
                   "generate FizzBuzz between in (seperated by a"
                   " space):\n").split()

# Input is taken as a list. List is converted into a range.
numbers = range(int(user_input[0]), int(user_input[1]) + 1)

# The numbers which re divided by 3, are printed as "Fizz". The numbers which are
# divided by 5, are printed as "Buzz". The numbers which are divided by
# both, are printed as "FizzBuzz". At last, rest of the numbers are
# printed as it is.
for number in numbers:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
