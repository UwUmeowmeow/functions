"""function to print name a given number of times
"""


def print_name(name, number):
    for person in range(0, number):
        print(name)


# Main routine
name_ = input("Enter name to print: ")
number_ = int(input("Times to ping: "))
print_name(name_, number_)
