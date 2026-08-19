import json
import sys
from datetime import * 

running = True

tasks = []


#architecture: at the start load the JSON file into task objects
#useful chars:  🗹  ◻  
  
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

        

TT1 = Task("poop", "completed", 1 , "8/18/2026", "8/18/2027")
TT2 = Task("eat urine","incompleted", 2 , "8/18/2026", "8/18/2027")


def list_all():
        print("STATUS   ID   NAME ")

        for t in tasks:
            print(f"{"◻" if t.status == "incompleted" else "🗹"}   {t.id}   {t.title} \n" )


def list_completed():
        
        print("STATUS   ID   NAME ")

        for t in tasks:
            if t.status == "completed":
                print(f"{"◻" if t.status == "incompleted" else "🗹"}   {t.id}   {t.title} \n" )


def list_incompleted():
        print("STATUS   ID   NAME ")

        for t in tasks:
            if t.status == "incompleted":
                print(f"{"◻" if t.status == "incompleted" else "🗹"}   {t.id}   {t.title} \n" )

#sets ID index based off existing tasks (run this AFTER importing JSON file)
def setIDIndex():
    IDVals = []
    for ta in tasks:
          IDVals.append(ta.id)
    return max(IDVals) + 1

id_index = setIDIndex()

    
list_commands = {
    "all": list_all,
    "completed": list_completed,
    "incompleted": list_incompleted
}

while running:

    menu_input = input("welcome to the TASK CLI. Don't forget to save before you leave!  \n")
    parts = menu_input.split()
    #print(parts) debug line
    #print(datetime.now()) returned 2026-08-18 23:02:29.654075
    if "list" in parts[0] and len(parts)>1: #main command
        list_commands[parts[1]]() #subcommand tied to dict of the same type

    if "add" in parts[0] and len(parts)>1:
        currentDate = str(datetime.now()).split()[0]
        currentTime =  str(datetime.now()).split()[1] #getr current times

        Task(parts[1:], "incompleted", id_index, f"saved on {currentDate} at {currentTime}", f"updated on {currentDate} at {currentTime}")

        list_commands["all"]() #list updated tasklist

        id_index += 1

    if "delete" in parts[0] and len(parts)>1: #syntax: delete ID
        for t in tasks:
             if t.id == parts[1]:
                  print(f" deleted {t.pop()}")
                  list_commands["all"]
         

    
    
         


### COMMIT TEST COMMENT
    
