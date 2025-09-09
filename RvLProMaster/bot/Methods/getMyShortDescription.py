from ...config import Credentials
from ...utils import CreateLog
from aiohttp import ClientSession
from aiohttp.client_exceptions import ClientResponseError, ClientError
from json import dumps

# Get Credentials
credentials = Credentials.GetCredentials()
endpoint = credentials.endpoint

class getMyShortDescription:
  def __init__(self) -> None:
    self.raw_data = None
    self.pretty_print = None
    self.short_description = None
    
  async def Initialize(self):
    try:
      async with ClientSession() as session:
        async with session.post(f"{endpoint}/getMyShortDescription") as client:
          self.raw_data = await client.json()
          self.pretty_print = dumps(self.raw_data, indent=2)
          if self.raw_data.get("ok") is True:
            self.short_description = self.raw_data['result'].get("short_description")
        return self
    except (ClientError, ClientResponseError) as e:
      CreateLog("ERROR", str(e))
      return self
          