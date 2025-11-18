# Introduction to While Loops in Python
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Simple while loop of numbers
i = int(input("Enter the current month's number: "))
remaining_Months = 12 - i
while i <= 12:
    print(i)
    i += 1
print("Finish Hard!. You have " + str(remaining_Months) + " months to end the year! ")
print()


# Using while loop and nested If statement with Dictionary keys
month_Conversions = {
    "JAN": "JANUARY",
    "FEB": "FEBRUARY",
    "MAR": "MARCH",
    "APR": "APRIL",
    "MAY": "MAY",
    "JUN": "JUNE",
    "JUL": "JULY",
    "AUG": "AUGUST",
    "SEP": "SEPTEMBER",
    "OCT": "OCTOBER",
    "NOV": "NOVEMBER",
    "DEC": "DECEMBER",
}

user_Key = (input("Enter the 3 letter month key: "))
newUser_Key = user_Key.upper()


while newUser_Key not in month_Conversions:
    print("Sorry, Wrong Answer!")
    tryAgain_Key = (input("Try Again: "))
    print()
    tryAgain_Key = tryAgain_Key.upper()
    if tryAgain_Key in month_Conversions:
        print("Result is: " + month_Conversions.get(tryAgain_Key))
        print("")
        break
else:
    print()
    print("Your Result is: ", month_Conversions.get(newUser_Key, "Thank you!"))

