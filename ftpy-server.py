import socket

print(f"bind {socket.gethostbyname(socket.gethostname())}")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostbyname(socket.gethostname()),1234))
s.listen(5)
print("listen")
while True:
    clientsock,address = s.accept()
    print(f'connection from {address}')
    clientsock.send(bytes("conn accepted, waiting for instructions","utf-8"))
    command = clientsock.recv(1024).decode('utf-8')
    if command == "clone":
        print("instruction clone")
        path = clientsock.recv(1024).decode('utf-8')
        with open(path,"rb") as f:
            print(f"post {path}")
            clientsock.send(f.read())
            print("finished posting")

    if command == "push":
        print("instruction push")
        filepath = clientsock.recv(1024).decode('utf-8')
        file = clientsock.recv(10000)
        with open(filepath.split("/")[-1],"wb") as f:
            f.write(file)