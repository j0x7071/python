import socket

hostname=socket.gethostname()

print("nombre",hostname)

ip = socket.gethostbyname(hostname)

print(ip)