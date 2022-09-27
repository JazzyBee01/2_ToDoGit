import json
import sys
#from classFile import Task, TaskList
from datetime import datetime

def readlists():
    global tasks
    global completed
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        print('geen tasks gevonden')
        tasks = []
        pass
    try:
        with open("completed.json","r") as f:
            completed = json.load(f)
    except FileNotFoundError:
        print('geen log file gevonden')
        completed = []
        pass

def savelists():
    with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    with open("completed.json","w") as f:
            json.dump(completed, f)


def useMenu():
    menu = '1. Toon taken\n2. Toon voltooid\n3. Voeg taak toe\n4. Verwijder taak\n5. Voltooi taak'
    print(menu)
    keuze = int(input('kies een optie (1/2/3/4/5): '))
    while keuze not in {1,2,3,4,5}:
        print('Geen geldige keuze')
        keuze = int(input('kies een optie (1/2/3/4/5): '))
    if keuze == 1:
        show(tasks)
    elif keuze ==2:
        show(completed)
    elif keuze ==3:
        addTask()
    elif keuze ==4:
        show(tasks)
        index = int(input('index of task to delete:'))
        deleteTask(index)
    elif keuze == 5:
        show(tasks)
        index = int(input('index of task to complete:'))
        completeTask(index)
    
def show(lijst):
    #true copy

    lijst.sort(key=lambda x:x[0])

    print('\tdatum\t\tvak\ttaak')
    print('----------------------+------+------')
    for i in range(len(lijst)):
        print(i, end = '\t')
        for veld in lijst[i]:
            print(veld, end='\t')
        print()


def addTask():
    task = []
    date =          input('date: ')
    course =        input('course: ')
    description =   input('description: ')
    task.append(date)
    task.append(course)
    task.append(description)
    tasks.append(task)

def deleteTask(index):
    awnser = input(f'Do you wish to delete {tasks[int(index)]} \n(y/n):')
    if awnser == "y":
        tasks.pop(int(index))
        print('item deleted')


def completeTask(index):
    completed.append(tasks.pop(index))

def showCourse(course):
    courseTasks = []
    for task in tasks:
        if task[1]==course:
            courseTasks.append(task)
    if len(courseTasks)>0:
        show(courseTasks)
    else:
        print('no tasks found for given course')
def clrList(list):
    if list == "tasks":
        tasks = []
    elif list == "completed":
        completed = []
def main():
    '''
    if no arguments are provided, you will be guided by a menu
    '''
    readlists()
    #check op systeemargumenten
    if len(sys.argv) > 1:
        print('sys arg found')
        if sys.argv[1] == "show":
            if len(sys.argv)>2:
                if sys.argv[2] == "completed":
                    show(completed)
                else:
                    print("invalid arg. try show or show completed")
            else:
                show(tasks)
        elif sys.argv[1] == "add":
            addTask()
        elif sys.argv[1] == "delete":
            deleteTask(sys.argv[2])
        elif sys.argv[1] == "complete":
            if sys.argv == "":
                print("need index")
            else:
                completeTask(sys.argv[2])
        elif sys.argv[1] == "course":
            if len(sys.argv) <3:
                print("need course name")
            else:
                showCourse(sys.argv[2])
        elif sys.argv[1] == "clear":
            if sys.argv == "":
                print("clear tasks or completed?")
            elif sys.argv[2] in ['tasks', 'completed']:
                clrList(sys.argv[2])
            else:
                print('invalid list')       
        else:
            print('invalid arguments. read the docs')

    
    #als geen systeem argumenten -> vragen stellen
    else:
        print ('no sys arg found')
        useMenu()
    
    savelists()

if __name__ == "__main__":
    main()

    
    