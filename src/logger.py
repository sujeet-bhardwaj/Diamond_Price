import logging
import os
from datetime import datetime

# Generate log file name using current timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Path to store the log file
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)  # Create logs directory if it doesn't exist

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Example log messages
logging.info("This is an informational message.")
logging.warning("This is a warning message.")
logging.error("This is an error message.")
