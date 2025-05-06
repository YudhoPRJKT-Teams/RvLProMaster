from .long_poling import LongPolling
from ..bot import Message, ChatJoinRequest
from ..utils import CreateLog
from .save_polling import SavePolling
from ..bot import pick_command, event_pick
import asyncio

class Telegram:
  def __init__(self):
    self.message = Message
    self.chat_join_request = ChatJoinRequest
    
    
  async def ExtractPolling(self, save_polling: bool = False):
    while True:
      try:
        self.out_updates = await LongPolling()
        self.current_event = ''
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
        
        # Request join
        if "chat_join_request" in self.out_updates:
          self.current_event = "chat_join_request"
          req_key = self.out_updates["chat_join_request"]
          
          # chat_join_request
          self.chat_join_request.update_id =  req_key.get("update_id", "")
          self.chat_join_request.date = req_key.get("date", "")
          self.chat_join_request.user_chat_id = req_key.get("user_chat_id", "")
          
          # chat_join_request.chat
          self.chat_join_request.chat.id = req_key["chat"].get("id", "")
          self.chat_join_request.chat.title = req_key["chat"].get("title", "")
          self.chat_join_request.chat.username = f"@{req_key["chat"].get("username", "")}"
          self.chat_join_request.chat.type = req_key["chat"].get("type", "")
          
          # chat_join_request.from
          self.chat_join_request.From.id = req_key["from"].get("id", "")
          self.chat_join_request.From.is_bot = req_key["from"].get("is_bot", "")
          self.chat_join_request.From.first_name = req_key["from"].get("first_name", "")
          self.chat_join_request.From.last_name = req_key["from"].get("last_name", "")
          self.chat_join_request.From.username = f"@{req_key["from"].get("username", "")}"
          self.chat_join_request.From.language_code = req_key["from"].get("language_code", "")
          await self.DispatchEvent()
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
        
  async def DispatchEvent(self):
    if self.current_event == "chat_join_request":
      self.current_event = ""
      if "UserRequest" in event_pick:
        await event_pick["UserRequest"]()
        
        # Reset chat_join_request after completed dispatch
        # await asyncio.sleep(3)
        self.chat_join_request.update_id = "" 
        self.chat_join_request.date = "" 
        self.chat_join_request.user_chat_id = "" 
        
        # chat_join_request.chat
        self.chat_join_request.chat.id = "" 
        self.chat_join_request.chat.title = "" 
        self.chat_join_request.chat.username = "" 
        self.chat_join_request.chat.type = "" 
        
        # chat_join_request.from
        self.chat_join_request.From.id = ""
        self.chat_join_request.From.is_bot = ""
        self.chat_join_request.From.first_name = ""
        self.chat_join_request.From.last_name = ""
        self.chat_join_request.From.username = ""
        self.chat_join_request.From.language_code = ""