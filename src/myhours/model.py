from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path


@dataclass
class Detail:
    hours: int
    kind: str


@dataclass
class Day:
    date: datetime
    hours: int = 0
    details: list[Detail] = field(default_factory=list)

    def add_work(self, hours: int, work_kind: str) -> None:
        self.hours += hours
        self.details.append(Detail(hours, work_kind))


@dataclass
class Sheet:
    org_filename: Path
    days: dict[datetime, Day] = field(default_factory=dict)


SortedWorkDays = dict[datetime, Day]
