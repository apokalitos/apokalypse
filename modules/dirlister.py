import os
def run (**args):
	print ("[*] In dirlister module.")
	files = os.listdir(".")
	return str(files).encode_base64
