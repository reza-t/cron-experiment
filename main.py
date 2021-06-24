from crontab import CronTab
from datetime import datetime

cron = CronTab(tab="t")


def task():
    f = open("MyFile.txt", "a")
    time = datetime.now()
    f.write(str(time))
    f.close()


job = cron.new(command=task())
job.setall(1, None, None, None, None)
cron.write()
