from .extract_polling import Telegram
from ..config import api_id, api_hash
from .server import Server
from ..utils import GetDate
import asyncio


srv = Server()
async def RunBOT(always_run: bool = True, save_polling: bool = False):
  if api_id and api_hash is not None:
    await srv.StartServer(api_id, api_hash)
  await asyncio.sleep(3)
  if always_run == True and save_polling == True:
    try:
        print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
        while True:
            await Telegram().ExtractPolling(save_polling=True)
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await srv.StopServer()
  elif always_run == True and save_polling == False:
    try:
        print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
        while True:
            await Telegram().ExtractPolling()
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await srv.StopServer()
  elif always_run == False and save_polling == True:
    try:
        print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
        while True:
            await Telegram().ExtractPolling(save_polling=True)
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        await srv.StopServer()
  elif always_run == False and save_polling == False:
    try:
        print(f"⚙️  Bot Running...\nAlways Run: {always_run}\nSave Polling: {save_polling}\nRunning At: {GetDate()}")
        await Telegram().ExtractPolling()
        await asyncio.sleep(1)
    except KeyboardInterrupt:
        await srv.StopServer()
  else:
      print(f"Please Specify always_run parameter\nIf Set To True BOT Will Receive The Latest Polls Continuously (Real Time) And Send Any Response Method Only Once\nIf Set To False BOT Will Receive Latest Poll Once And Send Any Response Method Only Once Then Bot Will Stop")