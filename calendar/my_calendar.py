import re

class CalendarFormatError(Exception):
    pass

def get_day(day_str):
    """Get date from string and convert into a touple with
    the year, the month and the day.
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
        return (year, month, day)

    raise CalendarFormatError("The date's format is not supported")
