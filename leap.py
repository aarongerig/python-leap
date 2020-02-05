def leap_year(year: int) -> bool:
    if not isinstance(year, int):
        raise Exception(f'The given year "{year}" is not an integer.')

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
