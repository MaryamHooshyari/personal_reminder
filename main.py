# 2021.04.24
# Maryam Hooshyari
# personal reminder / main

from user import User
from task import Task
import pandas as pd
import hashlib
import csv
from datetime import datetime, date


def is_leap(yr):
    """
    (int) -> bool
    Checks if year is a leap year
    CALLED BY: calendar()
    """
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print('Welcome to personal reminder')

while True:
    print('which one do you want to do?\n'
          '1-sign in\n'
          '2-sign up\n'
          '3-close program')
    sign_input = int(input('- '))
    if sign_input == 1:
        log_output = False
        user_line = []
        username = input('enter username: ')
        with open("account.csv", 'r') as f:
            reader = csv.reader(f, delimiter=',')
            for line in reader:
                if line[1] == username:
                    user_line.append(line)
                    break
        if len(user_line) == 1:
            present_user = User(user_line[0][0], user_line[0][1], user_line[0][2], user_line[0][3], user_line[0][4])
            log_output = User.log_in(present_user)
        else:
            print('username does not exist!')
            break
        if log_output:
            # write show share code here
            while True:
                print('TASK menu\n'
                      '1-add new task\n'
                      '2-share or edit existing task\n'
                      '3-show all undone tasks in calendar\n'
                      '4-show tasks\n'
                      '5-change password\n'
                      '6-log out\n'
                      '7-delete account')
                task_input = int(input('- '))
                if task_input == 1:
                    with open('task_list.csv') as tl:
                        task_ID = sum(1 for line in tl)
                    present_task = Task.add_task(task_ID, present_user.user_id)
                    print('new task added')
                elif task_input == 2:
                    print('which task you want to edit or share?')
                    with open("task_list.csv", 'r') as f:
                        reader = csv.reader(f, delimiter=',')
                        lines = []
                        i = 1
                        for line in reader:
                            if line[1] == present_user.user_id and line[11] == '1' and line[10] == '0':
                                """
                                line[1]: task owner's id
                                line[10]: task status attribute (0 means undone)
                                line[11]: task delete attribute (1 means enable)
                                user can only edit undone and enable tasks
                                """
                                print(f'{i}-{line[2:10]}')
                                i += 1
                                lines.append(line)
                    n = int(input('enter number: ')) - 1
                    present_task = Task(lines[n][0], lines[n][1], lines[n][2], lines[n][3], lines[n][4], lines[n][5],
                                        lines[n][6], lines[n][7], lines[n][8], lines[n][9], lines[n][10], lines[n][11])
                    while True:
                        print('what change you want to apply?\n'
                              '1-postpone the task\n'
                              '2-report if the task is done\n'
                              '3-edit title\n'
                              '4-edit description\n'
                              '5-edit priority\n'
                              '6-edit link\n'
                              '7-edit location\n'
                              '8-share task\n'
                              '9-delete the task\n'
                              '10-go to TASK menu')
                        edit_input = int(input())
                        if edit_input == 1:
                            new_due_date = input('enter new due date: ')
                            present_task.postpone(new_due_date)
                            print(f'{present_task.title} is postponed to {present_task.due_date}')
                        elif edit_input == 2:
                            present_task.done()
                            print(f'{present_task.title} is done!')
                        elif edit_input == 3:
                            new_title = input('enter new title: ')
                            present_task = Task.edit_title(present_task, new_title)
                        elif edit_input == 4:
                            new_description = input('enter new description: ')
                            present_task = Task.edit_description(present_task, new_description)
                        elif edit_input == 5:
                            new_priority = int(input('enter new priority: '))
                            if new_priority in [1, 2, 3, 4]:
                                present_task = Task.edit_priority(present_task, new_priority)
                            else:
                                print('invalid input!\n'
                                      'you should give a number between 1 to 4')
                        elif edit_input == 6:
                            new_link = input('enter new link: ')
                            present_task = Task.edit_link(present_task, new_link)
                        elif edit_input == 7:
                            new_location = input('enter new location: ')
                            present_task = Task.edit_location(present_task, new_location)
                        elif edit_input == 8:
                            print('who do you want to share your task with?')
                            receiver = input("please enter receiver's username: ")
                            column_names = ["user_id", "username", "password", "E-mail", "status"]
                            df = pd.read_csv("account.csv", names=column_names)
                            user_list = list(df.username)
                            if receiver in user_list:
                                with open('share_task.csv') as st:
                                    shared_task_id = sum(1 for line in st)
                                shared = Task.share(present_task, present_user, receiver, shared_task_id)
                                with open("share_task.csv", 'w', newline='') as share:
                                    writer = csv.writer(share, delimiter=',')
                                    writer.writerow(shared)
                            else:
                                print('username does not exist!')
                        elif edit_input == 9:
                            present_task = Task.delete(present_task)
                            with open("task_list.csv", 'r') as f:
                                reader = csv.reader(f, delimiter=',')
                                save_lines = []
                                for line in reader:
                                    if line[0] == present_task.task_id:
                                        line[:] = present_task[:]
                                    save_lines.append(line)
                            with open("task_list.csv", 'w', newline='') as f:
                                writer = csv.writer(f, delimiter=',')
                                writer.writerows(save_lines)
                            break
                        elif edit_input == 10:
                            with open("task_list.csv", 'r') as f:
                                reader = csv.reader(f, delimiter=',')
                                save_lines = []
                                for line in reader:
                                    if line[0] == present_task.task_id:
                                        line = [present_task.task_id, present_task.user_id, present_task.title,
                                                present_task.description, present_task.due_date, present_task.set_date,
                                                present_task.priority, present_task.projects, present_task.link,
                                                present_task.location, present_task.status, present_task.delete_]
                                    save_lines.append(line)
                            with open("task_list.csv", 'w', newline='') as f:
                                writer = csv.writer(f, delimiter=',')
                                writer.writerows(save_lines)
                            break
                        else:
                            print('invalid input!')
                elif task_input == 3:
                    calendar_task = []
                    with open("task_list.csv", 'r') as f:
                        reader = csv.reader(f, delimiter=',')
                        i = 1
                        for line in reader:
                            if line[1] == present_user.user_id and line[11] == 1 and line[10] == 0:
                                """
                                line[1]: task owner's id
                                line[10]: task status attribute (0 means undone)
                                line[11]: task delete attribute (1 means enable)
                                only undone and enable tasks matters to show
                                """
                                limited_task = [line[2:5]]
                                """
                                calendar_task is a list of undone and enable tasks which are for our present user
                                each task will save in to this list with its title, description and due date
                                """
                                calendar_task.append(limited_task)
                    due_date_list = []
                    for task in calendar_task:
                        due_date_list.append(int(task[3][8:10]))
                    due_date_list = sorted(set(due_date_list))
                    # minus 1 is for list index I use later in code
                    month_now = datetime.now().month - 1
                    year_now = datetime.now().year
                    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
                             'October', 'November', 'December']
                    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                    print('which month you want to check?')
                    menu_res = []
                    for i in range(6):
                        """
                        make a menu for user to choose which month wants to show
                        it includes 6 months from now!
                        """
                        if month_now == 12:
                            print(f'{i + 1}-{month[month_now + i]} {year_now}')
                            menu_res.append((month_now, year_now))
                            month_now = 1
                            year_now += 1
                        else:
                            print(f'{i + 1}-{month[month_now + i]} {year_now}')
                            menu_res.append((month_now, year_now))
                    calendar_input = int(input('- '))
                    month_name, year = menu_res[calendar_input-1]
                    if is_leap(year):  # check if the year is leap
                        days_in_month[1] = 29
                    month_day = days_in_month[month.index(month_name)]
                    day_one = date(year, month.index(month_name), 1)
                    start_day = day_one.isoweekday()
                    Task.in_calendar(year, month_name, month_day, start_day, due_date_list, calendar_task)
                elif task_input == 4:
                    while True:
                        print('1-show undone tasks\n'
                              '2-show done tasks\n'
                              '3-go to TASK menu')
                        status = str(int(input()) - 1)
                        if status in ['0', '1']:
                            print('select a period of time:\n'
                                  '1-this day\n'
                                  '2-this week\n'
                                  '3-this month')
                            time_input = int(input())
                            period = 0
                            if time_input == 1:
                                period = 1
                            elif time_input == 2:
                                period = 7
                            elif time_input == 3:
                                period = 30
                            else:
                                print('invalid input!')
                            display_list = Task.display_task(present_user.user_id, status, period)
                            counter = 1
                            for i in display_list:
                                print(f'{counter}-{i[2:10]}')
                                counter += 1
                            print() # just to make a new line!
                        elif status == 3:
                            break
                        else:
                            print('invalid input!')
                elif task_input == 5:
                    current_password = input('enter your current password: ')
                    hashed_pwd = hashlib.sha256(current_password.encode('utf8')).hexdigest()
                    if hashed_pwd == present_user.password:
                        new_password = input('enter new password: ')
                        second_new_password = input('confirm new password: ')
                        if new_password == second_new_password:
                            present_user = User.change_password(present_user, new_password)
                elif task_input == 6:
                    print(f'{present_user.username} logged out successfully.')
                    with open("account.csv", 'r') as f:
                        reader = csv.reader(f, delimiter=',')
                        save_lines = []
                        for line in reader:
                            if line[0] == present_user[0]:
                                line[:] = present_user[:]
                            save_lines.append(line)
                    with open("account.csv", 'w', newline='') as f:
                        writer = csv.writer(f, delimiter=',')
                        writer.writerows(save_lines)
                    break
                elif task_input == 7:
                    present_user = User.delete_account(present_user)
                    with open("account.csv", 'r') as f:
                        reader = csv.reader(f, delimiter=',')
                        save_lines = []
                        for line in reader:
                            if line[0] == present_user[0]:
                                line[:] = present_user[:]
                            save_lines.append(line)
                    with open("account.csv", 'w', newline='') as f:
                        writer = csv.writer(f, delimiter=',')
                        writer.writerows(save_lines)
                    break
                else:
                    print('invalid input!')
        else:
            print('Wrong password!')
            break
    elif sign_input == 2:
        with open('account.csv') as ac:
            user_ID = sum(1 for line in ac)
        user_ID = User.create_account(user_ID)
    elif sign_input == 3:
        break
    else:
        print('invalid input!')
