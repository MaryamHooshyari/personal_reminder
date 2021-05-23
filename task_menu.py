# May 2021
# Maryam Hooshyari
# personal reminder / task_menu, show_task_menu, edit_task_menu, choose_from_task_list

import logging
import csv
import hashlib
from datetime import datetime
from user_class import User
from task_class import Task
from main import main_menu
from user_func import save_user
from task_func import create_task, add_task_to_file, save_task, display_task, in_calendar


def show_task_menu(user):
    """
    (user object) --> nothing
    just a menu for show tasks part
    called by task_menu function
    """
    print('1-show undone tasks\n'
          '2-show done tasks\n'
          '3-go to TASK menu')
    try:
        status = int(input('- '))
    except ValueError:
        print('Only integers are allowed!')
        logging.error('invalid input in show task menu: not a number')
    else:
        if status in [1, 2]:
            print('select a period of time:\n'
                  '1-this day\n'
                  '2-this week\n'
                  '3-this month')
            try:
                time_input = int(input('- '))
            except ValueError:
                print('Only integers are allowed!')
                logging.error('invalid input in show task menu: not a number')
            else:
                period = 0
                if time_input == 1:
                    period = 1
                elif time_input == 2:
                    period = 7
                elif time_input == 3:
                    period = 30
                else:
                    print('invalid input: number does not exist in menu')
                    logging.warning('invalid input in show task menu: unavailable number in menu')
                display_list = display_task(user.user_id, str(status-1), period)
                counter = 1
                for i in display_list:
                    print(f'{counter}-{i[2:10]}')
                    counter += 1
                print()  # just to make a new line!
        elif status == 3:
            task_menu(user)
        else:
            print('invalid input: number does not exist in menu')
            logging.warning('invalid input in show task menu: unavailable number in menu')


