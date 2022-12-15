# Final Sprint - HAB Taxi Services
# Authors: Group 5       Date:

import FormatValues as FV
import datetime
from datetime import date
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

# Automatic stand fees set-up

if Today.day == 1:

    FEE_DATE = Today
    MONTHLY_STAND_FEES = "Monthly Stand Fees"

    f = open("Revenues.dat", "w")

    f.write("{}\n".format(str(NEXT_TRANS_NO)))
    f.write("{}\n".format(FV.FDateS(FEE_DATE)))
    f.write("{}\n".format(str(MONTHLY_STAND_FEES)))
    f.write("{}\n".format(str(NEXT_DRIVER_NO)))
    f.write("{}\n".format(str(MON_STAND_FEE)))
    f.write("{}\n".format(str(DAILY_RENT_FEE)))
    f.write("{}\n".format(str(WEEK_RENT_FEE)))

    f.close()

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

    while True:

        # Print out top of report

        StartDate = date(2022, 12, 0o1)
        Today = datetime.datetime.now()
        print()
        print("HAB TAXI SERVICES")
        print(f"COMPANY PROFIT LISTING FROM {StartDate} TO {FV.FDateS(Today)} ")
        print()
        print("TRANSACTION  TRANSACTION   TRANSACTION      DRIVER     REVENUE      HST   TOTAL       TIPS ")
        print("    ID          DATE       DESCRIPTION      NUMBER                        REVENUE")
        print("===========================================================================================")

        # Set counter to 0, set accumulator to 0
        TransCtr = 0
        TotRevAcc = 0

        # Open Revenues.dat to read

        f = open("Revenues.dat", "r")

        for CustDataLine in f:
            CustLine = CustDataLine.split(",")
            TransDate = CustLine[1].strip()
            TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")

            if TransDateP.month == 12:
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransID = int(CustLine[0].strip())
                TransDescrip = CustLine[2].strip()
                DriverNo = int(CustLine[3].strip())
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotalRev = Total + Tips

                print(f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotalRev

        f.close()
        print("===========================================================================================")
        print(f"NO. TRANSACTIONS: {TransCtr:>3d}                                             TOTAL REVENUE: {FV.FDollar2(TotRevAcc):>9s}")
        print()

        Cont = input("ENTER 'END' TO QUIT: ").upper()
        if Cont == "END":
            break
        else:
            print("Please enter 'END' to quit.")


def DriverFinList():

    pass


def EmpRevList():

    while True:
        # User input
        print()
        print("HAB TAXI SERVICES")
        print("PRINT A DRIVER REVENUE REPORT")
        print()
        DriverNum = int(input("Enter the driver number: "))
        # Print out top of report

        StartDate = date(2022, 12, 0o1)
        Today = datetime.datetime.now()
        print()
        print("HAB TAXI SERVICES")
        print(f"EMPLOYEE REVENUE REPORT FROM {StartDate} TO {FV.FDateS(Today)} ")
        print()
        print("TRANSACTION  TRANSACTION   TRANSACTION      DRIVER     REVENUE      HST   TOTAL       TIPS ")
        print("    ID          DATE       DESCRIPTION      NUMBER                        REVENUE")
        print("===========================================================================================")

        # Set counter to 0
        TransCtr = 0
        TotRevAcc = 0

        # Open Revenues.dat to read

        f = open("Revenues.dat", "r")

        for CustDataLine in f:
            CustLine = CustDataLine.split(",")
            DriverNo = int(CustLine[3].strip())

            if DriverNo == 1968 and DriverNum == 1968:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 1111 and DriverNum == 1111:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 2222 and DriverNum == 2222:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev


            elif DriverNo == 3333 and DriverNum == 3333:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 2076 and DriverNum == 2076:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 1978 and DriverNum == 1978:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 2106 and DriverNum == 2106:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 2001 and DriverNum == 2001:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

            elif DriverNo == 2301 and DriverNum == 2301:
                TransID = int(CustLine[0].strip())
                TransDate = CustLine[1].strip()
                TransDateP = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDate = datetime.datetime.strptime(TransDate, "%Y-%m-%d")
                TransDescrip = CustLine[2].strip()
                TransAmt = float(CustLine[4].strip())
                HST = float(CustLine[5].strip())
                Total = float(CustLine[6].strip())
                Tips = float(CustLine[-1].strip())

                TransDescripDsp = "{:.15}".format(TransDescrip)
                TotRev = Total + Tips

                print(
                    f"   {TransID:>4d}       {FV.FDateS(TransDate)}   {TransDescripDsp:<15s}  {DriverNo:<4d}    {FV.FDollar2(TransAmt):>9s}  {FV.FDollar2(HST):>9s} {FV.FDollar2(Total):>7s} {FV.FDollar2(Tips):>9s}")
                TransCtr += 1
                TotRevAcc += TotRev

        f.close()
        print("===========================================================================================")
        print(f"NO. TRANSACTIONS: {TransCtr:>3d}                                             TOTAL REVENUE: {FV.FDollar2(TotRevAcc):>9s}")

        print()
        Cont = input("ENTER 'END' TO QUIT: ").upper()
        if Cont == "END":
            break
        else:
            print("Please enter 'END' to quit.")


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
    print("8. Print Driver Revenue Report.")
    print("9. Quit Program.")
    print()

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

        EmpRevList()

    elif Choice == 9:
        break










