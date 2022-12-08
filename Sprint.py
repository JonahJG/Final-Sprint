# Final Sprint - HAB Taxi Services
# Authors: Group 5       Date:

import FormatValues as FV
import datetime
Today = datetime.datetime.now()

# Open and read values from Defaults.dat

f = open("Defaults.dat", "r")
NEXT_TRANS_NO = int(f.readline())
NEXT_DRIVER_NO = int(f.readline())
MON_STAND_FEE = float(f.readline())
DAILY_RENT_FEE = float(f.readline())
WEEK_RENT_FEE = float(f.readline())
HST_RATE = float(f.readline())
f.close()

# Menu set-up

while True:
    print("HAB Taxi Services")
    print("Company Services System")
    print()
    print("1. Enter a New Employee (driver).")
    print("2. Enter Company Revenues.")
    print("3. Enter Company Expenses.")
    print("4. Track Car Rentals.")
    print("5. Record Employee Payment.")
    print("6. Print Company Profit Listing")
    print("7. Print Driver Financial Listing.")
    print("8. (TBD)")
    print("9. Quit Program.")
    print()

    # Set up options as functions.

    def NewEmp():

        pass

    def CompRev():

        pass

    def CompExpenses():

        pass

    def CarRentals():

        pass

    def EmpPay():

        pass

    def ProfList():

        pass

    def DriverFinList():

        pass

    def TBD():

        pass

    Choice = int(input("Enter your choice (1-9): "))

    if Choice == 1:

        NewEmp()

    elif Choice == 2:

        CompRev()

    elif Choice == 3:

        CompExpenses()

    elif Choice == 4:

        CarRentals()

    elif Choice == 5:

        EmpPay()

    elif Choice == 6:

        ProfList()

    elif Choice == 7:

        DriverFinList()

    elif Choice == 8:

        TBD()

    elif Choice == 9:
        break