def choose_from_task_list(user):
    """
    (user object) --> (task object)
    just a menu to show tasks in a list so user can choose one
    called by task_menu function
    """
    print('which task you want to edit or share?')
    with open("task_list.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        lines = []
        i = 1
        for line in reader:
            if line[1] == user.user_id and line[11] == '1' and line[10] == '0':
                """
                line[1]: task owner's id
                line[10]: task status attribute (0 means undone)
                line[11]: task delete attribute (1 means enable)
                user can only edit undone and enable tasks
                """
                print(f'{i}-{line[2:10]}')
                i += 1
                lines.append(line)
    try:
        n = int(input('enter number: ')) - 1
    except ValueError:
        print('Only integers are allowed!')
        logging.error('invalid input in choose task from list menu: not a number')
        choose_from_task_list(user)
    else:
        task = Task(lines[n][0], lines[n][1], lines[n][2], lines[n][3], lines[n][4], lines[n][5], lines[n][6],
                    lines[n][7], lines[n][8], lines[n][9], lines[n][10], lines[n][11])
        return task


def edit_task_menu(task, user):
    """
    (user object) and (task object) --> nothing
    a menu for edit and share tasks part
    called by task_menu function
    """
    print('what change you want to apply?\n'
          '1-postpone\n'
          '2-report if the task is done\n'
          '3-edit title\n'
          '4-edit description\n'
          '5-edit priority\n'
          '6-edit link\n'
          '7-edit location\n'
          '8-share task\n'
          '9-delete task\n'
          '10-go to TASK menu')
    try:
        edit_input = int(input('- '))
    except ValueError:
        print('Only integers are allowed!')
        logging.error('invalid input in edit task menu: not a number')
    else:
        if edit_input == 1:
            new_due_date = input('enter new due date: ')
            task.postpone(new_due_date)
            logging.info('task postponed')
            print(f'{task.title} is postponed to {task.due_date}')
            edit_task_menu(task, user)
        elif edit_input == 2:
            task.done()
            logging.info('task is done')
            print(f'{task.title} is done!')
            edit_task_menu(task, user)
        elif edit_input == 3:
            new_title = input('enter new title: ')
            task.edit_title(new_title)
            logging.info("task's title edited")
            edit_task_menu(task, user)
        elif edit_input == 4:
            new_description = input('enter new description: ')
            task.edit_description(new_description)
            logging.info("task's description edited")
            edit_task_menu(task, user)
        elif edit_input == 5:
            try:
                new_priority = int(input('enter new priority:\n'
                                         '1- important & urgent\n'
                                         '2- not important but urgent\n'
                                         '3- important but not urgent\n'
                                         '4- not important & not urgent\n'
                                         '- '))
            except ValueError:
                print('Only integers are allowed!')
                logging.error('invalid input in priority input: not a number')
            else:
                if new_priority in [1, 2, 3, 4]:
                    task.edit_priority(new_priority)
                else:
                    print('invalid input: you should give a number between 1 to 4')
                    logging.warning('invalid input in priority input: unavailable number in menu')
                logging.info("task's priority edited")
                edit_task_menu(task, user)
        elif edit_input == 6:
            new_link = input('enter new link: ')
            task.edit_link(task, new_link)
            logging.info("task's link edited")
            edit_task_menu(task, user)
        elif edit_input == 7:
            new_location = input('enter new location: ')
            task.edit_location(new_location)
            logging.info("task's location edited")
            edit_task_menu(task, user)
        elif edit_input == 8:
            print('who do you want to share your task with?')
            share_user_list = []
            with open('account.csv', 'r') as ac:
                reader = csv.reader(ac, delimiter=',')
                i = 1
                for line in reader:
                    if line[1] != user.username:
                        print(f'{i}-{line[1]}')  # to make a list of usernames as menu to choose
                        share_user_list.append(line[1])
                        i += 1
            receiver_input = int(input("- ")) - 1
            receiver = share_user_list[receiver_input]
            with open('share_task.csv') as st:
                shared_task_id = sum(1 for line in st)  # to count how many share task exist plus one!
            shared = Task.share(task, user.username, receiver, shared_task_id)
            with open("share_task.csv", 'a', newline='') as share:
                writer = csv.writer(share, delimiter=',')
                writer.writerows(shared)
            logging.info('new share task added')
            edit_task_menu(task, user)
        elif edit_input == 9:
            task = Task.delete(task)
            save_task(task)
            logging.info('task deleted')
            task_menu(user)
        elif edit_input == 10:
            save_task(task)
            logging.info('exit edit task menu')
            task_menu(user)
        else:
            print('invalid input: number does not exist in menu')
            logging.warning('invalid input in edit task menu: unavailable number in menu')


def task_menu(user):
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
            if line[2] == user.username:
                print('8-check shared task')
                share_exist = True
                break
    try:
        task_input = int(input('- '))
    except ValueError:
        print('Only Integers are allowed!')
        logging.error('invalid input in task menu: not a number')
    else:
        if task_input == 1:
            new_task = create_task(user.user_id)
            add_task_to_file(new_task)
            logging.info('new task added')
            print('new task added')
            task_menu(user)
        elif task_input == 2:
            task = choose_from_task_list(user)
            edit_task_menu(task, user)
        elif task_input == 3:
            in_calendar(user.user_id)
            task_menu(user)
        elif task_input == 4:
            show_task_menu(user)
        elif task_input == 5:
            current_password = input('enter your current password: ')
            hashed_pwd = hashlib.sha256(current_password.encode('utf8')).hexdigest()
            if hashed_pwd == user.password:
                new_password = input('enter new password: ')
                second_new_password = input('confirm new password: ')
                if new_password == second_new_password:
                    user = User.change_password(user, new_password)
                    save_user(user)
                    logging.info('password changed')
            task_menu(user)
        elif task_input == 6:
            print(f'{user.username} logged out successfully.')
            logging.info('user logged out')
            main_menu()
        elif task_input == 7:
            user = User.delete_account(user)
            print(f'{user.username} account deleted successfully.')
            logging.info('user deleted account')
            main_menu()
        elif task_input == 8:
            if share_exist:
                with open('share_task.csv', 'r') as st:
                    reader = csv.reader(st, delimiter=',')
                    share_task_list = []
                    for line in reader:
                        if line[2] == user.username:
                            share_task_list.append(line)
                print('which task you want to check?')
                for i in range(len(share_task_list)):
                    print(f'{i + 1}-{share_task_list[i][1]} --> {share_task_list[i][3:6]}')
                try:
                    share_input = int(input('- '))
                except ValueError:
                    print('Only integers are allowed!')
                    logging.error('invalid input in task menu/share: not a number')
                else:
                    task = share_task_list[share_input - 1]
                    accept_deny = input('do you want to accept this task?(yes/no) ').lower()
                    if accept_deny == 'yes':
                        set_date = datetime.now()
                        with open('task_list.csv') as tl:
                            task_id = sum(1 for line in tl)
                        share_task = Task(task_id, int(user.user_id), task[3], task[4], task[5],
                                          set_date, task[6], task[7], task[8], task[9])
                        add_task_to_file(share_task)
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
                    else:
                        print('Invalid Input! --> you should enter "yes" or "no"')
                        logging.warning('wrong input for accept or deny share task')
            else:
                print('Invalid input: number does not exist in menu!')
                logging.warning('invalid input: enter 8 in task menu when there was no shared task')
            task_menu(user)
