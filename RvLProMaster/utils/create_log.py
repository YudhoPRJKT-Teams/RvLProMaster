from typing import Literal
from datetime import datetime
import os
import inspect

def CreateLog(
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    message: str
):
    """The Utility function for creating logs.

    Args:
        level : Log Level
            - DEBUG: Debugging information
            - INFO: General information
            - WARNING: Warning messages
            - ERROR: Error messages
            - CRITICAL: Critical error messages
        message (str): Your Message Wants to display into log
    """
    now = datetime.now()
    day_name = now.strftime('%A')  # nama hari
    formatted_time = now.strftime('%d-%B-%Y, %I:%M:%S %p')  # tanggal-bulan-tahun dan jam AM/PM
    call_frame = inspect.stack()[1]
    get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
    print(f"[{day_name} {formatted_time}] [{get_running_file}] [{level}] {message}")