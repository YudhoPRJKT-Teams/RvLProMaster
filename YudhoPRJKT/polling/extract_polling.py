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
          
          # message
          self.message.text = msg_key.get("text", "")
          self.message.message_id = msg_key.get("message_id", "")
          self.message.date = msg_key.get("date", "")
          
          # message.chat
          self.message.chat.id = msg_key["chat"].get("id", "")
          self.message.chat.title = msg_key["chat"].get("title", "")
          self.message.chat.username = f"@{msg_key["chat"].get("username", "")}"
          
          # mmessage.chat.from
          self.message.From.id = msg_key["from"].get("id", "")
          self.message.From.first_name = msg_key["from"].get("first_name", "")
          self.message.From.last_name = msg_key["from"].get("last_name", "")
          self.message.From.username = f"@{msg_key["from"].get("username", "")}"          
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
    