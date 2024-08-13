import os
from Tasks import Tasks
from Menu import Menu


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


class Program:
    def __init__(self):
        self.tasks = Tasks()
        self.menu = Menu()

    def run(self):

        while True:
            clear_screen()
            if len(self.tasks.remaining_tasks) > 0:
                self.tasks.show_remaining_tasks()
            choice = self.menu.main_menu()
            if choice == '1':
                clear_screen()
                self.tasks.add_task(input("Enter Task Name you want to add: "))
                clear_screen()
            elif choice == '2':
                if len(self.tasks.remaining_tasks) > 0:
                    clear_screen()
                    option = self.choose_task_to_remove()
                    self.tasks.remove_task(option)
                    clear_screen()
                else:
                    print("No Tasks remaining to remove")
            elif choice == '3':
                if len(self.tasks.remaining_tasks) > 0:
                    clear_screen()
                    option = self.choose_task_to_complete()
                    self.tasks.complete_task(option)
                    clear_screen()
                    self.tasks.show_completed_tasks()
                else:
                    print("No Tasks remaining to complete")
            elif choice == '4':
                self.tasks.show_remaining_tasks()
                continue
            elif choice == '5':
                clear_screen()
                self.tasks.show_completed_tasks()
            else:
                clear_screen()
                self.menu.end_day()
                print(f"Completed tasks: {self.tasks.show_completed_tasks()}")
                print(f"Remaining tasks: {self.tasks.show_remaining_tasks()}")
                break
            self.tasks.show_remaining_tasks()
            bye = self.continue_or_quit()
            if bye == "2":
                break

    def choose_task_to_remove(self):
        self.tasks.show_remaining_tasks()
        while True:
            choice = input("Enter the number of the task to remove: ")
            if choice.isdigit() and 0 < int(choice) <= len(self.tasks.remaining_tasks):
                break
            else:
                print("Invalid number")
        return int(choice)

    def choose_task_to_complete(self):
        self.tasks.show_remaining_tasks()
        while True:
            choice = input("Enter the number of the task to complete: ")
            if choice.isdigit() and 0 < int(choice) <= len(self.tasks.remaining_tasks):
                break
            else:
                print("Invalid number")
        return int(choice)

    def continue_or_quit(self):
        while True:
            print("1.Continue\n2.Quit: ")
            choice = input("What would you like to do? ")
            if choice == '1':
                clear_screen()
                break
            elif choice == '2':
                self.menu.end_day()
                print(f"Completed tasks: {self.tasks.show_completed_tasks()}")
                print(f"Remaining tasks: {self.tasks.show_remaining_tasks()}")
                break
            else:
                print("Invalid choice")
        return choice


program = Program()
program.run()
