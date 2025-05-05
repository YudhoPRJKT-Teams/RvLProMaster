from .long_poling import LongPolling
from ..bot import Message
from ..utils import CreateLog
from .save_polling import SavePolling
from ..bot import pick_command


class Telegram:
  def __init__(self):
    self.message = Message
    
    
  async def ExtractPolling(self, save_polling: bool = False):
    while True:
      try:
        self.out_updates = await LongPolling()
        
        # Message
        if "message" in self.out_updates:
          msg_key = self.out_updates["message"]
          
          self.message.text = msg_key.get("text", "")
          self.message.chat.id = msg_key["chat"].get("id", "")
          
          await self.DispatchCommand()
        if save_polling == True:
          SavePolling(self.out_updates)
        elif save_polling == False:
          pass
        return self
      except KeyError as poll_key_error:
        CreateLog("ERROR", f"Polling Error: {poll_key_error}")
        
  async def DispatchCommand(self):
    message = self.message
    if message.text:
      command = message.text.split()[0]
      if command in pick_command:
        await pick_command[command]()
    