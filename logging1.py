#Logging in Python

import logging                                                                  
log_format = '%(levelname)s %(asctime)s - %(message)s'                          
logging.basicConfig(level = logging.DEBUG,
                    format=log_format)
logger = logging.getLogger()                                                    
logger.info('This is log text')                                                 

#This will show you the log at your editor screen or command prompt
'''If you want to get the logs in a new file suppose 'logging.log'
you may use the following code'''

import logging
log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(filename='logging.log',
                    filemode='a'
                    level = logging.DEBUG,
                    format=log_format)
logger = logging.getLogger()
logger.info('This is log text')

# Usage and Running
''' 1. Goto your command prompt or editor you are using
    2.open loggingg1.py file containg folder
    3.use 'python logging1.py'  #without quotations
    4. Try to make changes in files of your directory
    5. Now open your directory and find 'logging.log' which have all your logging details
'''
