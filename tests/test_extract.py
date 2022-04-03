from datetime import datetime, timedelta
from pathlib import Path

import pytest

from myhours.extract import _sort_dict, extract_days, open_xlsx
from myhours.model import Day


@pytest.fixture
def sheet():
    xls_file = Path(__file__).parent / "test_sheet.xlsx"

    sheet = open_xlsx(xls_file)
    return sheet


def test_get_sheet(sheet):

    days = extract_days(sheet)

    assert len(days) == 5


def test_sheet_day_hours(sheet):
    days = extract_days(sheet)

    hours = [4, 8, 11, 8, 8]

    actual = [day.hours for day in days.values()]

    assert actual == hours


def test_sort_days():
    date1 = datetime.now()
    date2 = date1 - timedelta(days=1)
    unsorted = {date1: Day(date1, 8), date2: Day(date2, 8)}

    sorted_days = _sort_dict(unsorted)

    sorted_date = list(sorted_days.keys())
    assert sorted_date[0] == date2
