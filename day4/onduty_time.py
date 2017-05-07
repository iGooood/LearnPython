# onduty_time.py
# !user/bin/env python

import time, datetime

duty_data = []
f = open('dutytime.txt', 'r')
data = f.read()
rows = data.split('\n')
for row in rows:
    split_row = row.split('\t')
    duty_data.append(split_row)
print(duty_data)000
0T1 = []
T2 = []
for row in duty_data[1:]:
    T1.append(row[4])  # 读取上班打卡时间T1
    T2.append(row[5])  # 读取下班打卡时间T2
day_count = len(T1)
print(day_count)
RT1 = []
RT2 = []
Delta_T = []

for i in range(day_count):
    RT1.append(datetime.datetime.strptime(T1[i], '%H:%M'))  # 将字符串格式的时间转换成时间格式
    RT2.append(datetime.datetime.strptime(T2[i], '%H:%M'))
    Delta_T.append(RT2[i] - RT1[i])
    if T1[i] == T2[i]:  # 上班打卡时间与下班打卡时间相同
        print('第 %s 个工作日' % (day_count - i) + '忘打卡了')

# ST0 = datetime.datetime.strptime('18:30', '%H:%M')
# ST1 = datetime.datetime.strptime('1:30', '%H:%M')
# ST2 = datetime.datetime.strptime('2:00', '%H:%M')
# if T1[i] >= T0:

# print(t2-t1)
print(RT1)
print(RT2)
print(Delta_T)

f.close()

