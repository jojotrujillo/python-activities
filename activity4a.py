# Activity 4a


def display_title():
    print('ISQA 3900 Letter Grade Calculator')


def get_grade(points):
    # final_grade grade e.g., 95%
    final_grade = points / 1000 * 100  # e.g. 95 / 1000 = 0.95 * 100 = 95%

    if 97 <= final_grade <= 100:
        letter_grade = 'A+'
    elif 93 <= final_grade < 97:
        letter_grade = 'A'
    elif 90 <= final_grade < 93:
        letter_grade = 'A-'
    elif 87 <= final_grade < 90:
        letter_grade = 'B+'
    elif 83 <= final_grade < 87:
        letter_grade = 'B'
    elif 80 <= final_grade < 83:
        letter_grade = 'B-'
    elif 77 <= final_grade < 80:
        letter_grade = 'C+'
    elif 73 <= final_grade < 77:
        letter_grade = 'C'
    elif 70 <= final_grade < 73:
        letter_grade = 'C-'
    elif 67 <= final_grade < 70:
        letter_grade = 'D+'
    elif 63 <= final_grade < 67:
        letter_grade = 'D'
    elif 60 <= final_grade < 63:
        letter_grade = 'D-'
    elif final_grade < 60:
        letter_grade = 'F'
    else:
        raise ValueError('Invalid value')

    return letter_grade


def main():
    display_title()

    user_input = 'y'  # assign default value for at least one iteration
    while user_input.lower() == 'y':
        try:
            total_points = int(input('\nEnter total number of points earned:\t'))
            grade = get_grade(total_points)
        except ValueError:  # catch ValueErrors; return message, then continue loop
            print('\nYou have entered an incorrect value. Please try again.')
            continue

        print('Letter grade:', grade)

        user_input = input('\nContinue (y/n)?: ')

    print('\nBye')


# run main
main()
# Done!
