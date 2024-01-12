"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited 1/11/24
Gathering Input Functions Assignment
"""


def how_many_integers():
    num_integers = 0
    while True:
        try:
            num_integers = int(input("How many integers would you like to store? "))
            # the number of integers must be at least 1
            if num_integers < 1:
                raise ValueError
        except ValueError:
            # if the user enters bad data, they should be told it's bad and be allowed to enter another integer
            print("Error, number must be an integer, and at least 1. Example: 20, try again. ")
            # !!! IMPORTANT: when testing uncomment raise below !!!
            # raise
            continue
        else:
            break
    return num_integers


def integers_to_store(num_of_integers=1):
    # function should have an input parameter with a default value
    integer_list = []
    for x in range(num_of_integers):
        while True:
            try:
                # default value should be used for each integer request except the last one
                if x == (num_of_integers - 1):
                    # which should override the parameter with something like "Enter your last integer: "
                    value = int(input("Enter your last integer: "))
                else:
                    value = int(input("Enter integer " + str(x) + ": "))
                print("Value " + str(value) + " has been added to the list")
                integer_list.append(value)
            except ValueError:
                # numbers must be integers
                # if the user enters bad data, they should be told it's bad and be allowed to enter
                # another integer
                print("Error, numbers must be integers: ")
                # !!! IMPORTANT: when testing uncomment raise below !!!
                # raise
                continue
            else:
                break
    return integer_list


# Driver Code
if __name__ == "__main__":
    number_of_ints = how_many_integers()
    integers_list = integers_to_store(number_of_ints)

    # once the user has entered correct number of integers the program should print the list of integers
    print("Integers: " + str(integers_list))

    average = 0
    total = 0
    count = 0
    for each in integers_list:
        total = total + each
        count = count + 1
    average = total / count
    # program should then print the average value of the integers in the list
    print("Average of List: " + str(average))

    # along with working program, you must also submit your working unit tests for your functions
    # - your unit tests should assert that bad input raises the expected errors
