import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("127.0.0.1", 8888))
sock.listen(5)

while True:
    try:
        client, addr = sock.accept()
        print(f"client: {client}")
        print(f"addr: {addr}")
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        result = client.recv(1024)
        client.close()
        print("Some message: ", result.decode("utf-8"))
