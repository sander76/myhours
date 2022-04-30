from datetime import datetime, timedelta

from myhours.model import Day, SortedWorkDays

DAY_STRING = "%Y-%m-%d"


def validate_days(days: SortedWorkDays) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_sequential_days(days))
    errors.extend(validate_hours_per_day(days))
    errors.extend(validate_start_of_week(days))

    return errors


def validate_sequential_days(days: SortedWorkDays) -> list[str]:
    # check if all days are sequential
    errors = []
    iterator = iter(days.values())
    previous_day = next(iterator)

    for day in iterator:
        expected = previous_day.date + timedelta(days=1)

        if not expected == day.date:
            errors.append(
                f"Days have gaps. Expected {expected.strftime(DAY_STRING)}, a {expected.strftime('%A')}, "
                f"got {day.date.strftime(DAY_STRING)}, a {day.date.strftime('%A')} "
            )
        previous_day = day

    return errors


def validate_hours_per_day(days: SortedWorkDays) -> list[str]:
    errors = []
    for day in days.values():
        if day.hours != 8:
            errors.append(
                f"Day {day.date.strftime(DAY_STRING)} has {day.hours} registered."
            )
    return errors


def validate_start_of_week(days: dict[datetime, Day]) -> list[str]:
    errors = []

    first_day = list(days.keys())[0]

    if not first_day.isoweekday() == 1:
        errors.append(
            f"First entry is not a monday. Got {first_day.strftime('%A')} [{first_day.strftime(DAY_STRING)}]"
        )
    return errors
