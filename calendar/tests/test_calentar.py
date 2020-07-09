# pylint: disable=missing-function-docstring,missing-module-docstring
from datetime import date

import pytest

from my_calendar import get_day, CalendarFormatError, is_workday


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019, 12, 31', 2019, 12, 31),
        ('1977, 11, 8', 1977, 11, 8),
        ('2001, 2, 28', 2001, 2, 28)
    ])
def test_get_day_with_comas(day_str, expected_year, expected_month, expected_day):
    expected_date = date(expected_year, expected_month, expected_day)
    day_date = get_day(day_str)

    assert day_date == expected_date


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019 12 31', 2019, 12, 31),
        ('1977 11 8', 1977, 11, 8),
        ('2001 2 28', 2001, 2, 28)
    ])
def test_get_day_with_spaces(day_str, expected_year, expected_month, expected_day):
    expected_date = date(expected_year, expected_month, expected_day)
    day_date = get_day(day_str)

    assert day_date == expected_date


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019/12/31', 2019, 12, 31),
        ('1977/11/8', 1977, 11, 8),
        ('2001/2/28', 2001, 2, 28)
    ])
def test_get_day_with_slash(day_str, expected_year, expected_month, expected_day):
    expected_date = date(expected_year, expected_month, expected_day)
    day_date = get_day(day_str)

    assert day_date == expected_date


@pytest.mark.parametrize(
    "day_str, expected_year, expected_month, expected_day",
    [
        ('2019-12-31', 2019, 12, 31),
        ('1977-11-8', 1977, 11, 8),
        ('2001-2-28', 2001, 2, 28)
    ])
def test_get_day_with_dash(day_str, expected_year, expected_month, expected_day):
    expected_date = date(expected_year, expected_month, expected_day)
    day_date = get_day(day_str)

    assert day_date == expected_date


def test_get_day_with_bad_string():
    bad_string = 'foo'

    with pytest.raises(
            CalendarFormatError,
            match="The date's format is not supported"):
        get_day(bad_string)


def test_workday_with_monday():
    day = date(2020, 7, 6)
    assert is_workday(day)


def test_workday_with_sunday():
    day = date(2020, 7, 5)
    assert not is_workday(day)
