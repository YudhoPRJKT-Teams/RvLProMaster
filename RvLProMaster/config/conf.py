from dotenv import load_dotenv
from ..utils import CreateLog
import os
import glob
import sys
import time


class Configs:
    def __init__(self) -> None:
        # Try to find existing .env file
        env_path = self.findEnv()
        if env_path is not None:
            self.basedir = env_path
            self.load_env()  # Load environment variables if .env exists
        else:
            self.ClearScreen()
            CreateLog("ERROR", "Unable to find authentication file")
            time.sleep(2)
            CreateLog("INFO", "Creating authentication file")
            self.basedir = f"{os.getcwd()}/.env"
            with open(self.basedir, "w"):
                CreateLog("INFO", "Authentication file created")
            self.CreateAuth()  # Prompt user to create config
            self.load_env()    # Load new environment variables
    
    # clear screen
    def ClearScreen(self):
      if sys.platform == "linux":
        os.system("clear")
      elif sys.platform == "darwin":
        os.system("clear")
      elif sys.platform == "win32":
        os.system("cls")
      else:
        CreateLog("ERROR", "Unsupported OS, Unable To Clear Screen")

    def load_env(self):
        """ Loads environment variables from .env file """
        load_dotenv(self.basedir, override=True)

        self.endpoint = os.getenv("endpoint")
        self.token = os.getenv("token")
        self.gemini_api_key = os.getenv("gemini_api_key")
        self.github_pat = os.getenv("github_pat")
        self.nekobin_api = os.getenv("nekobin_api")
        self.api_id = os.getenv("api_id")
        self.api_hash = os.getenv("api_hash")


    def findEnv(self, dir="."):
        for find_env in glob.iglob(f"{dir}/**/.env", recursive=True):
            result = os.path.abspath(find_env)
            return result
        return None

    def CreateAuth(self):
      try:
        input_token = str(input('Input Your Telegram BOT Token: '))
        input_api_id = str(input('Input Your Telegram API ID: '))
        input_api_hash = str(input('Input Your Telegram API Hash: '))
        server_endpoint = f"http://127.0.0.1:8080/bot{input_token}"
        if input_token and input_api_id and input_api_hash and server_endpoint == "":
            CreateLog("ERROR", "Please Provide All Required Fields")
        with open(self.basedir, "w") as f:
            f.write(f'token = "{input_token}"\nendpoint = "{server_endpoint}"\napi_id = "{input_api_id}"\napi_hash = "{input_api_hash}"\ngemini_api_key = "" # Please Change If You Have\ngithub_pat = "" # Please Change If You Have\nnekobin_api = "" # Please Change If You Have')
            CreateLog("INFO", "Configuration Saved!")
      except KeyboardInterrupt:
        CreateLog("INFO", "Authentication process interrupted by user")
        sys.exit(1)
# Initialize Config
Config = Configs()

# Pull out loaded environment values
endpoint = Config.endpoint
token = Config.token
gemini_api_key = Config.gemini_api_key
github_pat = Config.github_pat
nekobin_api = Config.nekobin_api
api_id = Config.api_id
api_hash = Config.api_hash