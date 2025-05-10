from ...config import endpoint
from typing import Literal
import json
import aiohttp

class sendMessage:
  def __init__(self) -> None:
    self.raw_data = None
    self.pretty_print = None
    
  async def Initialize(self,
    chat_id: int | str,
    text: int | str,
    parse_mode: Literal["MarkdownV2", "HTML", "Markdown"] = "MarkdownV2",
    disable_notification: bool | None = None,
    protect_content: bool | None = None,
    reply_markup: str | None = None,
    reply_message: int | str | None = None,
  ):
    async with aiohttp.ClientSession() as session:
      payload = {
          'chat_id': chat_id,
          'text': text,
          'parse_mode': parse_mode,
          'disable_notification': disable_notification,
          'protect_content': protect_content,
          'reply_to_message_id': reply_message
      }
      if reply_markup is not None:
          payload['reply_markup'] = reply_markup
      async with session.post(f"{endpoint}/sendMessage", data=payload) as client:
          self.raw_data = await client.json()
          self.pretty_print = json.dumps(self.raw_data, indent=2)
          self.message_id = self.raw_data['result'].get('message_id', '')
          return self