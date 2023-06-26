# list of all month days
month_list = {1:31 , 2:28 , 3:31 , 4:30 , 5:31 , 6:30 , 7:31 , 8:31 , 9:30 , 10:31 , 11:30 , 12:31}
try:
    print("\t******* Welcome *******")
    # year input
    print("")
    year = int(input("Enter year : "))
    print("1. January")
    print("2. Febuary")
    print("3. March")
    print("4. April")
    print("5. May")
    print("6. June")
    print("7. July")
    print("8. August")
    print("9. September")
    print("10. October")
    print("11. November")
    print("12. December")
    print("")
    # month input
    month = int(input("Enter month :"))
    # day input
    day = int(input("Enter day :"))
    # age in year
    n_year = 2023-year
    # age in months
    if month>=1 and month<12:
        n_month = 12-month
    else:
        n_month = 0
    # age in days
    if day>=1 and day<=31:
        for i in month_list:
            if i == month:
                n_day = month_list[i] - day
                break

    # result print
    if n_month == 0:
        print(f"\n{n_year} Year  {n_day} Day\n")
    else:
        print(f"\n{n_year} Year  {n_month} Month  {n_day} Day\n")

except ValueError:
    print("Error ::: It seems whether you do not enter any decision or whether you enter an alphabet.Try Again!")