from appLogPkg import appLog
from subLog import *


logger = appLog()

logger.info('Main Process starts')
logger.info('Passing 5 and 10 to subLog')
sumUp = subLog(5,10)
logger.info('Response from SubLog is ' + str(sumUp))