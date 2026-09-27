def is_leap(Year):
    if Year % 4 == 0:
        if Year % 100 == 0:
            if Year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(Shal = 2022, mash = 2):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(Shal):
        month_days[1] = 29
    return month_days[mash - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)







