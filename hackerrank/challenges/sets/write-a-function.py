def is_leap(year):
    if (year % 400 == 0 or year % 100 == 0 or year % 4 == 0):
        return True;

    return False


print(is_leap(int(input())))
