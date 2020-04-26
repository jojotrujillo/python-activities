# Activity 4b

# global constants
TWO_HOURS_OR_LESS = 2
ONE_HOUR_OR_LESS = 1


def display_title():
    print('ISQA 3900 Metro Courier Service Delivery Calculator')


def get_delivery_price(time, weight):
    if weight > 50.0:  # cannot accept packages over 50 lbs.
        raise ValueError()

    if time == TWO_HOURS_OR_LESS:
        shipping_rate = 7.95
    elif time == ONE_HOUR_OR_LESS:
        shipping_rate = 9.95
    else:
        raise ValueError()  # invalid value

    return shipping_rate + (weight - 2.0)


def main():
    display_title()

    user_input = 'y'  # assign default value for at least one iteration
    while user_input.lower() == 'y':
        try:
            time_window = int(input('Base delivery of a 1 lb package is $7.95 for a 2 hour or less delivery. Add $2 \
for a 1 hour or less delivery.\nEnter 2 for 2 hour or less or a 1 for 1 hour or less:\t'))
            pounds = float(input('Enter weight of package in POUNDS. NUMBERS ONLY PLEASE! $1 per pound starting at 2 \
lbs up to 50 lbs:\t'))
            grade = get_delivery_price(time_window, pounds)
        except ValueError:
            print('\nCan\'t ship packages over 50 lbs, or you\'ve chosen an invalid time window. Please try again.\n')
            continue

        print('Total delivery Price for Package:\t' + str(grade))

        user_input = input('\nContinue (y/n)?: ')
        print()  # add a blank line for console output formatting

    print('Bye')


main()
# Done!
