from typer import Typer
import socket

app = Typer()

@app.command()
def clone(host:str,port:int=1234,path:str="null"):
    if path == "null":
        print("Please enter a Path")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    msg = s.recv(5000)
    s.send("clone".encode('utf-8'))
    print(f"cloning into {path.split('/')[-1]}")
    s.send(path.encode('utf-8'))
    file = s.recv(5000)
    with open(path.split("/")[-1],"wb") as f:
        f.write(file)

    print("Received information. Code:0")
    

@app.command()
def push(host:str,port:int=1234,path:str="null"):
    if path == "null":
        print("Please enter a Path")
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host,port))

    msg = s.recv(5000)
    s.send("push".encode('utf-8'))
    print(f"pushing {path.split('/')[-1]} to server...")
    s.send(path.encode('utf-8'))
    s.send(open(path).read().encode('utf-8'))

    print("Received information. Code:0")

app()