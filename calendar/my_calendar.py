"""Simple module to check for working days."""
from datetime import date
import re


class CalendarFormatError(Exception):
    # pylint: disable=missing-class-docstring
    pass


def get_day(day_str):
    """Get the date from a string

    It returns datetime.date day.
    The supporte format are:
    * YYYY, mm, dd -> 2019, 12, 31
    * YYYY mm dd   -> 2019 12 31
    * YYYY/mm/dd   -> 2019/12/31
    * YYYY-mm-dd   -> 2019-12-31
    """
    date_comas_re = '(^[12][0-9]{3})[,/]?[\\s-]?([0-9]+)[,/]?[\\s-]?([0-9]+)'
    match = re.search(date_comas_re, day_str)
    if match:
        year, month, day = match.groups()
        day_date = date(int(year), int(month), int(day))
        return day_date

    raise CalendarFormatError("The date's format is not supported")


def is_workday(day):
    """Get a day and tell if is working day or not

    The day attibute is a datetime.date object.

    Working days: from Monday to Friday
    Non-Working days: Saturday and Sunday
    """
    weekday = day.isoweekday()
    if weekday in range(1, 6):
        return True

    return False
