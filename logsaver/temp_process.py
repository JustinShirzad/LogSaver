
from logsaver.file_logger import LogSaver

def dummy_process(i):
    logs = LogSaver(id=i)

    logs.debug(f"Starting process ID : {i}")
    for b in range (5) :
        logs.info(b)
        logs.critical("HELLO")