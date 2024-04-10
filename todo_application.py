def todo_application():
    while True:
        print("Todo application ")
        #showing the options here 
        print("""
              1.Add Task
              2.View Task 
              3.Remove Task
              
              4.Mark as completed 
              5.exit""")
        option=int(input("choose the option here : "))
        if option ==1:
            task=[]
            number_of_tasks=int(input("enter the number of task : "))
            for i in range (number_of_tasks):
                i= input(f" Give the task {i+1} : ")
                task.append(i)
            print("Tasks are added successfully")
            # for j in range(len(task)):
            #     print(j+1,":",task[j])
        elif option==2:
            print("please check the tasks below")
            for j in range(len(task)):
                print(j+1, ":", task[j])
        elif option == 3:
            # removed_task=[]
            removed_task_item=int(input("Enter the index number to remove : "))
            task.pop(removed_task_item)
            print(f"The item is removed succesfully")
        elif option == 4:
            completd_item=[]
            finished_index=int(input("Enter the finished index name : "))
            for i in range(len(task)):
                if i == finished_index:
                    completd_item.append(task[i])
            print(f"The completed items are {completd_item}")
            # for j in task:
            #     if j not in completd_item:
            #         task.append(j)
            # print(task)
            
        elif option ==5:
            print("Thank You for using our Application ")
            break
        else:
            print("please enter the correct option in here")
todo_application()
