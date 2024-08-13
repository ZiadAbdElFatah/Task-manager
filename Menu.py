class Menu:
    @staticmethod
    def main_menu():
        print("Welcome to my Task manager!\n"
              "1.Add task\n"
              "2.Remove task\n"
              "3.Complete a task\n"
              "4.Show remaining tasks\n"
              "5.Show completed tasks\n"
              "Other.Exit")
        choice = input("Enter your choice: ")
        return choice

    @staticmethod
    def end_day():
        print("Thanks you for using my Task Manager!")
