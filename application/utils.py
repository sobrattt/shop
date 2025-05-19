from datetime import datetime
from application.config import LAST_EXTRACTION_TIME
import os


def update_last_extraction_time():
    time = datetime.now().timestamp()
    file = open(LAST_EXTRACTION_TIME, "w")
    file.write(str(time))
    file.close()

def get_last_extraction_time():
    if os.path.exists(LAST_EXTRACTION_TIME):
        file = open(LAST_EXTRACTION_TIME, "r")
        time = file.read()
        file.close()
        time = datetime.fromtimestamp(float(time))
        return time
    else: return None

