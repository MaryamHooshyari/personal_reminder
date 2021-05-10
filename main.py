# 2021.04.24
# Maryam Hooshyari
# personal reminder / main

from user import User
from task import Task
import pandas as pd
import hashlib
import csv

print('Welcome to personal reminder')

with open('task_list.csv', 'w', newline='') as task_file:
    csv_writer = csv.writer(task_file)
    csv_writer.writerow(['task_id', 'user_id', 'title', 'description', 'due_date', 'set_date',
                         'priority', 'projects', 'link', 'location', 'status', 'delete_'])

with open('share_task.csv', 'w', newline='') as task_file:
    csv_writer = csv.writer(task_file)
    csv_writer.writerow(['shared_task_id', 'sender_name', 'receiver_name', 'title', 'description', 'due_date',
                         'priority', 'projects', 'link', 'location', 'accept/deny', 'check'])

while True:
    print('which one do you want to do?\n'
          '1-sign in\n'
          '2-sign up\n'
          '3-close program')
    sign_input = int(input())
    if sign_input == 1:
        present_user = User.log_in()
        while True:
            print('TASK menu\n'
                  '1-add new task\n'
                  '2-share or edit existing task\n'
                  '3-show all undone tasks in calendar\n'
                  '4-show tasks\n'
                  '5-change password\n'
                  '6-log out\n'
                  '7-delete account')
            task_input = int(input())
            if task_input == 1:
                with open('task_list.csv') as tl:
                    task_ID = sum(1 for line in tl)
                task_ID = Task.add_task(task_ID, present_user.user_id)
                print('new task added')
            elif task_input == 2:
                print('which task you want to edit or share?')
                with open("task_list.csv", 'r') as f:
                    reader = csv.reader(f, delimiter=',')
                    lines = []
                    i = 1
                    for line in reader:
                        if line[1] == present_user.user_id and line[11] == 1 and line[10] == 0:
                            """
                            line[1]: task owner's id
                            line[10]: task status attribute (0 means undone)
                            line[11]: task delete attribute (1 means enable)
                            user can only edit undone and enable tasks
                            """
                            print(f'{i}-{line[2:10]}')
                            i += 1
                            lines.append(line)
                n = int(input('enter number: '))
                present_task = Task(lines[n - 1][0], lines[n - 1][1], lines[n - 1][2], lines[n - 1][3], lines[n - 1][4],
                                    lines[n - 1][5], lines[n - 1][6], lines[n - 1][7], lines[n - 1][8], lines[n - 1][9],
                                    lines[n - 1][10], lines[n - 1][11])
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
                        present_task = Task.postpone(present_task, new_due_date)
                        print(f'{present_task.title} is postponed to {present_task.due_date}')
                    elif edit_input == 2:
                        present_task = Task.done(present_task)
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
                            shared = Task.share(present_task, present_user, receiver)
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
                                if line[0] == present_task[0]:
                                    line[:] = present_task[:]
                                save_lines.append(line)
                        with open("task_list.csv", 'w', newline='') as f:
                            writer = csv.writer(f, delimiter=',')
                            writer.writerows(save_lines)
                        break
                    else:
                        print('invalid input!')
            elif task_input == 3:
                Task.in_calendar(present_user)
            elif task_input == 4:
                while True:
                    print('1-show undone tasks\n'
                          '2-show done tasks\n'
                          '3-go to TASK menu')
                    status = int(input()) - 1
                    if status in [0, 1]:
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
                        display_list = Task.display_task(present_user.user_id, status, period)
                        counter = 1
                        for i in display_list:
                            print(f'{counter}-{i[2:10]}')
                            counter += 1
                        else:
                            print('invalid input!')
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
    elif sign_input == 2:
        with open('account.csv') as ac:
            user_ID = sum(1 for line in ac)
        user_ID = User.create_account(user_ID)
    elif sign_input == 3:
        break
    else:
        print('invalid input!')
