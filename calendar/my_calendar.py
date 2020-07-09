from datetime import date
import re

class CalendarFormatError(Exception):
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
