# May 2021
# Maryam Hooshyari
# personal reminder / task_id, add_task_to_file, save_task, create_task, display_task, is_leap, in_calendar


import csv
from datetime import datetime, date
from termcolor import colored
from task_class import Task


def task_id():
    """
    counts how many lines exists in task_list.csv file which means the number of tasks plus one(title row)
    :return: id for new task
    """
    with open('task_list.csv') as tl:
        id = sum(1 for line in tl)
    return id


def add_task_to_file(task):
    """
    (task object) --> None
    this will just save the task file as a row in task_list.csv
    :param task: a task object user wants to save
    :return: None
    """
    row_task = [[task.task_id, task.user_id, task.title, task.description, task.due_date, task.set_date,
                 task.priority, task.projects, task.link, task.location, task.status, task.delete_]]
    with open('task_list.csv', 'a', newline='') as csv_task:
        csv_writer = csv.writer(csv_task)
        csv_writer.writerows(row_task)


def save_task(task):
    """
    rewrites a task row to task_list.csv file
    :param task: task object which is going to save
    :return: nothing
    """
    with open("task_list.csv", 'r') as ts:
        reader = csv.reader(ts, delimiter=',')
        save_lines = []
        for line in reader:
            if line[0] == task.task_id:
                line = [task.task_id, task.user_id, task.title, task.description, task.due_date, task.set_date,
                        task.priority, task.projects, task.link, task.location, task.status, task.delete_]
            save_lines.append(line)
    with open("task_list.csv", 'w', newline='') as ts:
        writer = csv.writer(ts, delimiter=',')
        writer.writerows(save_lines)


def create_task(user_id):
    """
    (int) + inputs --> task object
    get a id which is for the user  who is going to make a task
    :param user_id: id for task owner
    :return: task object
    """
    id = task_id()
    title = input('please enter title of your task: ')
    description = input('please enter description of your task: ')
    day = list(map(int, input('when is the due date of this task? (yyyy,mm,dd,hh,mm) ').split(',')))
    due_date = datetime(day[0], day[1], day[2], day[3], day[4], 0)
    importance = input('is this task important? (yes / no)(default: no) ')
    urgency = input('is this task urgent? (yes / no)(default: no) ')
    project = input("what is the task's project? (default: inbox)")
    link = input('please enter related links to the task: ')
    location = input('please enter related locations to the task: ')
    set_date = datetime.now()
    priority = 4
    if importance == 'yes' and urgency == 'yes':
        priority = 1
    elif importance == 'yes' and urgency == 'no':
        priority = 2
    elif importance == 'no' and urgency == 'yes':
        priority = 3
    elif importance == 'no' and urgency == 'no':
        priority = 4
    new_task = Task(id, int(user_id), title, description, due_date, set_date, priority, project, link, location)
    return new_task


def display_task(user_id, status, period):
    """
    shows a list of selected tasks
    :param user_id: id for tasks' owner
    :param status: status for tasks want to see(done or undone)
    :param period: period of time choosed for task show(a day, a week, a month)
    :return: list of selected tasks with particular conditions
    """
    now = datetime.now()
    with open("task_list.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        lines = []
        for line in reader:
            # line[4] is task's due date
            if line[1] == user_id and line[10] == status:
                """
                line[1]: task owner's id
                line[10]: task status attribute (0 means undone and 1 means undone)
                this will collect all tasks on user conditions (status: done or undone)
                """
                due_date = datetime(int(line[4][0:4]), int(line[4][5:7]), int(line[4][8:10]))
                delta_day = (due_date.date() - now.date()).days
                if delta_day < period:
                    """
                    delta_day: shows how many days are between now and task's due date
                    this will collect all tasks on user conditions (time difference: a day, a week, a month)
                    """
                    lines.append(line)
    return lines


def is_leap(yr):
    """
    (int) -> bool
    Checks if year is a leap year
    called by in_calendar function
    """
    if yr % 4 == 0:
        if yr % 100 == 0:
            if yr % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def in_calendar(user_id):
    """
    (int) --> None
    this will find all the tasks which are for particular user, undone and enable
    then asks user about which month wants to see
    :param user_id: task owner's id
    :return: None
    called by task_menu function
    """
    calendar_task = []
    with open("task_list.csv", 'r') as f:
        reader = csv.reader(f, delimiter=',')
        i = 1
        for line in reader:
            if line[1] == user_id and line[11] == 1 and line[10] == 0:
                """
                line[1]: task owner's id
                line[10]: task status attribute (0 means undone)
                line[11]: task delete attribute (1 means enable)
                only undone and enable tasks matters to show
                """
                limited_task = [line[2:5]]
                """
                calendar_task is a list of undone and enable tasks which are for our present user
                each task will save in to this list with its title, description and due date
                """
                calendar_task.append(limited_task)
    # minus 1 is for list index I use later in code
    month_now = datetime.now().month - 1
    year_now = datetime.now().year
    month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September',
             'October', 'November', 'December']
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    print('which month you want to check?')
    menu_res = []
    for i in range(6):
        """
        make a menu for user to choose which month wants to show
        it includes 6 months from now!
        """
        if month_now == 12:
            print(f'{i + 1}-{month[month_now + i]} {year_now}')
            menu_res.append((month_now, year_now))
            month_now = 1
            year_now += 1
        else:
            print(f'{i + 1}-{month[month_now + i]} {year_now}')
            menu_res.append((month_now, year_now))
    calendar_input = int(input('- '))
    month_name, year = menu_res[calendar_input - 1]
    due_date_list = []
    for task in calendar_task:
        if int(task[3][5:7]) == (month.index(month_name)+1):
            due_date_list.append(int(task[3][8:10]))
    due_date_list = sorted(set(due_date_list))
    if is_leap(year):  # check if the year is leap
        days_in_month[1] = 29
    month_day = days_in_month[month.index(month_name)]
    day_one = date(year, month.index(month_name), 1)  # make the date of first day of month
    start_day = day_one.isoweekday()  # returns a number between 0 to 6 which shows what is the day in the week
    # show calendar: if user has task in a day that day will be printed red
    print(f'{month_name} {year}')
    print("Sun Mon Tue Wed Thu Fri Sat")
    i = 1 - start_day
    while i <= month_day:
        if 0 < i < 10:
            if i in due_date_list:
                print("", colored(i, 'red'), end="  ")
            else:
                print("", i, end="  ")
        elif i <= 0:
            print("  ", end="  ")
        else:
            if i in due_date_list:
                print(colored(i, 'red'), end="  ")
            else:
                print(i, end="  ")
        if (i + start_day) % 7 == 0:
            print(" ")
        i += 1
    print()  # just to make a new line
    # now prints all tasks for the month in list
    for j in due_date_list:
        for task in calendar_task:
            if j == int(task[3][8:10]) and int(task[3][5:7]) == (month.index(month_name)+1):
                print(f'{j} --> {task[0]}:{task[1]}')


