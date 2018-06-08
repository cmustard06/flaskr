#!/usr/bin/env python
# __Author__:cmustard

import socket


sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	sock.bind(("0.0.0.0",8000))
	sock.listen(5)
	while True:
		try:
			client,sddress = sock.accept()
			data = client.recv(4096)
			print(data.decode("utf-8"))
			client.send(b"HTTP/1.1 200 OK\r\n")
			client.close()
		except socket.timeout:
			continue
except KeyboardInterrupt as e:
	sock.close()

except Exception as e:
	print(e)
	sock.close()

