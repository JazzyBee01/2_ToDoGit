from datetime import datetime

class TaskList:
    def __init__(self, tasks=[]):
        self.tasks = tasks

class Task:
    def __init__(self, date=datetime.today(), course='', description=''):
        self.date = datetime.date(date)
        self.course = course
        self.description = description

    def __repr__(self):
        return f'{self.date}\t\t{self.course}\t{self.description}'


def main():
    tl = TaskList()
    

if __name__ == "__main__":
    main()