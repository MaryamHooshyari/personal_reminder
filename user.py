# 2021.04.24
# Maryam Hooshyari
# personal reminder / user class

import pandas as pd
import hashlib
import csv


class User:

    def __init__(self, user_id, username, password, email, status=1):
        """

        :param user_id: user's ID (primary key)
        :param username: user's name
        :param password: user's password
        :param email: user's email
        :param status: shows if the account is enable or not ( 0=disable, 1=enable)
        """
        self.user_id = user_id
        self.username = username
        self.password = password
        self.email = email
        self.status = status

    @staticmethod
    def create_account(user_id):
        """
        create aan account for new user and a csv file for this user's tasks
        :return: user_id that shows how many user account made!
        """
        column_names = ["user_id", "username", "password", "E-mail", "status"]
        df = pd.read_csv("account.csv", names=column_names)
        user_list = list(df.username)
        username = input('enter username: ')
        if username not in user_list:
            password = input('enter password: ')
            password_ = input('confirm password: ')
            if password == password_:
                hashed_pwd = hashlib.sha256(password.encode('utf8')).hexdigest()
                email = input('enter your E-mail: ')
                object_user = User(user_id, username, hashed_pwd, email)
                row_account = [[object_user.user_id, object_user.username, object_user.password, object_user.email,
                                object_user.status]]
                with open('account.csv', 'a', newline='') as csv_account:
                    csv_writer = csv.writer(csv_account)
                    csv_writer.writerows(row_account)
                print('new account created')
                return user_id
            else:
                print('confirm password does not match!')
        else:
            print('username already exist!')

    def log_in(self):
        """
        open the task csv file for the user
        :return: user id for the logged in user
        """
        res = False
        for i in range(3):
            password = input('enter password: ')
            hashed_pwd = hashlib.sha256(password.encode('utf8')).hexdigest()
            if self.password == hashed_pwd and self.status == '1':
                res = True
                break
        return res

    # @staticmethod
    # def log_out(id):
    #     """
    #     gets id for logged in user finds its username and send a message about logging out successfully
    #     :return: does not return any thing
    #     """
    #     column_names = ["user_id", "username", "password", "E-mail", "status"]
    #     df = pd.read_csv("account.csv", names=column_names)
    #     id_list = df.user_id
    #     i = id_list.index(id)
    #     username = df.username[i]
    #     print(f'{username} logged out successfully')

    def delete_account(self):
        """
        change user's status from enable(1) to disable(0)
        :return: changed user's attributes in a list
        """
        self.status = 0
        user = [self.user_id, self.username, self.password, self.email, self.status]
        return user

    def change_password(self, password):
        """
        change user's password to a new one
        :param password: new password which user want to change
        :return: changed user's attributes in a list
        """
        hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
        self.password = hashed_password
        user = [self.user_id, self.username, self.password, self.email, self.status]
        return user


if __name__ == '__main__':
    pass
