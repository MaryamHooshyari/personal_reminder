# 2021.04.24
# Maryam Hooshyari
# personal reminder / task class

from datetime import datetime
import csv


class Task:
    def __init__(self, task_ID, user_ID, description, due_date, set_date, priority=4, projects='inbox',
                 link=None, location=None, status='undone', delete_='enable'):
        """

        :param task_ID: task's ID (primary key)
        :param user_ID: the task's owner
        :param description: description of the task
        :param due_date: due date of task
        :param priority: the priority of task, it defines by importance and urgency on Eisenhower matrix
        :param projects: the project or the group which the task is about
        :param link: link of task or links about task
        :param location: location of task or place that task is going to happen
        :param status: status of task, if it's done or undone
        :param delete_: shows if the task is enable or not
        """
        self.task_ID = task_ID
        self.user_ID = user_ID
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
    def add_task(task_ID, user_ID):
        """
        to add a task
        :return: new task
        """
        description = input('please enter description of your task: ')
        due_date = input('when is the due date of this task? ')
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
        task_ID += 1
        object_task = Task(task_ID, user_ID, description, due_date, set_date, priority, project, link, location)
        row_task = [[object_task.task_ID, object_task.user_ID, object_task.description, object_task.due_date,
                     object_task.set_date, object_task.priority, object_task.projects, object_task.link,
                     object_task.location, object_task.status, object_task.delete_]]
        with open(str(user_ID)+'_task.csv', 'a', newline='') as csv_task:
            csv_writer = csv.writer(csv_task)
            csv_writer.writerows(row_task)
        print('new task added')
        return task_ID

    def edit(self):
        """
        to edit a task that already exist
        :return: edited task
        """
        pass

    def delete(self):
        """
        to delete a task
        :return:
        """
        pass

    @staticmethod
    def in_calendar():
        """
        it will detect all undone tasks
        :return: shows all undone tasks in calendar
        """
        pass

    @classmethod
    def display_tasks(cls, task_status, period):
        """

        :param task_status: if the tasks we want to show are done or undone
        :param period: what is the period of time we want to show (a day, a week or a month)
        :return: a list of done/ undone tasks for the period we picked
        """
        pass

    def share(self, sender, receiver):
        """

        :param sender: class user, the user who wants to share the task
        :param receiver: class user, the user who is going to receive the task
        :return:
        """
        pass


if __name__ == '__main__':
    pass
