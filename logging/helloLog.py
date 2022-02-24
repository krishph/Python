import logging
import  Employee


logging.basicConfig(filename='myLog.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(levelname)s:%(message)s'
                    )

# Debug
# Info
# Warning
# Error
# Critical

logging.info('This is from Main process, this should be in myLog.log')