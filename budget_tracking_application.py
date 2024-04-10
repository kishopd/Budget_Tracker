def my_function():
    dict_values = {}
    while True:
        option_list = """ 
                     1. Add income
                     2. Expense list 
                     3. View transition 
                     4. View balance 
                     5. Exit 
                     """
        print(option_list)
        option = int(input("Enter the option: "))

        if option == 1:
            type_of_income = int(input("Enter how many types of income: "))
            for i in range(type_of_income):
                work_type = input("Enter the work name: ")
                salary = float(input("Enter the salary: "))
                dict_values[work_type] = salary
            print(dict_values)

        elif option == 2:
            number_of_expenses = int(
                input("Enter how many number of expenses: "))
            for i in range(number_of_expenses):
                expenses_name = input("Enter the expenses name: ")
                expenses_amount = float(input("Enter the expense amount: "))
                dict_values[expenses_name] = -expenses_amount
            print(dict_values)

        elif option == 3:
            if not dict_values:
                print("There are no transitions.")
            else:
                for key, value in dict_values.items():
                    print(key, value)

        elif option == 4:
            total_balance = 0
            for key , value in dict_values.items():
                total_balance = total_balance + value
            
            print("Total balance:", total_balance)

        elif option == 5:
            break


my_function()
