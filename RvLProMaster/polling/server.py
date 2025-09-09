from aiohttp import ClientSession, ClientError
from ..utils import CreateLog
from ..config import Credentials
from aiohttp.client_exceptions import ClientConnectorError
import aiofiles
import os
import sys
import tempfile
import subprocess
import asyncio
import signal

# Get Credentials
credentials = Credentials.GetCredentials()
api_id = credentials.api_id
api_hash = credentials.api_hash

class Server:
  def __init__(self) -> None:
    self.proc = None
    self.temp_dir = None
    self.cmd = None
    self.current_dir = os.getcwd()
    self.download_path = f"{self.current_dir}/RvLProMaster/polling/telegram-bot-api"


  # Download Server
  async def DownloadServer(self) -> None:
    try:
      if os.path.exists(self.download_path):
        CreateLog("INFO", "Server already exists, skipping download.")
      else:
        CreateLog("INFO", "Downloading Server Please Wait!")
        async with ClientSession() as session:
          async with session.get("https://github.com/YudhoPRJKT-Teams/telegram-bot-api/releases/download/linux/telegram-bot-api") as client:
            client.raise_for_status()
            if client.status == 200:
              async with aiofiles.open(self.download_path, "wb") as stream:
                srv_read = await client.read()
                await stream.write(srv_read)
                os.chmod(self.download_path, 0o755)
                CreateLog("INFO", "Downloaded Server successfully.")
            else:
              CreateLog("ERROR", f"Failed to download Server. Status code: {client.status}")
              sys.exit(1)
    except ClientError as e:
      CreateLog("ERROR", f"An error occurred while downloading Server: {e}")
      sys.exit(1) 
  
  # Create Temporary Directory  
  async def CreateTempFile(self) -> None:
    self.temp_dir = f"{tempfile.gettempdir()}/tg-files"

    try:
      os.makedirs(self.temp_dir, exist_ok=True)
      CreateLog("INFO", f"Temporary directory created at {self.temp_dir}")
    except Exception as e:
      CreateLog("ERROR", f"An error occurred while creating temporary directory: {e}")
      sys.exit(1)
    
  # Kill Server and check
  def killServer(self):
    try:
      r = subprocess.check_output(["ps", "aux"], text=True)
      l = r.splitlines()
      k = []
      for line in l:
        if "telegram-bot-api" in line and "grep" not in line:
          p = line.split()
          found_pid = int(p[1])
          os.kill(found_pid, signal.SIGKILL)
          k.append(found_pid)
        if k:
          CreateLog("INFO", f"Killed Server With PID: {k}")
    except Exception as e:
      CreateLog("ERROR", str(e))
  # Start Server
  async def StartServer(self, api_id: str, api_hash: str) -> None:
    """The Function To Start The Server

    Args:
        api_id (str): The API ID for the Telegram bot
        api_hash (str): The API hash for the Telegram bot
    """
    try:
      await self.DownloadServer()
      self.killServer()
      await asyncio.sleep(3)
      if api_id and api_hash is not None:
        await self.CreateTempFile()
        if self.temp_dir is not None:
          if os.path.exists(self.temp_dir):
            CreateLog("INFO", "Starting Server!")
            # Linux
            if sys.platform == "linux":
              cmds = [
                self.download_path,
                f"--api-id={api_id}",
                f"--api-hash={api_hash}",
                "--http-port=8080",
                f"--dir={self.temp_dir}",
                f"--temp-dir={self.temp_dir}"
              ]
            # MacOS
            elif sys.platform == "darwin":
              cmds = [
                self.download_path,
                f"--api-id={api_id}",
                f"--api-hash={api_hash}",
                "--http-port=80",
                f"--dir={self.temp_dir}",
                f"--temp-dir={self.temp_dir}"
              ]
            self.cmd = ' '.join(cmds)
            self.proc = subprocess.Popen(
              self.cmd,
              shell=True,
              stderr=subprocess.PIPE,
              stdout=subprocess.PIPE,
              start_new_session=True
            )
            await asyncio.sleep(3)
          else:
            CreateLog("ERROR", "Temporary directory does not exist.")
            sys.exit(1)
        else:
          CreateLog("ERROR", "API ID and API Hash must be provided.")
          sys.exit(1)
    except Exception as e:
      CreateLog("ERROR", f"An error occurred while starting the server: {e}")
      self.StopServer()
    except KeyboardInterrupt:
      self.killServer()
  # Stop Server
  def StopServer(self) -> None:
    CreateLog("INFO", "Stopping Server!")
    self.killServer()