# May 2021
# Maryam Hooshyari
# personal reminder / main

import logging
import csv
import os.path
from user_class import User
from task_menu import task_menu
from user_func import user_id, create_account, add_user_to_file

logging.basicConfig(filename='code_record.log', filemode='a', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')

if not os.path.isfile('account.csv'):
    with open('account.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['user_id', 'username', 'password', 'E-mail', 'status'])
if not os.path.isfile('task_list.csv'):
    with open('task_list.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['task_id', 'user_id', 'title', 'description', 'due_date', 'set_date', 'priority', 'projects',
                         'link', 'location', 'status', 'delete_'])
if not os.path.isfile('share_task.csv'):
    with open('share_task.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['shared_task_id', 'sender_name', 'receiver_name', 'title', 'description', 'due_date',
                         'priority', 'projects', 'link', 'location', 'accept/deny', 'check'])


def main_menu():
    print('which one do you want to do?\n'
          '1-sign in\n'
          '2-sign up\n'
          '3-close program')
    try:
        sign_input = int(input('- '))
    except ValueError:
        print('Only integers are allowed!')
        logging.error('invalid input in main menu: not a number')
        main_menu()
    else:
        if sign_input == 1:
            user_line = []
            username = input('enter username: ')
            with open("account.csv", 'r') as f:
                reader = csv.reader(f, delimiter=',')
                for line in reader:
                    if line[1] == username:
                        user_line.append(line)
                        break
            if len(user_line) == 1:
                user = User(user_line[0][0], user_line[0][1], user_line[0][2], user_line[0][3], user_line[0][4])
                log_output = User.log_in(user)
                if log_output:
                    logging.info('user logged in')
                    print('user logged in successfully!')
                    task_menu(user)
                else:
                    print('Wrong password!')
                    logging.warning('wrong password')
                    main_menu()
            else:
                print('username does not exist!')
                logging.warning('entered username does not exist')
                main_menu()
        elif sign_input == 2:
            id = user_id()
            user = create_account(id)
            add_user_to_file(user)
            logging.info('new user added')
            print('new account created')
            main_menu()
        elif sign_input == 3:
            print('See You Later:)')
            logging.info('user exit')
            exit()
        else:
            print('Invalid input: number does not exist in menu')
            logging.warning('invalid input in main menu: unavailable number in menu')
            main_menu()


if __name__ == '__main__':
    print('Welcome to personal reminder')
    main_menu()
