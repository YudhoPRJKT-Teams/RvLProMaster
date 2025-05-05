from typing import Callable, Dict
from functools import wraps

pick_command: Dict[str, Callable] = {}

def BotCommands(command: str):
  
  """Use this decorator to register a command in the bot.

  Args:
      command (str): Your command name. Example: /start, /help, etc.
  """
  def decorator(func):
      @wraps(func)
      async def wrapper():  # message akan dilempar dari polling
          return await func()
      pick_command[command] = wrapper
      return wrapper
  return decorator