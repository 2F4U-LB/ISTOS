# Python HTTP server
# TO-DO: Create class, for init, bind, listen.

print("\nInitiating socket...\n")
import socket
try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("\nSocket initiated!\n")
except socket.error as err:
	print(f"\nSocket failure!\n{err}\n")

print("\nBinding socket...\n")
ip="192.168.0.216"
port=80
wait=True
t=10
while wait:
	try:
		s.bind((ip,port))
		print(f"\nSocket binded to {ip}:{port}\n")
		wait=False
	except socket.error as err:
		print(f"\nFailed to bind {ip}:{port}!\n{err}\n")
		import time
		print(f"\nRetrying in {t} seconds\n")
		time.sleep(10)
s.listen(5)
print("\nSocket is listening...\n")
while True:
	try:
		import os
		import sys
		os.chdir("/Users/mikhael/Documents/TIRD-Website-main")
		c,addr=s.accept()
		print(f"\n{addr} has connected.\n")
		r=c.recv(1000).split()[1].decode()
		d=r.strip('/')
		print(f"Requesting:",r)
		if r=='/index.html' or r=='/':
			c.sendall('''HTTP/1.1 200 OK\n'''.encode())
			f=open(os.getcwd()+'/index.html')
			o=f.read()
			f.close()
			print("\nSending:",os.getcwd()+r,"\n")
			c.sendall(o.encode())
		if d[-4:]=='.css':
			f=open(os.getcwd()+'/style.css')
			o=f.read()
			f.close()
			sty='''HTTP/1.1 200 OK
Content-Type: text/css\n
'''+o
			print("\nSending:",os.getcwd()+r,"\n")
			c.sendall(sty.encode())
		if d[-3:]=='.js':
			f=open(os.getcwd()+r)
			o=f.read()
			f.close()
			js='''HTTP/1.1 200 OK
Content-Type: text/javascript\n
'''+o
			print('Sending:', os.getcwd()+r,"\n")
			c.sendall(js.encode())
		else:
			f=open(os.getcwd()+r)
			o=f.read()
			f.close()
			http='''HTTP/1.1 200 OK\n'''+o
			print("Sending:",r,"\n")
			c.sendall(http.encode())
		c.close()
	except socket.error as err:
		print(f"\nCommunication error!\n{err}\n")