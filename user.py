# 2021.04.24
# Maryam Hooshyari
# personal reminder / user class

import pandas as pd
import hashlib
import csv


class User:
    user_ID = 0

    def __init__(self, user_ID, username, password, email, status='enable'):
        """

        :param user_ID: user's ID (primary key)
        :param username: user's name
        :param password: user's password
        :param email: user's email
        :param status: shows if the account is enable or not
        """
        self.user_ID = user_ID
        self.username = username
        self.password = password
        self.email = email
        self.status = status

    @staticmethod
    def create_account(user_ID):
        """
        create aan account for new user and a csv file for this user's tasks
        :return: user_ID that shows how many user account made!
        """
        column_names = ["user_ID", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        user_list = list(df.username)
        username = input('enter username: ')
        if username not in user_list:
            password = input('enter password: ')
            password_ = input('confirm password: ')
            if password == password_:
                hashed_pwd = hashlib.sha256(password.encode('utf8')).hexdigest()
                email = input('enter your E-mail: ')
                user_ID += 1
                object_user = User(user_ID, username, hashed_pwd, email)
                row_account = [[object_user.user_ID, object_user.username, object_user.password, object_user.email,
                                object_user.status]]
                with open('account.csv', 'a', newline='') as csv_account:
                    csv_writer = csv.writer(csv_account)
                    csv_writer.writerows(row_account)
                with open(str(user_ID)+'_task.csv', 'w', newline='') as task_file:
                    csv_writer = csv.writer(task_file)
                    csv_writer.writerow(['task_ID', 'user_ID', 'description', 'due_date', 'set_date', 'priority',
                                         'projects', 'link', 'location', 'status', 'delete_'])
                print('new account created')
                return user_ID
            else:
                print('confirm password does not match!')
        else:
            print('username already exist!')

    @staticmethod
    def log_in():
        """
        open the task csv file for the user
        :return: user id for the logged in user
        """
        column_names = ["user_ID", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        user_list = list(df.username)
        username = input('enter username: ')
        if username in user_list:
            i = user_list.index(username)
            password = input('enter password: ')
            hashed_pwd = hashlib.sha256(password.encode('utf8')).hexdigest()
            if hashed_pwd == df.password[i] and df.status[i] == 'enable':
                user_ID = df.user_ID[i]
                print(f'{username} logged in successfully')
                return user_ID

    @staticmethod
    def log_out(id):
        """
        gets id for logged in user finds its username and send a message about logging out successfully
        :return: does not return any thing
        """
        column_names = ["user_ID", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        id_list = df.user_ID
        i = id_list.index(id)
        username = df.username[i]
        print(f'{username} logged out successfully')

    @staticmethod
    def delete_account(id):
        """
        it will disable the account
        :return:
        """
        column_names = ["user_ID", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        id_list = df.user_ID
        i = list(id_list).index(id)
        "account.csv".replace(df.status[i], 'disable')
        username = df.username[i]
        print(f'{username} account deleted successfully')

    @staticmethod
    def change_password(id):
        """
        it will edit the user password but not any thing else
        :return:
        """
        column_names = ["user_ID", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        id_list = df.user_ID
        i = list(id_list).index(id)
        current_password = input('please enter your current password: ')
        current_hashed_pwd = hashlib.sha256(current_password.encode('utf8')).hexdigest()
        if current_hashed_pwd == df.password:
            new_password = input('please enter your new password: ')
            new_password_ = input('please confirm your new password: ')
            if new_password == new_password_:
                hashed_new_pwd = hashlib.sha256(new_password.encode('utf8')).hexdigest()
                "account.csv".replace(df.password[i], hashed_new_pwd)
                username = df.username[i]
                print(f'{username} password changed successfully')


if __name__ == '__main__':
    pass
