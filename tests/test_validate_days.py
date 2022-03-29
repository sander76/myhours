from datetime import datetime, timedelta

from myhours.model import Day
from myhours.validation import validate_sequential_days


def test_validate_days_sequential_success():
    start_date = datetime.now()

    day_1 = Day(start_date, 8)
    day_2 = Day(start_date + timedelta(days=1), 8)
    days = {day_1.date: day_1, day_2.date: day_2}

    errors = validate_sequential_days(days)
    assert len(errors) == 0


def test_validate_days_sequential_fail_2sep_days():
    start_date = datetime.now()

    day_1 = Day(start_date, 8)
    day_2 = Day(start_date + timedelta(days=2), 8)
    days = {day_1.date: day_1, day_2.date: day_2}

    errors = validate_sequential_days(days)
    assert len(errors) == 1
