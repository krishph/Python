import logging
import os
import datetime


class appLog:
    _logger = None

    def __new__(cls, *args, **kwargs):
        if cls._logger is None:

            logDir=None
            level=None
            if 'logDir' in kwargs.keys():
                logDir = kwargs['logDir']
                del kwargs['logDir']
                print('dirName passed is : ' + logDir)
            else:
                logDir=None
            
            if 'level' in kwargs.keys():
                level = kwargs['level']
                del kwargs['level']
                print('Level passed is : ' + level)
            else:
                logDir=None


            print("Logger new  ")
            cls._logger = super().__new__(cls, *args, **kwargs)
            cls._logger = logging.getLogger("crumbs")

            if level is None:
                cls._logger.setLevel(logging.ERROR) 
            else:
                if level.upper() == 'INFO':
                    cls._logger.setLevel(logging.INFO)
                elif level.upper() == 'DEBUG':
                    cls._logger.setLevel(logging.DEBUG)
                elif level.upper() == 'WARNING':
                    cls._logger.setLevel(logging.WARNING)
                elif level.upper() == 'ERROR':
                    cls._logger.setLevel(logging.ERROR)
                else:
                    cls._logger.setLevel(logging.ERROR)

            formatter = logging.Formatter(
                '%(asctime)s \t [%(levelname)s | %(filename)s:%(lineno)s] > %(message)s')

            now = datetime.datetime.now()
            if logDir != None:
               if not os.path.isdir(logDir):
                   os.mkdir(logDir)
               fileHandler = logging.FileHandler(
                   logDir + "/log_" + now.strftime("%Y-%m-%d")+".log")
               fileHandler.setFormatter(formatter)
               cls._logger.addHandler(fileHandler)

            streamHandler = logging.StreamHandler()
            streamHandler.setFormatter(formatter)
            cls._logger.addHandler(streamHandler)

        return cls._logger


# a simple usecase
if __name__ == "__main__":
    logger = appLog()
    logger.info("Hello, Logger")
    logger = appLog()
    logger.debug("bug occured")