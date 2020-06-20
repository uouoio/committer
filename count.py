import datetime
import random
import os


def change_day():
    return datetime.timedelta(days=1)


def change_time():
    return datetime.timedelta(minutes=1)


# 循环的时间
commit_date = datetime.datetime.now()

for i in range(random.randint(1, 2)):
    f = open('data.txt', 'a+')
    commit_date = commit_date + change_time()
    f.writelines(commit_date.isoformat() + '\n')
    f.close()
    os.system('git add .')
    os.system('git commit --date={time} -m "Update {time}"'.format(time=commit_date.isoformat()))
os.system('git push')
