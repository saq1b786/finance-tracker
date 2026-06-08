
import datetime

def add_transaction(transaction: list) -> None:
    ''' Asks the user for deatils about their specific income or expense. Then is appended to the transaction list. '''

    while True:

        income_or_expense = input('please enter whether you are adding an income or expense: ').lower()

        if income_or_expense not in ['income', 'expense']:
            print("that is an invalid option. Please enter 'income' or 'expense'. ")
        else:
            print(f"thank you for your repsonse. I can help you with adding an {income_or_expense} to the transaction list.")
            break
        
    while True:
        try:
            amount = float(input('please enter the amount: £'))
        except ValueError:
            print('you must input a number only greater than 0.')
            continue

        if amount <= 0:
            print('the amount must be greater than £0. Please try again')
        else:
            break    

    category = input(f"what category is this {income_or_expense} fall under (food, transport, bills, salary, entertainment etc): ").lower()

    description = input('a short description of the transaction: ')

    date = str(datetime.date.today())

    added_transaction = {
        'type': income_or_expense,
        'amount': amount, 
        'category': category,
        'description': description, 
        'date': date
    }

    transaction.append(added_transaction)

    print('the transaction has been added!')
            

def view_transactions(transaction: list) -> None:
    ''' Checks if the transaction list is empty. if not then prints out the transiction list for the user to see all existing transactions.'''

    if not transaction:
        print('There are no transactions in the list yet. sorry.')
        return
    else:
        for item in transaction:
            for key, value in item.items():
                print(f"{key} : {value}")

    

def get_summary(transaction: list) -> None:
    ''' Checks if the transiction list is empty. If not then calculates and prints total income, total expense and net balance for the user to see.'''
    total_income = 0
    total_expenses = 0 
    net_balance = 0

    if not transaction:
        print('There are no transactions in the list yet. sorry.')
        return
    
    for item in transaction:
        if item['type'] == 'income':
                total_income = total_income + item['amount']
        elif item['type'] == 'expense':
            total_expenses = total_expenses + item['amount']
            

    net_balance = total_income - total_expenses

    print(f"your total income is: £{total_income:.2f}")
    print(f"your total expenses is: £{total_expenses:.2f}")
    print(f"Your net balance is £{net_balance:.2f}")


def category_breakdown(transaction: list) -> None:
    ''' Checks if the transaction list is empty. If not calculates the expense total by category. if the category does not exist then it adds it to the categories list with the amount spent for the user to see.'''
    categories = {}
    if not transaction:
        print('There are no transactions in the list yet. sorry.')
        return
    
    for item in transaction:
        if item['type'] == 'expense':
            if item['category'] in categories:
                categories[item['category']] += item['amount']
            else:
                categories[item['category']] = item['amount']
    
    for category, amount in categories.items():
        print(f"{category} : £{amount:.2f}")


def main() -> None:
    choices = 0
    transaction = []

    while choices == 0:
        
        print('1. add transaction')
        print('2. view all transactions')
        print('3. view summary')
        print('4. view spending by category')
        print('5. quit')

        try:

            user_choice = int(input('please enter a number from the list above to choose which action you would like to take:'))
        except ValueError:
            print('you need to enter a number only between 1-5.')
            continue
    

        if user_choice == 1:
            add_transaction(transaction)
        elif user_choice == 2:
            view_transactions(transaction)
        elif user_choice == 3:
            get_summary(transaction)
        elif user_choice == 4:
            category_breakdown(transaction)
        elif user_choice == 5:
            break
        else:
            print('thats not a valid choice, please try again with a number between 1-5.')

            
main()