import socket


host_name = socket.gethostname()
print(host_name)
ip_address = socket.gethostbyname(host_name)
print(ip_address)
local_port = 12345
buffer_size = 1024

#  Message to be sent encode in utf-8 standard.
msg = bytes("Welcome to my Server!", "utf-8")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((ip_address, local_port))

print("Server is up and listening!")

while True:
    recv_msg = s.recvfrom(buffer_size)
    data = recv_msg[0]
    ip_address_client = recv_msg[1]

    print(data.decode('utf-8'))
    print(ip_address_client)
    s.sendto(msg, ip_address_client)
