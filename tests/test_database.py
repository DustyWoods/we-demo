from datetime import date
from pathlib import Path

from we_demo.infrastructure.database import WeightRecord, Database

def test_add():
    record = WeightRecord(date=date(2026, 9, 9), weight=81.1)

    with Database(Path(":memory:")) as db:
        db.add(record)
        records = db.get_range(date(2026, 9, 9), date(2026, 9, 9))

    assert records == [record]


def test_update():
    first = WeightRecord(date=date(2026, 9, 9), weight=80.2)
    second = WeightRecord(date=date(2026, 9, 9), weight=78.2)

    with Database(Path(":memory:")) as db:
        db.add(first)
        db.add(second)
        records = db.get_range(date(2026, 9, 9), date(2026, 9, 9))

    assert records == [second]


def test_get_range():
    records = [
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 3), 79.3),
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 5), 66.3),
    ]

    with Database(Path(":memory:")) as db:
        for record in records:
            db.add(record)

        result = db.get_range(date(2026, 1, 3), date(2026, 1, 4))

    assert result == records[1:3]


def test_get_range_empty():
    with Database(Path(":memory:")) as db:
        result = db.get_range(date(2026, 1, 3), date(2026, 1, 4))

    assert result == []


def test_get_range_order():
    records = [
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 5), 66.3),
        WeightRecord(date(2026, 1, 3), 79.3),
    ]

    expected = [
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 3), 79.3),
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 5), 66.3),
    ]

    with Database(Path(":memory:")) as db:
        for record in records:
            db.add(record)

        result = db.get_range(date(2026, 1, 2), date(2026, 1, 5))

    assert result == expected


def test_get_all():
    records = [
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 3), 79.3),
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 5), 66.3),
    ]

    with Database(Path(":memory:")) as db:
        for record in records:
            db.add(record)

        result = db.get_all()

    assert result == records


def test_get_all_empty():
    with Database(Path(":memory:")) as db:
        result = db.get_all()

    assert result == []


def test_get_all_order():
    records = [
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 5), 66.3),
        WeightRecord(date(2026, 1, 3), 79.3),
    ]

    expected = [
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 3), 79.3),
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 5), 66.3),
    ]

    with Database(Path(":memory:")) as db:
        for record in records:
            db.add(record)

        result = db.get_all()

    assert result == expected


def test_clean():
    records = [
        WeightRecord(date(2026, 1, 4), 77.3),
        WeightRecord(date(2026, 1, 2), 80.2),
        WeightRecord(date(2026, 1, 5), 66.3),
        WeightRecord(date(2026, 1, 3), 79.3),
    ]

    with Database(Path(":memory:")) as db:
        for record in records:
            db.add(record)

        db.clean()
        result = db.get_all()

    assert result == []
