import os
def run(**args):
  command_output = "[*] In environ module:\n\n"
  return command_output + str(os.environ) + "\n\n"
