import datetime

last_id = 0

class Task:

    """
    Represent a task in the list.
    """

    def __init__(self, task):
        """
        Initialize a task.
        """
        self.task = task + ' - Not done'
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        """
        Determine if this task matches the filter text.
        """
        return filter in self.task

class Commands:
    """
    Represent a collection of tasks that can be modified and finished.
    """

    def __init__(self):
        """
        Initialize a empty list for tasks.
        """
        self.tasks = []

    def new_task(self, task):
        """
        Create a new task.
        """
        self.tasks.append(Task(task))
    
    def modify_task(self, task_id, task):
        """
        Find the task with the given id and change the task to the given value
        """
        for row in self.tasks:
            if str(row.id) == str(task_id):
                row.task = task + ' - Not done'
                print('Task modified with sucess')
                break

    def finish_task(self, task_id):
        """
        Find the task with the given id and change the progress to done
        """
        for row in self.tasks:
            if str(row.id) == str(task_id):
                row.task = row.task.replace(' - Not done', ' - Done')
                print('Great job!')
                break
            