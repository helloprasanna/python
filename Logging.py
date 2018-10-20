
# coding: utf-8

# In[8]:


import logging

# numeric_level = getattr(logging, loglevel.upper(), None)
# print(numeric_level)
logging.basicConfig(filename="example.log",
                    level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    filemode='w')
log = logging.getLogger()
clog = logging.getLogger()


# In[9]:


clog.setLevel(logging.ERROR)
log.setLevel(logging.DEBUG)
log.warning('-'*20 + 'Starting Log')
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('Arguments: %s & %s','first str',"second str")
# modular approach
log.info('Arguments: %s & %s','first str',"second str") 
clog.info('Arguments: %s & %s','first str',"second str") # wont be displayed
clog.error('This is error')


# In[1]:


import logging

# Console logger
# create logger
logger = logging.getLogger('simple_example')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')

