from ...config import Credentials
from ...utils import CreateLog
import json
import aiohttp

# Get Credentials
credentials = Credentials.GetCredentials()
endpoint = credentials.endpoint


class getMe:
  def __init__(self) -> None:
    self.raw_data = None
    self.pretty_print = None
    
  async def Initialize(self):
    try:
      print(credentials.api_id)
      print(credentials.api_hash)
      print(credentials.token)
      print(credentials.gemini_api_key)
      print(credentials.github_pat)
      print(credentials.nekobin_api)
      async with aiohttp.ClientSession() as session:
        async with session.get(f"{endpoint}/getMe") as client:
          self.raw_data = await client.json()
          self.pretty_print = json.dumps(self.raw_data, indent=2)
          return self
    except (aiohttp.ClientError, aiohttp.ClientResponseError, KeyError) as e:
      CreateLog("ERROR", f"{e}")
      return self