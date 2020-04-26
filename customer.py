'''customer.py'''
# pylint: disable=unused-variable, invalid-name, redefined-builtin, too-many-arguments, too-many-instance-attributes
import csv

CUSTOMER_OBJECTS = []

class Customer:
    """
    These Customer instance objects act as encapsulation for specific customer attributes
    """
    def __init__(self, id=0, first_name='', last_name='', company='', address='', city='', \
            state='', zip_code=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.full_address = first_name + " " + last_name
        if company != '':
            self.full_address += "\n" + company
        self.full_address += "\n" + address \
            + "\n" + city + ", " + state + " " + str(zip_code)

    @classmethod
    def get_customers_from_csv(cls):
        """
        read csv file from directory, assign over the list, then append Customer
        objects to global CUSTOMER_OBJECTS
        """
        customer_attributes = []

        with open('customers.csv') as in_file:
            reader = csv.reader(in_file)
            customer_attributes = list(reader)

        customer_attributes.pop(0)  # drop column headers

        for j, item in enumerate(customer_attributes):
            CUSTOMER_OBJECTS.append(Customer(customer_attributes[j][0], customer_attributes[j][1], \
                customer_attributes[j][2], customer_attributes[j][3], customer_attributes[j][4], \
                customer_attributes[j][5], customer_attributes[j][6], customer_attributes[j][7]))

    @classmethod
    def search_for_id(cls, user_input_id):
        """
        fill global CUSTOMER_OBJECTS by calling class method, check each Customer
        object's row id against user's input, either return the objects full address
        or raise a ValueError
        """
        cls.get_customers_from_csv()

        for k, object_item in enumerate(CUSTOMER_OBJECTS):
            if user_input_id == int(CUSTOMER_OBJECTS[k].id):
                return CUSTOMER_OBJECTS[k].full_address

        raise ValueError('\nNo customer with that ID.\n')
