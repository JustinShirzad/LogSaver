import os
import sys
import logging
import inspect
from datetime import datetime 

class LogSaver:
    def __init__(self, log_dir = "logs"):
        self.log_dir = log_dir
        self.log_file, self.process_name = self.create_log_file()
        self.setup_logger()

    def create_log_file(self):
        relative_path = os.path.join(self.log_dir)

        # Creat directory if it doesn't exist
        os.makedirs(relative_path, exist_ok=True)

        # Get process name
        process_name = os.path.basename(sys.argv[0])
        if process_name.endswith(".py"):
            process_name = process_name[:-3]

        # Create timestamp
        timestamp = datetime.now().strftime("%H%M%S_%Y-%m-%d")

        # Initialise log file
        log_filename = f"{process_name}_{timestamp}.log"
        log_file = os.path.join(relative_path, log_filename)
        with open(log_file, "w") as log:
            log.write(f"|=== START OF LOG FOR: {process_name} ===|\n")
            log.write(f"|=== Started: {datetime.now().strftime('%H:%M:%S %d-%m-%Y')} ===|\n")

        return log_file, process_name
    
    def setup_logger(self):
        self.logger = logging.getLogger(self.process_name)
        self.logger.setLevel(logging.DEBUG)
            
        # Create file handler to write to the correct log file
        self.logger.handlers.clear()
        file_handler = logging.FileHandler(self.log_file)
        file_handler.setLevel(logging.DEBUG)
        
        # Format the log messages for the file
        log_formatter = logging.Formatter(
            fmt='[ %(levelname)s ] - %(asctime)s : %(name)s - %(message)s',
            datefmt='%H:%M:%S %d-%m-%Y'
        )
        file_handler.setFormatter(log_formatter)
        
        # Add handler to logger
        self.logger.addHandler(file_handler)

    def create_log(self, log_level, message):
        # Navigate to the frame where the logging method was called
        process_frame = inspect.currentframe().f_back.f_back
        process_lineno = process_frame.f_lineno

        formatted_message = f"Line {process_lineno} : {message}"

        if log_level == "debug":
            self.logger.debug(formatted_message)
        elif log_level == "info":
            self.logger.info(formatted_message)
        elif log_level == "warning":
            self.logger.warning(formatted_message)
        elif log_level == "error":
            self.logger.error(formatted_message)
        elif log_level == "critical":
            self.logger.critical(formatted_message)

        

    # Logging methods (Single letter)
    def D(self, message):
        self.create_log("debug", str(message))

    def I(self, message):
        self.create_log("info", str(message))
    
    def W(self, message):
        self.create_log("warning", str(message))

    def E(self, message):
        self.create_log("error", str(message))

    def C(self, message):
        self.create_log("critical", str(message))

    # Logging methods (Full words)
    def debug(self, message):
        self.create_log("debug", str(message))

    def info(self, message):
        self.create_log("info", str(message))

    def warning(self, message):
        self.create_log("warning", str(message))

    def error(self, message):
        self.create_log("error", str(message))

    def critical(self, message):
        self.create_log("critical", str(message))