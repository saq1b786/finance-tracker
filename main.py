

def add_transaction():
    pass

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
            print('you need to enter a number')
            continue
    

        if user_choice == 1:
            add_transaction()
        elif user_choice == 2:
            view_transactions()
        elif user_choice == 3:
            get_summary()
        elif user_choice == 4:
            category_breakdown()
        elif user_choice == 5:
            break
        else:
            print('thats not a valid choice, please try again')

            
main()