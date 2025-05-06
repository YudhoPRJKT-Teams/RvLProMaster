import subprocess


class _Terminal:
  def __init__(self):
    self.output_terminal = ''
  
  
  def Bash(self, command: str):
    """
    Run a bash command and return the output.
    """
    pr = subprocess.run(
      command,
      shell=True,
      check=True,
      text=True,
      capture_output=True,
    )
    
    self.output_terminal = pr.stdout
    if pr.stderr:
      self.output_terminal = pr.stderr
    return self
  
Terminal = _Terminal()
