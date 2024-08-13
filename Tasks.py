class Tasks:
    completed_tasks = []
    remaining_tasks = []

    def __init__(self):
        self.completed_tasks = []
        self.remaining_tasks = []

    def add_task(self, task):
        self.remaining_tasks.append(task)

    def complete_task(self, task):
        self.completed_tasks.append(self.remaining_tasks[task - 1])
        self.remaining_tasks.pop(task - 1)

    def remove_task(self, task):
        self.remaining_tasks.pop(task - 1)

    def show_remaining_tasks(self):
        if len(self.remaining_tasks) == 0:
            print("No tasks remaining")
        else:
            print("Remaining tasks:")
            for number, task in enumerate(self.remaining_tasks, start=1):
                print(f"{number}. {task}")
            print('\n')

    def show_completed_tasks(self):
        if self.completed_tasks.__len__() == 0:
            print("No tasks completed.")
        else:
            print("Completed tasks:")
            for number, task in enumerate(self.completed_tasks, start=1):
                print(f"{number}. {task}")
            print('\n')

