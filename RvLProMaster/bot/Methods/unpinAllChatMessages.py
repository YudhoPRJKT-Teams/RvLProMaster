from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientError, ClientResponseError
from ...config import Credentials
from json import dumps
from ...utils import CreateLog

# Get Credentials
credentials = Credentials.GetCredentials()
endpoint = credentials.endpoint


class unpinAllChatMessages:
  def __init__(self) -> None:
    self.raw_data = None
    self.pretty_print = None
    
  async def Initialize(self, chat_id: int | str):
    try:
      payload = {
        "chat_id": chat_id
      }
      async with ClientSession() as session:
        async with session.post(f"{endpoint}/unpinAllChatMessages", data=payload) as response:
          self.raw_data = await response.json()
          self.pretty_print = dumps(self.raw_data, indent=2)
          return self
    except (ClientError, ClientResponseError) as e:
      CreateLog("ERROR", f"{e}")
      return self