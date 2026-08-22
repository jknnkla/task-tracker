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
        
        - save all #saves it all dumbass