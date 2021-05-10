# 2021.04.24
# Maryam Hooshyari
# personal reminder / task class

from datetime import datetime, date
import csv
import pandas as pd


class Task:
    def __init__(self, task_id, user_id, title, description, due_date, set_date, priority=4, projects='inbox',
                 link=None, location=None, status=0, delete_=1):
        """

        :param task_id: task's ID (primary key)
        :param user_id: the task's owner
        :param title: title of the task
        :param description: description of the task
        :param due_date: due date of task
        :param priority: the priority of task, it defines by importance and urgency on Eisenhower matrix
        :param projects: the project or the group which the task is about
        :param link: link of task or links about task
        :param location: location of task or place that task is going to happen
        :param status: status of task, if it's done or undone (0=undone, 1=done)
        :param delete_: shows if the task is enable or not (0=disable, 1=enable)
        """
        self.task_id = task_id
        self.user_id = user_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.projects = projects
        self.link = link
        self.location = location
        self.set_date = set_date
        self.status = status
        self.delete_ = delete_

    @staticmethod
    def add_task(task_id, user_id):
        """
        make new task
        :param task_id: id of previous task plus it with one and use as this new task id
        :param user_id: task owner's id
        :return: new task
        """
        title = input('please enter title of your task: ')
        description = input('please enter description of your task: ')
        day = list(map(int, input('when is the due date of this task? (yyyy,mm,dd,hh,mm,ss) ').split(',')))
        due_date = datetime(day[0], day[1], day[2], day[3], day[4], day[5])
        importance = input('is this task important? (yes / no)')
        urgency = input('is this task urgent? (yes / no)')
        project = input("what is the task's project? (default: inbox)")
        link = input('please enter related links to the task: ')
        location = input('please enter related locations to the task: ')
        set_date = datetime.now()
        if importance == 'yes' and urgency == 'yes':
            priority = 1
        elif importance == 'yes' and urgency == 'no':
            priority = 2
        elif importance == 'no' and urgency == 'yes':
            priority = 3
        elif importance == 'no' and urgency == 'no':
            priority = 4
        task_id += 1
        object_task = Task(task_id, user_id, title, description, due_date, set_date, priority, project, link, location)
        row_task = [[object_task.task_id, object_task.user_id, object_task.title, object_task.description,
                     object_task.due_date, object_task.set_date, object_task.priority, object_task.projects,
                     object_task.link, object_task.location, object_task.status, object_task.delete_]]
        with open('task_list.csv', 'a', newline='') as csv_task:
            csv_writer = csv.writer(csv_task)
            csv_writer.writerows(row_task)
        return task_id

    def edit_title(self, title):
        """
        change the task's title
        :param title: new title for task
        :return: changed task
        """
        self.title = title
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def edit_description(self, description):
        """
        change the task's description
        :param description: new description for task
        :return: changed task
        """
        self.description = description
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def edit_priority(self, priority):
        """
        change the task's priority
        :param priority: new priority for task
        :return: changed task
        """
        self.priority = priority
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def edit_projects(self, projects):
        """
        change the task's projects
        :param projects: new projects for task
        :return: changed task
        """
        self.projects = projects
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def edit_link(self, link):
        """
        change the task's link
        :param link: new link for task
        :return: changed task
        """
        self.link = link
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def edit_location(self, location):
        """
        change the task's location
        :param location: new location for task
        :return: changed task
        """
        self.location = location
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def postpone(self, due_date):
        """
        change the task's due date
        :param due_date: new due date for task
        :return: changed task
        """
        self.due_date = due_date
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def delete(self):
        """
        change task's delete_ attribute form 1 to 0 which means the task is disable
        :return: changed task
        """
        self.delete_ = 0
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    def done(self):
        """
        change task's status attribute form 0 to 1 which means the task is done
        :return: changed task
        """
        self.status = 1
        task = Task(self.task_id, self.user_id, self.title, self.description, self.due_date, self.set_date,
                    self.priority, self.projects, self.link, self.location, self.status, self.delete_)
        return task

    @staticmethod
    def display_task(user_id, status, period):
        now = datetime.now()
        with open("task_list.csv", 'r') as f:
            reader = csv.reader(f, delimiter=',')
            lines = []
            for line in reader:
                # line[4] is task's due date
                delta_day = (line[4].date() - now.date()).days
                if line[1] == user_id and line[10] == status and delta_day < period:
                    """
                    line[1]: task owner's id
                    line[10]: task status attribute (0 means undone and 1 means undone)
                    delta_day: shows how many days are between now and task's due date
                    this will collect all tasks on user conditions (status: done or undone & 
                    """
                    lines.append(line)
        return lines

    @staticmethod
    def in_calendar(user_id):
        """
        shows all undone tasks for a particular user in a calender
        :param user_id: task owner ID
        :return:
        """
        pass

    def share(self, sender, receiver):
        """

        :param sender: class user, the user who wants to share the task
        :param receiver: username for the user who is going to receive the task
        :return:
        """

        share_task = [shared_task_id, sender.username, receiver, self.title, self.description, self.due_date, self.priority,
                      self.projects, self.link, self.location, 0, 0]
        return share_task


if __name__ == '__main__':
    pass
