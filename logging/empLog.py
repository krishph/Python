import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')

file_handler = logging.FileHandler('appLog.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Debug
# Info
# Warning
# Error
# Critical


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

        logger.info(
            'Employee Created : {} - {}'.format(self.firstname, self.lastname))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.firstname, self.lastname)

    @property
    def fullName(self):
        return '{} {}'.format(self.firstname, self.lastname)


if __name__ == '__main__':
    emp1 = Employee('John', 'Smith')
    emp2 = Employee('Tom', 'Anderson')

emp1 = Employee('John', 'Smith')
emp2 = Employee('Tom', 'Anderson')
