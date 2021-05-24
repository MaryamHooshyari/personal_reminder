# May 2021
# Maryam Hooshyari
# personal reminder / task class


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

    def edit_title(self, title):
        """
        change the task's title
        :param title: new title for task
        :return: changed task
        """
        self.title = title
        return self

    def edit_description(self, description):
        """
        change the task's description
        :param description: new description for task
        :return: changed task
        """
        self.description = description
        return self

    def edit_priority(self, priority):
        """
        change the task's priority
        :param priority: new priority for task
        :return: changed task
        """
        self.priority = priority
        return self

    def edit_projects(self, projects):
        """
        change the task's projects
        :param projects: new projects for task
        :return: changed task
        """
        self.projects = projects
        return self

    def edit_link(self, link):
        """
        change the task's link
        :param link: new link for task
        :return: changed task
        """
        self.link = link
        return self

    def edit_location(self, location):
        """
        change the task's location
        :param location: new location for task
        :return: changed task
        """
        self.location = location
        return self

    def postpone(self, due_date):
        """
        change the task's due date
        :param due_date: new due date for task
        :return: changed task
        """
        self.due_date = due_date
        return self

    def delete(self):
        """
        change task's delete_ attribute form 1 to 0 which means the task is disable
        :return: changed task
        """
        self.delete_ = 0
        return self

    def done(self):
        """
        change task's status attribute form 0 to 1 which means the task is done
        :return: changed task
        """
        self.status = 1
        return self

    def share(self, sender, receiver, shared_task_id):
        """

        :param shared_task_id: an id use for share_task.csv primary key
        :param sender: class user, the user who wants to share the task
        :param receiver: username for the user who is going to receive the task
        :return: a row with shared task informations use to save in share_task.csv
        """
        share_task = [shared_task_id, sender, receiver, self.title, self.description, self.due_date,
                      self.priority, self.projects, self.link, self.location, 0, 0]
        """
        two last parameters which are both 0 valued are for checking
        first one, column name is accept/deny if value is 0 request is denied and  if it's 1 request is accepted
        by default it's 0 means denied until receiver check and accept it
        second one, column name is check if value is 0 request is not checked yet and  if it's 1 request is checked
        """
        return share_task
