from MyLogger import *
from subLog import *


logger = MyLogger(logDir= "./log", level='DEBUG')

logger.info('Main Process starts')
logger.info('Passing 5 and 10 to subLog')
sumUp = subLog(5,10)
logger.info('Response from SubLog is ' + str(sumUp))