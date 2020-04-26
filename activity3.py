# Activity 3


# define calculate_discount function
def calculate_discount(grade, length):
    if grade == 1:
        price = 2
    elif grade == 2:
        price = 1
    else:
        raise ValueError('Invalid value')

    # calculate subtotal cost of lumber
    subtotal = length * price

    if 0 <= subtotal < 10000:
        discount = 0
    elif 10000 <= subtotal <= 50000:
        discount = 0.1
    elif subtotal > 50000:
        discount = 0.2

    # total is assigned the subtotal minus amount of discount
    total = subtotal - (subtotal * discount)

    return total


# define main function
def main():
    print('ISQA 3900 Lumber Price Calculator\n')

    # initialize while loop index
    user_input = 'y'
    while user_input == 'y':
        print('You will be asked the number of board feet for the purchase and the type of lumber (common or select)')

        # catch any exception from input and catch any invalid values
        try:
            length_in_feet = float(input('Enter number of board feet:\t'))
            lumber_grade = float(input('Enter a 1 for select lumber or a 2 for common lumber:\t'))
            final_price = calculate_discount(lumber_grade, length_in_feet)
        except ValueError:
            print('\nYou have entered an incorrect value. Please try again.\n')
            continue

        print('Total price for the lumber is\t' + f'{final_price:,.2f}' + '\n')
        user_input = input('Continue (y/n)?: ')


# run main function
main()
# Done!
