import os
def run(**args):
  command_output = "[*] In dirlister module:\n\n"
  return command_output + str(os.listdir(".")) + "\n\n"
