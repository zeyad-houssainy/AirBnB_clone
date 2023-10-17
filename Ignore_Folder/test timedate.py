from datetime import timedelta, datetime
now = datetime.now()
then = now - timedelta(days=10)

print(now)
print(then)

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)

print(delta)
print(f"Total seconds: {delta.total_seconds()}")
# print(f"Total minutes: {delta.total_}")
