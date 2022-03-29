import shutil
from datetime import datetime
from pathlib import Path


def compose_filename(start_date: datetime, stop_date: datetime) -> str:
    day_format = "%Y_%m_%d"
    start = start_date.strftime(day_format)
    stop = stop_date.strftime(day_format)
    return f"{start}__{stop}.xlsx"


def save_xlsx(source_file: Path, target_file: Path) -> None:
    shutil.copy(source_file, target_file)
