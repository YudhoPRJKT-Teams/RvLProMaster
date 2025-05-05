from YudhoPRJKT import endpoint
import json
import aiohttp

class getMe:
  def __init__(self) -> None:
    self.raw_data = None
    self.pretty_print = None
    
  async def Initialize(self):
    async with aiohttp.ClientSession() as session:
      async with session.get(f"{endpoint}/getMe") as client:
        self.raw_data = await client.json()
        self.pretty_print = json.dumps(self.raw_data, indent=2)
        return self