import socket
import threading

def client_handler(conn, addr):
    while True:
        msg = conn.recv(1024)
        # decode to get text
        msg = msg.decode('utf-8')
        print(f"Message sent by client {addr}: {msg}")
        if msg == "exit":
            break

def main():
    server_sock = socket.socket() # networked communication is done over sockets
    # bind the server socket to your IP address
    # clients can input the same IP address on their side to connect
    server_sock.bind(('localhost', 16000))
    server_sock.listen() # listen for connection requests
    
    while True:
        try:
            conn, addr = server_sock.accept() # accept new connections if a client wants to connect
            print("new client:", addr)
            # threading allows multiple things to run at once
            # in this case, threading will let multiple clients connect to this one server
            t = threading.Thread(target=client_handler, args=(conn, addr))
            t.start()
        except:
            server_sock.close()

main()