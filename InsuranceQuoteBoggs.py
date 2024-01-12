"""
Abigail Boggs
amboggs@dmacc.edu
Last Edited: 1/9/24
Module 1, Topic 4: Insurance Quote Assignment
Calculate an insurance quote based on age, coverage type, and past accident history
"""


# Gather User Info: Driver Name (String), Driver Age(int), Coverage Level(String (SM, L, F))
# use try/except to insure the user input is valid
def getting_input_and_test():
    test_pass = False
    while test_pass is False:
        try:
            d_name = input("Enter Driver Name: ")
            while d_name == " " or d_name == "":
                d_name = input("Name cannot be blank, please try again")

            d_age = input("Enter Driver Age: ")
            while int(d_age) < 16:
                print("Driver's age cannot be less than 16, please try again")
                d_age = input("Enter Driver Age: ")

            print("Enter Coverage Level Desired: (see list below)")
            coverage = input("State Minimum: SM,\nLiability Coverage: L,\nFull Coverage: F")
            coverage = coverage.upper()
            while coverage != "SM" and coverage != "L" and coverage != "F":
                print("Invalid option, please use abbreviations SM, L, Or F")
                coverage = input(" State Minimum: SM,\nLiability Coverage: L,\nFull Coverage: F:    \n")

            # if it makes it to this point with no errors, the driver info is correct and is added to dict
            # store in dict
            driver_in = {
                "Name": d_name,
                "Age": int(d_age),
                "Coverage": coverage,
                "Price": float(0)
            }
            # pass the test
            test_pass = True
            return driver_in
        except ValueError:
            print("Age must be a whole number")


def determine_price(driver_in):
    # add customer's coverage cost to dictionary according to their age and coverage desired using the table
    # created a dict with an internal dict for easy searching for the right coverage, avoiding all of the
    # extended if/else statements
    age16 = {"SM": 2593, "L": 2957, "F": 6930}
    age25 = {"SM": 608, "L": 691, "F": 1745}
    age35 = {"SM": 552, "L": 627, "F": 1564}
    age45 = {"SM": 525, "L": 596, "F": 1469}
    age55 = {"SM": 494, "L": 560, "F": 1363}
    age65 = {"SM": 515, "L": 585, "F": 1402}
    coverage_chart = {"16": age16, "25": age25, "35": age35, "45": age45, "55": age55, "65": age65}

    c = driver_in["Coverage"]
    if 16 <= driver_in["Age"] < 25:
        for x, y in coverage_chart["16"].items():
            if x == c:
                driver_in["Price"] = y
    elif 25 <= driver_in["Age"] < 35:
        for x, y in coverage_chart["25"].items():
            if x == c:
                driver_in["Price"] = y
    elif 35 <= driver_in["Age"] < 45:
        for x, y in coverage_chart["35"].items():
            if x == c:
                driver_in["Price"] = y
    elif 45 <= driver_in["Age"] < 55:
        for x, y in coverage_chart["45"].items():
            if x == c:
                driver_in["Price"] = y
    elif 55 <= driver_in["Age"] < 65:
        for x, y in coverage_chart["55"].items():
            if x == c:
                driver_in["Price"] = y
    elif driver_in["Age"] >= 65:
        for x, y in coverage_chart["65"].items():
            if x == c:
                driver_in["Price"] = y
    else:
        print("Driver age not found")

    # ask if user had any accidents
    accidents = input("Have you had any accidents? Y/N: ")
    while accidents.upper() != "Y" and accidents.upper() != "N":
        accidents = input("Please enter Y/N: ")
    # - if yes increase the coverage rate by 41%
    if accidents.upper() == "Y":
        # update the customers coverage cost in the dict
        print(driver_in["Price"])
        driver_in["Price"] = driver_in["Price"] * 1.41
        print(driver_in["Price"])

    # ask use if the want to pay up front for a 10% discount
    pay_up_front = input("Would you like to pay up front for a 10% discount? Y/N: ")
    while pay_up_front.upper() != "Y" and pay_up_front.upper() != "N":
        pay_up_front = input("Please enter Y or N: ")

    # - if yes update the dict with new amount (-10%)
    if pay_up_front.upper() == "Y":
        driver_in["Price"] = driver_in["Price"] * .90

    return driver_in["Price"]


# Driver Code
driver_info = getting_input_and_test()

price = determine_price(driver_info)

# output the annual insurance cost for the customer
formatted_price = "{:,.2f}".format(price)
print("Your annual insurance cost is: $" + str(formatted_price))
