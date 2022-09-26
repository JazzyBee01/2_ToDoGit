import json
import sys

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
    menu = '1. Toon taken\n2. Voltooi taak\n3. Voeg taak toe\n4. Verwijder taak\n 5. Toon voltooid'
    print(menu)

    keuze = int(input('kies een optie (1/2/3/4/5): '))
    while keuze not in {1,2,3,4,5}:
        print('Geen geldige keuze')
        keuze = int(input('kies een optie (1/2/3/4/5): '))
    
def show(lijst):
    #true copy
    a = []
    for i in lijst:
        a.append(i)
    #sort by date
    a.sort(key=lambda x:x[0])

    print('datum\t\tvak\ttaak')
    print('---------------+------+------')
    for item in a:
        for veld in item:
            print(veld, end='\t')
        print()
    


    ...

def addTask(list):
    tasks.append(list)
def deleteTask(index):
    ...
def completeTask(index):
    ...
def showCourse(course):
    ...
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
            if sys.argv[2] == "tasks":
                show(tasks)
            elif sys.argv[2] == "completed":
                show(completed)
            else:
                print("invalid arg. try show tasks or show completed")
        
        elif sys.argv[1] == "add":
            addTask(sys.argv[2])
        
        elif sys.argv[1] == "delete":
            if sys.argv == "":
                print("need index")
            else:
                deleteTask(sys.argv[2])

        elif sys.argv[1] == "complete":
            if sys.argv == "":
                print("need index")
            else:
                completeTask(sys.argv[2])

        elif sys.argv[1] == "course":
            if sys.argv == "":
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