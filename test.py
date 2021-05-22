import csv

#######################

# with open('task_list.csv', 'w', newline='') as task_file:
#     csv_writer = csv.writer(task_file)
#     csv_writer.writerow(['task_id', 'user_id', 'title', 'description', 'due_date', 'set_date',
#                          'priority', 'projects', 'link', 'location', 'status', 'delete_'])
#
# with open('share_task.csv', 'w', newline='') as task_file:
#     csv_writer = csv.writer(task_file)
#     csv_writer.writerow(['shared_task_id', 'sender_name', 'receiver_name', 'title', 'description', 'due_date',
#                          'priority', 'projects', 'link', 'location', 'accept/deny', 'check'])
#################################
# lines = []
# with open("items.csv", 'r') as f:
#     reader = csv.reader(f, delimiter=',')
#
#     for line in reader:
#         if line[0] == 'cat':
#             line[0] = 'jade'
#         lines.append(line)
# print(lines)
# with open("items.csv", 'w', newline='') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerows(lines)
###############
from datetime import datetime, date
#
# now = datetime.now()
# print(now)
# due_date1 = datetime(2021, 5, 15, 12, 1)
# print(due_date1)
# due_date1 = str(due_date1)
# due_date = datetime(int(due_date1[0:4]), int(due_date1[5:7]), int(due_date1[8:10]))
# time_ = (due_date.date() - now.date()).days
# print(due_date)
# print(time_)
# if time_ == 0:
#     print('true')
###################


# class Book:
#     def __init__(self, name, number, page):
#         self.name = name
#         self.number = number
#         self.page = page
#
#
# obj = Book('pig', 12, 3)
# with open("items.csv", 'w', newline='') as f:
#     writer = csv.writer(f, delimiter=',')
#     writer.writerow([obj.name, obj.number, obj.page])
# ##################
from termcolor import colored

#
# print(colored('hello', 'red'), colored('world', 'green'))

#####################################
# def calendar(year, month_name, month_day, s, due_date_list):
#     # this will convert string value to a corresponding integer
#     # if s == "Su":
#     #     d = 0
#     # elif s == "Mo":
#     #     d = 1
#     # elif s == "Tu":
#     #     d = 2
#     # elif s == "We":
#     #     d = 3
#     # elif s == "Th":
#     #     d = 4
#     # elif s == "Fr":
#     #     d = 5
#     # elif s == "Sa":
#     #     d = 6
#     print(f'{month_name} {year}')
#     print("Sun Mon Tue Wed Thu Fri Sat")
#     i = 1 - s
#     while i <= month_day:
#         if 0 < i < 10:
#             if i in due_date_list:
#                 print("", colored(i, 'red'), end="  ")
#             else:
#                 print("", i, end="  ")
#         elif i <= 0:
#             print("  ", end="  ")
#         else:
#             if i in due_date_list:
#                 print(colored(i, 'red'), end="  ")
#             else:
#                 print(i, end="  ")
#         if (i + s) % 7 == 0:
#             print(" ")
#         i += 1
#
#
# day_one = date(2021, 6, 1)
# start_day = day_one.isoweekday()
# print(start_day)
# calendar(2021, 'January', 30, 3, [4, 8, 10])
#####################################

from plyer import notification

# notification.notify(title="HI MATTEO!", message="Here's the notification to be sent every hour!", timeout=10)
################################
import schedule
import time


class Job:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def change_duration(self, new_du):
        self.duration = new_du
        return self


# def job():
#     print("I'm working...")
#
#
# schedule.every(10).seconds.do(job)
# schedule.every(10).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).minutes.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)
#
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# student = Job('school', 8)
# student.change_duration(5)
# print(student.duration)
#############################
import os.path

if os.path.isfile('account.csv'):
    print("File exist")
else:
    print("File not exist")
