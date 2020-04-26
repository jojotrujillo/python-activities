# Activity 6
import csv, os


def list_file_info(dictionaries):
	print('Current records\n' \
		  'Name, A1, A2, A3, A4, AVG GR')
	
	for i in dictionaries:
		print(i['Name'] + ', ' + i['A1'] + ', ' + i['A2'] + ', ' + i['A3'] + ', ' + i['A4'] + ', ' + i['AVG GR'])


def read_grades_from_file():
	list_of_dictionaries = []
	name_and_grades_from_file = {}

	with open('grades.csv', 'r') as file:
		reader = csv.DictReader(file)
		for row in reader:
			name_and_grades_from_file = row
			list_of_dictionaries.append(name_and_grades_from_file)
	
	list_file_info(list_of_dictionaries)


def write_grades_to_file(**name_and_grades_dictionary):
	if os.stat('grades.csv').st_size == 0:  # if grades.csv is empty
		with open('grades.csv', 'w', newline='') as file:
			writer = csv.DictWriter(file, name_and_grades_dictionary.keys())
			writer.writeheader()  # write CSV column headers
			writer.writerow(name_and_grades_dictionary)
	else:
		with open('grades.csv', 'a') as file:
			writer = csv.DictWriter(file, name_and_grades_dictionary.keys())
			writer.writerow(name_and_grades_dictionary)


def input_name_and_grades():
	name_and_grades = {}

	try:
		student_name = input('Enter student name:\t\t')
	
		if student_name != '':
			name_and_grades['Name'] = student_name
		else:			
			raise ValueError
	
		counter = 1
		while counter < 5:
			name_and_grades['A' + str(counter)] = float(input('Enter Assignment ' + str(counter) + ' grade:\t'))
			counter += 1				
			
		sum = 0
		for k, v in name_and_grades.items():
			if k == 'Name':
				continue
			else:
				sum += float(v)
	
		name_and_grades['AVG GR'] = sum / (len(name_and_grades) - 1)  # subtract 1 to account for Name index; there's only 4 grades
		print('Average:\t\t\t' + str(name_and_grades['AVG GR']) + '\n')

		write_grades_to_file(**name_and_grades)

		read_grades_from_file()

		user_input = input('\nMore entries? (y or n): ')
		while user_input.lower() != 'y' and user_input.lower() != 'n':  # continue to prompt until y or n
			print('Invalid entry. Please try again.')
			user_input = input('\nMore entries? (y or n): ')
		
		if user_input.lower() == 'n':
			return 'n'
		else:
			return
	except Exception:
		raise Exception


def main():
	file = open('grades.csv', 'w+')  # write and read new CSV file

	while True:
		try:
			print('Grading Application 2\n')
			more_entries = input_name_and_grades()
			if more_entries == 'n':
				break
			else:
				os.system('cls')
		except Exception:
			os.system('cls')
			print('Invalid entry. Please try again.\n')

	file.close()
	print('Bye')


# run main()
main()
# Done!
