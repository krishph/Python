from appLog_package import appLog

class subLog:
    def __init__(self, var1, var2):
        logger = appLog(logDir= "./log", level='DEBUG')
        self.__var1__ = var1
        self.__var2__ = var2
        logger.info('Submodule Var1 is : ' + str(var1))
        logger.info('Submodule Var2 is : ' + str(var2))
    
    def sumUp(self):
        var3 = self.__var1__ + self.__var2__
        logger.info('Submodule Var3 is : ' + str(var3))
        return var3

