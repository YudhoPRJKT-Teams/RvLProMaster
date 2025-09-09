from ..utils import CreateLog


class credentials:
  def __init__(self) -> None:
    self.api_id = None
    self.api_hash = None
    self.token = None
    self.gemini_api_key = ""
    self.github_pat = ""
    self.nekobin_api = ""
    self.endpoint = f"http://127.0.0.1:8080/bot{self.token}"


  # Set Credentials
  def SetCredentials(self, api_id: int, api_hash: str, token: str, gemini_api_key: str | None = "", github_pat: str | None = "", nekobin_api: str | None = "") -> object:
    """The Functions to Set Credentials

    Args:
        api_id (int): Your api_id above account, obtained from https://my.telegram.org
        api_hash (str): Your api_hash above account, obtained from https://my.telegram.org
        token (str): Your bot token, obtained from https://t.me/botfather
        gemini_api_key (str | None): Your Gemini API key, obtained from https://gemini.com
        github_pat (str | None): Your GitHub PAT, obtained from github personal access token
        nekobin_api (str | None): Your Nekobin API key
    """
    if (api_id is None or api_hash is None or token is None):
      try:
        self.gemini_api_key = ""
        self.github_pat = ""
        CreateLog("ERROR", "Please set your credentials first.")
        raise ValueError("Please set your credentials first.")
      except ValueError:
        pass
      return self
    if (api_id is not None and api_hash is not None and token is not None):
      self.api_id = api_id
      self.api_hash = api_hash
      self.token = token
      self.gemini_api_key = gemini_api_key
      self.github_pat = github_pat
      self.nekobin_api = nekobin_api
    return self
  
  def GetCredentials(self):
    return self
  
Credentials = credentials()