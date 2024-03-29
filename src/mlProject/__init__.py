import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = "logs" #creating log folder
log_filepath = os.path.join(log_dir,"running_logs.log") #inside log create folder running log
os.makedirs(log_dir, exist_ok=True)


logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #it will save all the logging
        logging.StreamHandler(sys.stdout) #it will print my log in the terminal
    ]
)

logger = logging.getLogger("mlProjectLogger")