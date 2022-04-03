from datetime import datetime, timedelta

import pytz

from myhours.model import Day
from myhours.validation import validate_sequential_days, validate_start_of_week


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


def test_validate_start_day_no_monday():
    start_date = datetime(year=2022, month=4, day=3, tzinfo=pytz.UTC)  # A sunday

    hours_with_wrong_start_day = {start_date: Day(start_date, 8)}
    errors = validate_start_of_week(hours_with_wrong_start_day)

    assert len(errors) == 1


def test_validate_start_day_monday():
    start_date = datetime(year=2022, month=4, day=4, tzinfo=pytz.UTC)  # A monday

    hours_with_correct_start_day = {start_date: Day(start_date, 8)}
    errors = validate_start_of_week(hours_with_correct_start_day)

    assert len(errors) == 0
