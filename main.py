# 2021.04.24
# Maryam Hooshyari
# personal reminder / main

from user import User
from task import Task
import pandas as pd

print('Welcome to personal reminder')
column_names = ["user_ID", "username", "password", "E-mail", "status"]
df = pd.read_csv("account.csv", names=column_names)
user_ID = len(df.user_ID) - 1
while True:
    print('which one do you want to do?\n'
          '1-sign in\n'
          '2-sign up\n'
          '3-close program')
    sign_input = int(input())
    if sign_input == 1:
        present_user = User.log_in()
        column_names = ['task_ID', 'user_ID', 'description', 'due_date', 'set_date', 'priority',
                        'projects', 'link', 'location', 'status', 'delete_']
        df = pd.read_csv(str(user_ID)+'_task.csv', names=column_names)
        task_ID = len(df.task_ID) - 1
        while True:
            print('TASK menu\n'
                  '1-add new task\n'
                  '2-change existing task\n'
                  '3-show all undone tasks in calendar\n'
                  '4-show tasks\n'
                  '5-share a task\n'
                  '6-change password\n'
                  '7-log out\n'
                  '8-delete account')
            task_input = int(input())
            if task_input == 1:
                task_ID = Task.add_task(task_ID, present_user)
            elif task_input == 2:
                task_description = input('enter description of the task you want to change: ')
                while True:
                    print('what change you want to apply?\n'
                          '1-postpone the task\n'
                          '2-report if the task is done\n'
                          '3-edit description\n'
                          '4-edit priority\n'
                          '5-edit link\n'
                          '6-edit location\n'
                          '7-delete the task')
            elif task_input == 3:
                Task.in_calendar()
            elif task_input == 4:
                while True:
                    print('1-show done tasks\n'
                          '2-show undone tasks\n'
                          '3-go to task menu')
                    show_input = input()
                    if show_input == 1:
                        while True:
                            print()
            elif task_input == 5:
                Task.share()
            elif task_input == 6:
                User.change_password(present_user)
            elif task_input == 7:
                User.log_out(present_user)
                break
            elif task_input == 8:
                User.delete_account(present_user)
                break
            else:
                print('invalid input!')
    elif sign_input == 2:
        user_ID = User.create_account(user_ID)
    elif sign_input == 3:
        break
    else:
        print('invalid input!')
