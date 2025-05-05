from typing import Literal
from .Updates import getUpdates
from .Methods import (
  getMe
)
from .bot_command import BotCommands


class Bot:
  def __init__(self):
    self.Updates = self._Updates()
    self.Methods = self._Methods()
  
  # Updates
  class _Updates:
    def __init__(self):
      pass
    
    # updates: getUpdates
    async def getUpdates(self, offset: None):
      """Use this method to receive incoming updates using long polling (wiki). Returns an Array of Update objects.
  
      Args:
          offset (int): Identifier of the first update to be returned. Must be greater by one than the highest among the identifiers of previously received updates. By default, updates starting with the earliest unconfirmed update are returned. An update is considered confirmed as soon as getUpdates is called with an offset higher than its update_id. The negative offset can be specified to retrieve updates starting from -offset update from the end of the updates queue. All previous updates will be forgotten.
      """
      return await getUpdates().Initialize(offset)
    
  # Methods
  class _Methods:
    def __init__(self):
      pass
    
    # methods: getMe
    async def getMe(self):
      """Use this method to get information about the bot. Returns a User object on success."""
      return await getMe().Initialize()
  
  # Bot Commands
  def command(self, command: str):
    return BotCommands(command)
bot = Bot()