# Activity 5b
import re  # regular expression module


def main():
    print('Discount Calculator\n'
          'Enter \'x\' to exit\n')

    item_prices = []

    while True:  # hard-coded boolean True because thrown ValueError from input() acts as loop control
        try:
            temp = float(input('Enter item price: '))

            if temp > 250.001:
                print('Item amounts must be from 0 through 250. Price too high. Item discarded. Try again.')
                continue
            else:
                item_prices.append(temp)
        except ValueError as err:
            user_exit = str(re.findall(r"\'(.*?)\'", str(err.args)))
            if user_exit.lower() == '[\'x\']':
                break
            else:
                print('Invalid entry. Enter item price or \'x\' to exit. Try again.')

    total = 0.0
    for price in item_prices:
        total += price

    num_of_prices = len(item_prices)

    discount = 0
    if total >= 500:
        discount = 0.3
    elif 200 <= total <= 499.99:
        discount = 0.2
    elif total < 200:
        discount = 0

    print('\nPrices:\t\t\t' + str(item_prices) + '\n'
          'Total:\t\t\t%.2f' % round(total, 2) + '\n'
          'Number of Prices:\t' + str(num_of_prices) + '\n'
          'Average Price:\t\t%.2f' % round(total / num_of_prices, 2) + '\n'
          'Discount:\t\t' + str(int(discount * 100)) + '%')
    print('Discounted Price:\t$%.2f' % round(total - (total * discount), 2) + '\n'
          '\nBye!')


# run main()
main()
# Done!
