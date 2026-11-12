import shutil
import plotext as plt
from datetime import datetime
from statistics import median

from ..infrastructure.database import WeightRecord

def render(records: list[WeightRecord], days = 30):
    dates = [ datetime.combine(record.date, datetime.min.time()) for record in records ]
    weights = [ record.weight for record in records ]

    fig = plt.figure
    fig.clear()

    width = shutil.get_terminal_size().columns * 0.8
    height = shutil.get_terminal_size().lines * 0.4

    fig.plot_size(width, height)
    fig.date("x").activate(form="%Y-%m-%d")

    signal1 = fig.signal(dates, weights, marker=plt.marker("braille", pixel="white")).lines()
    signal2 = fig.signal(dates, weights, marker=plt.marker("x", pixel="cyon"))

    fig.draw(signal1)
    fig.draw(signal2)

    fig.theme("simple")
    fig.title("Recent Weight Record")
    fig.show()

    count = len(weights)
    maximum = max(weights, default=-1)
    minimum = min(weights, default=-1)
    average = sum(weights) / count if count else -1
    med = median(weights) if count else -1
    change = weights[-1] - weights[-2] if count > 1 else 0.0
    print()
    print(f"Overview in the past {days} days ({count} records):")
    print(f"\tMaximum: {maximum:.1f} kg")
    print(f"\tMinimum: {minimum:.1f} kg")
    print(f"\tAverage: {average:.1f} kg")
    print(f"\tMedian:  {med:.1f} kg")
    print()
    print(f"Compared with the previous record, change: {change:.1f} kg")
    print()
