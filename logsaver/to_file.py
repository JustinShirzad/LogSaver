import os
import sys
from datetime import datetime

class LogSaver:
    def __init__(self, log_dir = "logs"):
        self.log_dir = log_dir
        self.log_file = self.create_log_file()

    def create_log_file(self):
        relative_path = os.path.join(self.log_dir)

        # Creat directory if it doesn't exist
        os.makedirs(relative_path, exist_ok=True)

        # Get process name
        process_name = os.path.basename(sys.argv[0])
        if process_name.endswith(".py"):
            process_name = process_name[:-3]

        # Create timestamp
        timestamp = datetime.now().strftime("%S%M%H_%d-%m-%Y")

        # Initialise log file
        log_filename = f"{process_name}_{timestamp}.log"
        log_file = os.path.join(relative_path, log_filename)
        with open(log_file, "w") as log:
            log.write(f"|=== START OF LOG FOR: {process_name} ===|\n")
            log.write(f"|=== Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===|\n")

        return log_file
    
    def write_to_log(self, message, level="INFO"):
        # Create timestamp
        timestamp = datetime.now().strftime("%S%M%H_%d-%m-%Y")
    
if __name__ == "__main__":
    logger = LogSaver()