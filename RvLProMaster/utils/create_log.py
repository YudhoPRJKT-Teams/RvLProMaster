from typing import Literal
from datetime import datetime
import os
import inspect

def CreateLog(
    level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
    message: str
):
    try:
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
        formatted_time = now.strftime('%d-%B-%Y %I:%M:%S %p')
        call_frame = inspect.stack()[1]
        get_running_file = os.path.basename(call_frame.filename).replace('.py', '')
        log_pattern = f"{day_name} {formatted_time} {level} {get_running_file} - {message}"
        print(log_pattern)
        
        if os.path.exists("bot.log"):
            with open("bot.log", "a") as f:
                f.write(f"\n{log_pattern}")
    except FileNotFoundError:
        with open("bot.log", "a") as f:
            f.write(f"\n{log_pattern}")
        os.chmod("bot.log", 0o777) # Ensure the log file is fully accessible
    # if not os.path.exists("bot.log"):
    #     os.chmod("bot.log", 0o777)  # Ensure the log file is fully accessible
    #     with open("bot.log", "a") as f:
    #         f.write(f"\n{log_pattern}")
    # else:
    #     with open("bot.log", "a") as f:
    #         f.write(f"\n{log_pattern}")