from typing import Any

class exceptions:
  class TEXT_ESCAPED(Exception):
    def __init__(self, message: Any, status_code: int):
      self.message = message
      self.status_code = status_code
      super().__init__(message)
    
    def __str__(self) -> str:
      return f"RvLProMasted Says\n{self.status_code} {self.message}"