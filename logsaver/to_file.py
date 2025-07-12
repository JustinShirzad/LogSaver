import os
import sys
from datetime import datetime

def create_log_file():
    relative_path = os.path.join("logs")

    # Creat directory if it doesn't exist
    os.makedirs(relative_path, exist_ok=True)

    # Get process name
    process_name = os.path.basename(sys.argv[0])
    if process_name.endswith(".py"):
        process_name = process_name[:-3]

    # Create timestamp
    timestamp = datetime.now().strftime("%S%M%H_%d-%m-%Y")

    # Make log file
    log_filename = f"{process_name}_{timestamp}.log"
    log_file = os.path.join(relative_path, log_filename)
    with open(log_file, "w") as log:
        log.write(f"|=== START OF LOG FOR: {process_name} ON===|\n")
        log.write(f"|=== Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ===|\n")
    
if __name__ == "__main__":
    create_log_file()