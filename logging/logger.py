import logging


class logger:

    def __init__(self):

        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)
        formatter = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'

        file_handler = logging.FileHandler('appLog.log')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)
