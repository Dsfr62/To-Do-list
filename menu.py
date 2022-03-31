import sys
from index import Task, Commands
from os import system

class Menu:
    """
    Display a menu and respond to choices when run.
    """

    def __init__(self):
        self.tasks = Commands()
        self.choices = {
            "1": self.show_tasks,
            "2": self.add_task,
            "3": self.modify_task,
            "4": self.finish,
            "5": self.clear_terminal,
            "6": self.quit,

        }
    
    def display_menu(self):
        print(
            """
            1. Show all tasks
            2. Add task
            3. Modify task
            4. Finish task
            5. Clear
            6. Quit
            """
        )

    def run(self):
        """
        Display the menu and respond to choices.
        """
        while True:
            self.display_menu()
            choice = input('Enter an option: ')
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
    
    def show_tasks(self, tasks = None):
        """
        Show all the tasks.
        """
        if not tasks:
            tasks = self.tasks.tasks
        for task in tasks:
            print("\n{0}: {1}\n".format(task.id, task.task))

    def add_task(self):
        """
        Add a new task in the list.
        """
        task = input('Enter the task: ')
        self.tasks.new_task(task)
        print("Your task has been added.\n")

    def modify_task(self):
        """
        Modify a task, using the id.
        """
        id = input('Enter the task id: ')
        task = input('Enter the task: ')
        self.tasks.modify_task(id, task)

    def finish(self):
        """
        This is for done tasks, picking then from the id_task
        """
        task_id = input('Enter the task id: ')
        self.tasks.finish_task(task_id)

    def clear_terminal(self):
        """
        This method is to clear the terminal.
        """
        system('cls')
    
    def quit(self):
        """
        This is to close the program
        """
        print("Bye my friend")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
    