from croniter import croniter
from datetime import datetime
import time

base = datetime.now().replace(microsecond=0)
iterator = croniter('*/1 * * * *', base)
next_time = iterator.get_next(datetime)

print(base)
print(next_time)

while True:
    now = datetime.now().replace(microsecond=0)

    if now >= next_time:
        print("NOW==========================================")
        iterator1 = croniter('*/1 * * * *', now)
        next_time = iterator1.get_next(datetime)
        print(now)
        print(next_time)
    time.sleep(1)
