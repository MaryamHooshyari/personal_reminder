# May 2021
# Maryam Hooshyari
# personal reminder / user class


import hashlib


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

    def log_in(self):
        """
        (User object) --> bool
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

    def delete_account(self):
        """
        (User  object) --> User object
        change user's status from enable(1) to disable(0)
        :return: changed user's attributes in a list
        """
        self.status = 0
        return self

    def change_password(self, password):
        """
        (User  object) --> User object
        change user's password to a new one
        :param password: new password which user want to change
        :return: changed user's attributes in a list
        """
        hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
        self.password = hashed_password
        return self
