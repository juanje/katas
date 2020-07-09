import pytest
from my_calendar import get_day, CalendarFormatError
from datetime import date

@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019, 12, 31', '2019', '12', '31'),
        ('1977, 11, 8', '1977', '11', '8'),
        ('2001, 2, 30', '2001', '2', '30')
])
def test_get_day_with_comas(day_str, expected_year, expected_month, expected_day):

    year, month, day =  get_day(day_str)

    assert year == expected_year
    assert month == expected_month
    assert day == expected_day


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019 12 31', '2019', '12', '31'),
        ('1977 11 8', '1977', '11', '8'),
        ('2001 2 30', '2001', '2', '30')
])
def test_get_day_with_spaces(day_str, expected_year, expected_month, expected_day):

    year, month, day =  get_day(day_str)

    assert year == expected_year
    assert month == expected_month
    assert day == expected_day


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019/12/31', '2019', '12', '31'),
        ('1977/11/8', '1977', '11', '8'),
        ('2001/2/30', '2001', '2', '30')
])
def test_get_day_with_slash(day_str, expected_year, expected_month, expected_day):

    year, month, day =  get_day(day_str)

    assert year == expected_year
    assert month == expected_month
    assert day == expected_day


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019-12-31', '2019', '12', '31'),
        ('1977-11-8', '1977', '11', '8'),
        ('2001-2-30', '2001', '2', '30')
])
def test_get_day_with_dash(day_str, expected_year, expected_month, expected_day):

    year, month, day =  get_day(day_str)

    assert year == expected_year
    assert month == expected_month
    assert day == expected_day


def test_get_day_with_bad_string():
    bad_string = 'foo'

    with pytest.raises(
            CalendarFormatError,
            match="The date's format is not supported"):
        get_day(bad_string)
