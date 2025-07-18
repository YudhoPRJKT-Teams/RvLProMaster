from ..utils import CreateLog
import os
import json
import sys
import subprocess


def SavePolling(out_updates: str):
  try:
    """save polling data to a file"""
    current_dir = os.getcwd()
    full_path = f"event.json"
    pretty_print = str(json.dumps(out_updates, indent=2))
    print(f"Saving polling data to {current_dir}")
    print(full_path)
    if not os.path.exists(full_path):
      with open(full_path, "w") as f:
        f.write(pretty_print)
    else:
      with open(full_path, "w") as f:
        f.write(pretty_print)
  except Exception as e:
    CreateLog("ERROR", f"An error occurred while saving polling data: {e}")
    sys.exit(1)