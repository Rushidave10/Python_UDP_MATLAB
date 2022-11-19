import socket


host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
local_port = 12345
buffer_size = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg = bytes("Hello! from the other side", "utf-8")

s.sendto(msg, (ip_address, local_port))

while True:
    msg_from_server = s.recvfrom(buffer_size)
    data_server = msg_from_server[0]
    ip_address_server = msg_from_server[1]

    print(data_server.decode('utf-8'))

