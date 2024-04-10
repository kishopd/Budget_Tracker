class Budget:
    def __init__(self):
        self.budget_list = {}
        self.current_balance = 0

    def add_income(self):
        print("e.g: salary, freelance work")
        type_of_income = int(input("Enter how many types of income: "))
        for i in range(type_of_income):
            work_type = input("Enter the income source name: ")
            amount = float(input(f"Enter the amount received from {work_type}: "))
            self.budget_list[work_type] = amount
        print("Income list added successfully.")

    def expenses(self):
        print("e.g: Groceris expenses, School fee, emi, ")
        type_of_expense = int(input("Enter how many expenses: "))
        for i in range(type_of_expense):
            expense_name = input("Enter the expense name: ")
            expense_amount = float(input(f"Enter the expense amount for {expense_name}: "))
            self.budget_list[expense_name] = -expense_amount
        print("Expenses list added successfully.")

    def transaction(self):
        if not self.budget_list:
            print("There are no transactions.")
        else:
            print("Transaction history:")
            for key, value in self.budget_list.items():
                print(key,value)

    def view_balance(self):
        for key,value in self.budget_list.items():
            self.current_balance = self.current_balance + value
        print("Total balance:", self.current_balance)
        

    def main():
        budget = Budget()
        while True:
            print("----->Budget List<--------")
            option_list = """
            1. Add Income 
            2. Expense List
            3. Transaction List
            4. View Balance
            5. Exit 
            """
            print(option_list)
            option = int(input("Enter the option: "))
            if option == 1:
                budget.add_income()
            elif option == 2:
                budget.expenses()
            elif option == 3:
                budget.transaction()
            elif option == 4:
                budget.view_balance()
            elif option == 5:
                print("Thank you for using the application!")
                break
            else:
                print("Please enter a valid option.")


if __name__ == "__main__":
    Budget.main()
