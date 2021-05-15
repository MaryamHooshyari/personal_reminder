# 2021.04.24
# Maryam Hooshyari
# personal reminder / main

from user import User
from task import Task
from modules import save_task, add_task, in_calendar
from datetime import datetime
import hashlib
import csv
import os.path

if not os.path.isfile('account.csv'):
    with open('account.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'username', 'password', 'E-mail', 'status'])
if not os.path.isfile('task_list.csv'):
    with open('task_list.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['task_id', 'user_id', 'title', 'description', 'due_date', 'set_date', 'priority', 'projects',
                         'link', 'location', 'status', 'delete_'])
if not os.path.isfile('share_task.csv'):
    with open('share_task.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(['shared_task_id', 'sender_name', 'receiver_name', 'title', 'description', 'due_date',
                         'priority', 'projects', 'link', 'location', 'accept/deny', 'check'])

print('Welcome to personal reminder')
sign_input = 0
while sign_input != 3:
    try:
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
                print('logged in successfully!')
                task_input = 0
                while task_input not in [6, 7]:
                    print('TASK menu\n'
                          '1-add new task\n'
                          '2-share or edit existing task\n'
                          '3-show all undone tasks in calendar\n'
                          '4-show tasks\n'
                          '5-change password\n'
                          '6-log out\n'
                          '7-delete account')
                    share_exist = False
                    with open('share_task.csv', 'r') as st:
                        reader = csv.reader(st, delimiter=',')
                        for line in reader:
                            if line[2] == present_user.username:
                                print('8-check shared task')
                                share_exist = True
                                break
                    task_input = int(input('- '))
                    try:
                        if task_input == 1:
                            present_task = add_task(present_user.user_id)
                            save_task(present_task)
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
                            try:
                                present_task = Task(lines[n][0], lines[n][1], lines[n][2], lines[n][3], lines[n][4],
                                                    lines[n][5], lines[n][6], lines[n][7], lines[n][8], lines[n][9],
                                                    lines[n][10], lines[n][11])
                                edit_input = 0
                                while edit_input not in [9, 10]:
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
                                    try:
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
                                            share_user_list = []
                                            with open('account.csv', 'r') as ac:
                                                reader = csv.reader(ac, delimiter=',')
                                                i = 1
                                                for line in reader:
                                                    if line[1] != present_user.username:
                                                        print(
                                                            f'{i}-{line[1]}')  # to make a list of usernames as menu to choose
                                                        share_user_list.append(line[1])
                                                        i += 1
                                            receiver_input = int(input("- ")) - 1
                                            receiver = share_user_list[receiver_input]
                                            with open('share_task.csv') as st:
                                                shared_task_id = sum(
                                                    1 for line in st)  # to count how many share task exist plus one!
                                            shared = Task.share(present_task, present_user.username, receiver, shared_task_id)
                                            with open("share_task.csv", 'a', newline='') as share:
                                                writer = csv.writer(share, delimiter=',')
                                                writer.writerows(shared)
                                        elif edit_input == 9:
                                            present_task = Task.delete(present_task)
                                            with open("task_list.csv", 'r') as f:
                                                reader = csv.reader(f, delimiter=',')
                                                save_lines = []
                                                for line in reader:
                                                    if line[0] == present_task.task_id:
                                                        line = [present_task.task_id, present_task.user_id, present_task.title,
                                                                present_task.description, present_task.due_date,
                                                                present_task.set_date, present_task.priority,
                                                                present_task.projects,
                                                                present_task.link, present_task.location, present_task.status,
                                                                present_task.delete_]
                                                    save_lines.append(line)
                                            with open("task_list.csv", 'w', newline='') as f:
                                                writer = csv.writer(f, delimiter=',')
                                                writer.writerows(save_lines)
                                        elif edit_input == 10:
                                            with open("task_list.csv", 'r') as f:
                                                reader = csv.reader(f, delimiter=',')
                                                save_lines = []
                                                for line in reader:
                                                    if line[0] == present_task.task_id:
                                                        line = [present_task.task_id, present_task.user_id, present_task.title,
                                                                present_task.description, present_task.due_date,
                                                                present_task.set_date,
                                                                present_task.priority, present_task.projects, present_task.link,
                                                                present_task.location, present_task.status,
                                                                present_task.delete_]
                                                    save_lines.append(line)
                                            with open("task_list.csv", 'w', newline='') as f:
                                                writer = csv.writer(f, delimiter=',')
                                                writer.writerows(save_lines)
                                    except ValueError:
                                        print('Only Integers are allowed!')
                                    except edit_input not in range(1, 11):
                                        print('Number does not exist in menu!')
                            except ValueError:
                                print('Only Integers are allowed!')
                            except:
                                print('Number does not exist in menu!')
                        elif task_input == 3:
                            in_calendar(present_user.user_id)
                        elif task_input == 4:
                            while True:
                                print('1-show undone tasks\n'
                                      '2-show done tasks\n'
                                      '3-go to TASK menu')
                                status = str(int(input('- ')) - 1)
                                if status in ['0', '1']:
                                    print('select a period of time:\n'
                                          '1-this day\n'
                                          '2-this week\n'
                                          '3-this month')
                                    time_input = int(input('- '))
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
                                    print()  # just to make a new line!
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
                            print(f'{present_user.username} logged out successfully.')
                        elif task_input == 7:
                            present_user = User.delete_account(present_user)
                            print(f'{present_user.username} account deleted successfully.')
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
                        elif task_input == 8:
                            with open('share_task.csv', 'r') as st:
                                reader = csv.reader(st, delimiter=',')
                                share_task_list = []
                                for line in reader:
                                    if line[2] == present_user.username:
                                        share_task_list.append(line)
                            print('which task you want to check?')
                            for i in range(len(share_task_list)):
                                print(f'{i + 1}-{share_task_list[i][1]} --> {share_task_list[i][3:6]}')
                            share_input = int(input('- '))
                            try:
                                task = share_task_list[share_input - 1]
                                accept_deny = input('do you want to accept this task?(yes/no) ').lower()
                                try:
                                    if accept_deny == 'yes':
                                        set_date = datetime.now()
                                        with open('task_list.csv') as tl:
                                            task_id = sum(1 for line in tl)
                                        share_task = Task(task_id, int(present_user.user_id), task[3], task[4],
                                                          task[5],
                                                          set_date,
                                                          task[6], task[7], task[8], task[9])
                                        save_task(share_task)
                                        # change check from 0 to 1 and accept/deny from 0 to 1 which means accepted
                                        with open('share_task.csv', 'r') as st:
                                            reader = csv.reader(st, delimiter=',')
                                            lines = []
                                            for line in reader:
                                                if line[0] == task[0]:
                                                    line[10] = 1
                                                    line[11] = 1
                                                lines.append(line)
                                        with open("share_task.csv", 'w', newline='') as st:
                                            writer = csv.writer(st, delimiter=',')
                                            writer.writerows(lines)
                                    elif accept_deny == 'no':
                                        # just change check from 0 to 1
                                        with open('share_task.csv', 'r') as st:
                                            reader = csv.reader(st, delimiter=',')
                                            lines = []
                                            for line in reader:
                                                if line[0] == task[0]:
                                                    line[11] = 1
                                                lines.append(line)
                                        with open("share_task.csv", 'w', newline='') as st:
                                            writer = csv.writer(st, delimiter=',')
                                            writer.writerows(lines)
                                except:
                                    print('Invalid Input! --> you should enter "yes" or "no" ')
                            except ValueError:
                                print('Only integers are allowed!')
                            except:
                                print('please enter a number which exist in menu!')
                    except ValueError:
                        print('Only Integers are allowed!')
                    except task_input not in range(1, 9):
                        print('Number does not exist in menu!')
            else:
                print('Wrong password!')
                break
        elif sign_input == 2:
            with open('account.csv') as ac:
                user_ID = sum(1 for line in ac)
            user_ID = User.create_account(user_ID)
    except ValueError:
        print('Only integers are allowed!')
    except sign_input not in range(1, 4):
        print('you should enter a number between 1 to 3!')
