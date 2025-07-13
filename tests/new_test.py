from logsaver import LogSaver
from logsaver.temp_process import dummy_process
from multiprocessing import Process

# LOGS = LogSaver()


if __name__ == "__main__":

    a = Process(target=dummy_process, args=(1,))
    b = Process(target=dummy_process, args=(2,))
    
    a.start()
    b.start()
    
    a.join()
    b.join()
    
    print("All processes completed.")