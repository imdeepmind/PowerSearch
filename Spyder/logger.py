import logging

# Setting a logger
logger = logging.getLogger(__name__)

# Setting the log level
logger.setLevel(logging.DEBUG)

# Setting the log message format
formatter = logging.Formatter("%(levelname)s : %(asctime)s : %(filename)s : %(message)s")

# Setting file handler for the log
file_handler = logging.FileHandler("logging.log")
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

# Setting stream handler for the log
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

# Adding the two handlers for the logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)