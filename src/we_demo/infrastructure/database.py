import sqlite3

from datetime import date
from pathlib import Path
from dataclasses import dataclass

@dataclass
class WeightRecord:
    date: date
    weight: float

class Database:

    def __init__(self, path: Path):
        self.conn = sqlite3.connect(path)

    def __enter__(self):
        self.init()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

    def init(self) -> None:
        self.conn.execute(
            '''
            CREATE TABLE IF NOT EXISTS Weight (
                date TEXT PRIMARY KEY,
                weight REAL NOT NULL
            )
            '''
        )
        self.conn.commit()

    def add(self, record: WeightRecord) -> None:
        self.conn.execute(
            '''
            INSERT INTO Weight (date, weight)
            VALUES (?, ?)
            ON CONFLICT(date)
            DO UPDATE SET weight = excluded.weight
            ''',
            (
                record.date.isoformat(),
                record.weight,
            ),
        )
        self.conn.commit()

    def get_range(self, start: date, end: date) -> list[WeightRecord]:
        cursor = self.conn.execute(
            '''
            SELECT date, weight
            FROM Weight
            WHERE date BETWEEN ? AND ?
            ORDER BY date
            ''',
            (
                start.isoformat(),
                end.isoformat(),
            ),
        )

        return [ WeightRecord(date=date.fromisoformat(row[0]), weight=row[1]) for row in cursor]

    def get_all(self) -> list[WeightRecord]:
        cursor = self.conn.execute(
            '''
            SELECT date, weight
            FROM Weight
            ORDER BY date
            ''',
        )

        return [ WeightRecord(date=date.fromisoformat(row[0]), weight=row[1]) for row in cursor]
    def clean(self):
        # Clean all the data in the database
        self.conn.execute(
            '''
            DELETE FROM weight
            ''',
        )

        self.conn.commit()
