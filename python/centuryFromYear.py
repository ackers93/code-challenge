# Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

# Example

# For year = 1905, the output should be
# centuryFromYear(year) = 20
# For year = 1700, the output should be
# centuryFromYear(year) = 17.
# Input/Output

# [execution time limit] 4 seconds(py3)

# [input] integer year

# A positive integer, designating the year.

# Guaranteed constraints:
# 1 ≤ year ≤ 2005.

# [output] integer

# The number of the century the year is in.


def centuryFromYear(year):
    year_str = str(year)

    if len(year_str) == 4:
        first = year_str[:2]
        second = year_str[2:]

        if int(second) == 0:
            return int(first)
        else:
            return int(first) + 1

    if len(year_str) == 3:
        first_pos = year_str[:1]
        last_bit = year_str[1:]

        if int(last_bit) == 0:
            return int(first_pos)
        else:
            return int(first_pos) + 1

    if len(year_str) <= 2:
        return 1
