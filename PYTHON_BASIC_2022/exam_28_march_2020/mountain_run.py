from math import floor

record = float(input())
distance = float(input())
seconds_per_meter = float(input())

climbing_seconds = distance * seconds_per_meter
delaying = floor(distance / 50) * 30
total_time = climbing_seconds + delaying
if total_time < record:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    diff = abs(record - total_time)
    print(f"No! He was {diff:.2f} seconds slower.")