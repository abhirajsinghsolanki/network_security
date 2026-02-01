import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """Custom exception class for Network Security module."""

    def __init__(self,error_message,error_detail:sys):
        super().__init__(self,error_message)
        self.error_message = error_message
        _,_,exc_tb = error_detail.exc_info()
        self.file_name = exc_tb.tb_frame.f_code.co_filename
        self.line_number = exc_tb.tb_lineno
    def __str__(self):
        self.full_message = f"Error occurred in file: {self.file_name}, line: {self.line_number} - {self.error_message}"
        return self.full_message
    
if __name__ == "__main__":
    try:
        logger.logging.info("Testing NetworkSecurityException")
        a = 1 / 0
    except Exception as e:
        ne = NetworkSecurityException(e,sys)
        logger.logging.info(ne)
        raise ne
    