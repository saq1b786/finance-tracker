
import datetime

def add_transaction(transaction):
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
            


        
        

def view_transactions():
    pass


def get_summary():
    pass

def category_breakdown():
    pass



def main():
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
            view_transactions()
        elif user_choice == 3:
            get_summary()
        elif user_choice == 4:
            category_breakdown()
        elif user_choice == 5:
            break
        else:
            print('thats not a valid choice, please try again with a number between 1-5.')

            
main()