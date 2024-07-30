import socket

soc = socket.socket()
# replace the IP address and port number below with
# your server's IP address and port
soc.connect(('10.130.68.37', 16080))
print("Connection established")

while True:
    msg = input("Enter msg: ")
    # must encode text before sending
    soc.send(msg.encode('utf-8'))
    if msg == "exit":
        soc.close()
        break
