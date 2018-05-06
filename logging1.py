# import logging
# log_format = '%(levelname)s %(asctime)s - %(message)s'
# logging.basicConfig(filename='logging.log',
# 					level=logging.DEBUG,
# 					format = log_format)
# logger = logging.getLogger()
# logger.info('My 1st msg!')
# print(logger.level)

# import logging
# log_format = '%(levelname)s %(asctime)s - %(message)s'
# logging.basicConfig(filename='logging.log',level=logging.DEBUG,format = log_format,filemode='w')
# logger = logging.getLogger()
# logger.info('My 1st msg!')
# print(logger.level)

# import logging
# log_format = '%(levelname)s %(asctime)s - %(message)s'
# logging.basicConfig(filename='one.log',level = logging.DEBUG,format=log_format,filemode='w')
# logger = logging.getLogger()
# logger.info('This is log data')


import logging
log_format = '%(levelname)s %(asctime)s - %(message)s'
logging.basicConfig(level = logging.DEBUG,format=log_format,filemode='w')
logger = logging.getLogger()
logger.info('This is log text')


# pypdf2
# docx
