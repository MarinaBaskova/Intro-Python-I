# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE


def is_even(num):
    if (num % 2 == 0):
        return True


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"


def is_even_odd(num):
    if (is_even(num)):
        print("Even!")
    else:
        print("Odd")


# YOUR CODE HERE
is_even_odd(num)
