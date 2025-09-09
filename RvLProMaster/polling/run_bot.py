from .extract_polling import Telegram
from ..config import Credentials
from .server import Server
from ..utils import GetDate, CreateLog
from aiohttp.client_exceptions import ClientConnectorError
import asyncio

# Get Credentials
credentials = Credentials.GetCredentials()
api_id = str(credentials.api_id)
api_hash = str(credentials.api_hash)

srv = Server()
async def RunBOT(always_run: bool = True, save_polling: bool = False):
  try:
    await srv.StartServer(api_id, api_hash)
    if always_run == True and save_polling == True:
      try:
          print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
          while True:
              await Telegram().ExtractPolling(save_polling=True)
              await asyncio.sleep(1)
      except KeyboardInterrupt:
          srv.StopServer()

    elif always_run == True and save_polling == False:
      try:
          print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
          while True:
              await Telegram().ExtractPolling()
              await asyncio.sleep(1)
      except KeyboardInterrupt:
          srv.StopServer()

    elif always_run == False and save_polling == True:
      try:
          print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
          while True:
              await Telegram().ExtractPolling(save_polling=True)
              await asyncio.sleep(1)
      except KeyboardInterrupt:
          srv.StopServer()

    elif always_run == False and save_polling == False:
      try:
          print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
          await Telegram().ExtractPolling()
          await asyncio.sleep(1)
      except KeyboardInterrupt:
          srv.StopServer()

    else:
        print(f"Please Specify always_run parameter\nIf Set To True BOT Will Receive The Latest Polls Continuously (Real Time) And Send Any Response Method Only Once\nIf Set To False BOT Will Receive Latest Poll Once And Send Any Response Method Only Once Then Bot Will Stop")
  except ClientConnectorError:
    CreateLog("ERROR", "Detected Error! Killing Server")
    srv.killServer()
    await asyncio.sleep(2)
    CreateLog("INFO", "Restarting Server...")
    await srv.StartServer(api_id, api_hash)