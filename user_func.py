# May 2021
# Maryam Hooshyari
# personal reminder / user_id, create_account, add_user_to_file, save_user

import csv
import hashlib
from user import User
import pandas as pd


def user_id():
    """
    counts how many lines exists in account.csv file which means the number of users plus one(title row)
    :return: id for new user
    """
    with open('account.csv') as ac:
        id = sum(1 for line in ac)
    return id


def create_account(id):
    """
    (int) --> class User obj
    create an account for new user
    :return: new user which just created
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
            new_user = User(id, username, hashed_pwd, email)
            return new_user
        else:
            print('confirm password does not match!')
    else:
        print('username already exist!')


def add_user_to_file(user):
    row_account = [[user.user_id, user.username, user.password, user.email, user.status]]
    with open('account.csv', 'a', newline='') as csv_account:
        csv_writer = csv.writer(csv_account)
        csv_writer.writerows(row_account)


def save_user(user):
    with open("account.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        save_lines = []
        for line in reader:
            if line[0] == user.user_id:
                line = [user.user_id, user.username, user.password, user.email, user.status]
            save_lines.append(line)
    with open("account.csv", 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerows(save_lines)
