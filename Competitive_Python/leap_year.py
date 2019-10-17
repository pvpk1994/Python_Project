'''
Leap Year Calculation
Author: Pavan Kumar Paluri
'''

'''
Description:
In the Gregorian calendar three criteria must be taken into account to identify leap years:
The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
'''


def is_leap_year(year_c: int):
    leap = False
    if year_c % 4 == 0:
        if year_c % 100 == 0:
            if year_c % 400 == 0:
                leap = True
                return leap
            else:
                leap = False
                return leap
       # print('entering')
        leap = True
        return leap
    return leap


if __name__ == '__main__':
    year = int(input('Enter the year:'))
    if year < 1900:
        raise AssertionError('Year range: 1900 <= year <= 10^5')
    elif year > pow(10, 5):
        raise AssertionError('Year range: 1900 <= year <= 10^5')
    elif year < 0:
        raise AssertionError('Year cannot be negative')
    print(is_leap_year(year))