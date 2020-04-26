''' Activity 8 '''
# pylint: disable=invalid-name
from customer import Customer

def main():
    """
    give user context, prompt for user id to search for, then ask to continue
    """
    print('Customer Viewer')

    customers = Customer()

    user_input = 'y'
    while user_input == 'y':
        try:
            customers_address = customers.search_for_id(int(input('\nEnter customer ID: ')))

            print('\n' + customers_address + '\n')
        except ValueError as e:
            print(str(e))

        user_input = input('Continue? (y/n): ')

    print('\nBye!')

main()
