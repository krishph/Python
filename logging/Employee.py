import logging


logging.basicConfig(filename='employee.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'
                    )

# Debug
# Info
# Warning
# Error
# Critical

class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        logging.info('Employee Created : {} - {}'.format(self.firstname, self.lastname))
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstname, self.lastname)
    
    @property
    def fullName(self):
        return '{} {}'.format(self.firstname, self.lastname)
    

if __name__ == '__main__':
    emp1 = Employee('John', 'Smith')
    emp2 = Employee('Tom', 'Anderson')
