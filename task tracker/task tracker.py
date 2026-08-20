import json
import sys
from datetime import * 

running = True

tasks = []


#architecture: at the start load the JSON file into task objects
#useful chars:  🗹  ☐ 
  
id_index = 0

class Task:
    def __init__(self, title, status, id, createdAt, updatedAt):
        self.id = id
        self.title = title
        self.status = status #incompleted or completed
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        tasks.append(self)

    def displaySelf(self): #NOTE: perferably used in cases when it only needs to be called alone, like when adding
         pass
         
    def destroy(self):
        tasks.remove(self)

    def __str__(self):
        return f"{self.status} task: {self.title}"

        

TT1 = Task("poop", "completed", 1 , "8/18/2026", "8/18/2027")
TT2 = Task("eat urine","incompleted", 2 , "8/18/2026", "8/18/2027")


def printTask(t):
     print(f"   {"☐" if t.status == "incompleted" else "🗹"}     {t.id}   {t.title}  {t.createdAt}  {t.updatedAt}\n" )

def list_all():
        print("STATUS   ID   NAME    CREATED    UPDATED")

        for t in tasks:
            printTask(t)


def list_completed():
        
        print("STATUS   ID   NAME    CREATED    UPDATED")

        for t in tasks:
            if t.status == "completed":
                printTask(t)
                


def list_incompleted():
        print("STATUS   ID   NAME    CREATED    UPDATED")

        for t in tasks:
            if t.status == "incompleted":
                printTask(t)
                

#sets ID index based off existing tasks (run this AFTER importing JSON file)
def setIDIndex():
    IDVals = []
    for ta in tasks:
          IDVals.append(ta.id)
    return max(IDVals) + 1

#importing would go here

id_index = setIDIndex()

    
list_commands = {
    "all": list_all,
    "completed": list_completed,
    "incompleted" : list_incompleted
}

while running:

    menu_input = input("welcome to the TASK CLI. Don't forget to save before you leave!  \n")
    parts = menu_input.split()

    currentDate = str(datetime.now()).split()[0]
    currentTime =  str(datetime.now()).split()[1] #getr current times

    #print(parts) debug line
    #print(datetime.now()) returned 2026-08-18 23:02:29.654075
    if "help" == parts[0] or "h" == parts[0] or "man" == parts[0]:
         print(""" 
         first is a template for how to read others. each command has an example below it
         - mainCommand [subcommands (third identifier)] #description
                
         - list [status (all, completed, incompleted)] #lists all tasks, filtered by status 
            list all #lists all tasks regardless of completion

        - add [title] #add a task
            add say hello to bobby #adds "say hello to bobby" as a task

        - delete [ID] #deletes a task by ID. can check the list of tasks to find its id with "list all" 
            delete 3 #deletes task with ID of 3
        
        - complete [ID] #completes a task
            complete 3 #you get the idea 
        
        
        
           """)

    if "list" in parts[0] and len(parts)>1: #main command
        try: list_commands[parts[1]]() #subcommand tied to dict of the same type
        except: pass # if you mispell you nimwit dont worry you wont break the program

    if "add" in parts[0] and len(parts)>1:
        """        currentDate = str(datetime.now()).split()[0]
        currentTime =  str(datetime.now()).split()[1] #getr current times"""

        Task(" ".join(parts[1:]), "incompleted", id_index, f"created on {currentDate} at {currentTime}", f"updated on {currentDate} at {currentTime}")

        list_commands["all"]() #list updated tasklist

        id_index += 1

    if "delete" in parts[0] and len(parts)>1: #syntax: delete ID
        for t in tasks:
            if t.id == int(parts[1]):
                  
                  print(f" deleted {t}")
                  t.destroy()
                  list_commands["all"]()

    if "complete" in parts[0] and len(parts)>1: # complete ID
        for t in tasks:
            if t.id == int(parts[1]):
                t.status = "completed"
                t.updatedAt = f"updated on {currentDate} at {currentTime}"
                list_commands["all"]()

    if "save" in parts[0] and len(parts)>1:
         pass
    else:pass

""" TODO: 
        add the save and load feature
        add to the save feature the ability to delete all completed tasks before saving (or save excluding completed)
    """
         


    
