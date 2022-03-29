from pathlib import Path

import pytest

from myhours.extract import extract_days, open_xlsx


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
