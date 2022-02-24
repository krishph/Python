from myPkg.myLog import appLog
import re

logger = appLog(level='debug')
logger.info('this is regex starting')

text_to_Search = '''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
    abc
Ha HaHa

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
https://facebook.com
http://www.udemy.com

Metacharacters (Need to be escaped):

. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
132.345.5678

Mr.  Schafer
Mr Smith
Mr Davis
Mrs. Robinson
Mr. Tango
'''

sentence = 'start a sentence and then bring it to an end'

logger.info(r'\tTab, notice that tab')
logger.info('\tTab, notice that tab')

patter = re.compile(r'abc')
matches = patter.finditer(text_to_Search)
logger.info('type of matches is ' + str(type(matches)))
# logger.info('Length of matches is : ' + str(len(matches)))
for match in matches:
    logger.info(match)

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(text_to_Search)
logger.info('Extract only the websites')
# logger.info('Length of matches is : ' + str(len(matches)))
for match in matches:
    logger.info(match)
    logger.info(str(match))

pattern = re.compile(r'\bHa\b')
matches = pattern.finditer(text_to_Search)
logger.info('Extract only the websites')
# logger.info('Length of matches is : ' + str(len(matches)))
for match in matches:
    logger.info(match)