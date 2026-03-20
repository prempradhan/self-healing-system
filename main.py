import time
import psutil
import os
from config import PROCESS_NAME, RESTART_COMMAND, CHECK_INTERVAL
from logger import log_event

def is_running(process_name):
    for proc in psutil.process_iter(['name']):
        try:
            if proc.info['name'] == process_name:
                return True
        except:
            pass
    return False

def restart_process():
    log_event("Process not running. Restarting...")
    os.system(RESTART_COMMAND)

def monitor():
    log_event("Starting Self-Healing System...")

    while True:
        if not is_running(PROCESS_NAME):
            restart_process()
        else:
            log_event("Process running normally")

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor()
