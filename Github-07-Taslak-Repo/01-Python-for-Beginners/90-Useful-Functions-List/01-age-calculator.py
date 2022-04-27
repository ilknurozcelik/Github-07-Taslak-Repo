#muce
from datetime import date, datetime


def age_calculator():

    birth = input("Your Birth Date: (DAY.MOON.YEAR) ")

    to_ordinal_date1 = datetime.strptime(birth, "%d.%m.%Y").toordinal()
    to_ordinal_date2 = datetime.today().toordinal()

    ordinal = (to_ordinal_date2 - to_ordinal_date1)     # ordinal
    gregorian = date.fromordinal(ordinal)               # Gregorian Ordinal

    print(f"Your Life Day: {ordinal}")
    print(f'Your Age (Gregorian): {gregorian}')


if __name__ == "__main__":
    age_calculator()
