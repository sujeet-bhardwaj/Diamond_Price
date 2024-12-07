import sys
import os

# Add the 'src' directory to sys.path
sys.path.append(os.path.join(os.getcwd(), "src"))

# Now import logging from logger module
from logger import logging

def error_message_detail(error, error_detail: sys):
    _, _, exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename

    error_message = f"Error occurred in python script name [{file_name}] line number [{exc_tb.tb_lineno}] error message [{str(error)}]"
    return error_message

class CustomException(Exception):
    
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        return self.error_message  

if __name__ == "__main__":
    logging.info("Logging has started")

    try:
        a = 1 / 0
    except Exception as e:
        logging.info('Division by zero error occurred')
        raise CustomException(e, sys)