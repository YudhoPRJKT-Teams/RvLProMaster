from ...utils import CreateLog
from ...config import endpoint
from json import dumps
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError, ClientError

class editMessageMedia:
  def __init__(self) -> None:
    pass
  
  async def Initialize(self,
    chat_id: int | str,
    message_id: int | str,
    media: str,
    reply_markup: str | None = None,
  ):
    try:
      payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "media": media,
      }
      if reply_markup is not None:
        payload["reply_markup"] = reply_markup  
      async with ClientSession() as session:
        async with session.post(f"{endpoint}/editMessageMedia", data=payload) as client:
          self.raw_data = await client.json()
          self.pretty_print = dumps(self.raw_data, indent=2)
        return self
    except (ClientError, ClientResponseError) as e:
      CreateLog("ERROR", str(e))
      return self