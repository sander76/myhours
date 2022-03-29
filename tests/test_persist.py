from datetime import datetime, timedelta

from myhours.persist import compose_filename


def test_compose_filename():
    start = datetime(year=2020, month=2, day=9)
    stop = start + timedelta(days=3)

    fname = compose_filename(start, stop)

    assert fname == "2020_02_09__2020_02_12.xlsx"
