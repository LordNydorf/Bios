import socket
import hashlib
import hmac
import base64
import os

with open(r"C:\Users\Rohit\Desktop\Bios\Chat app\key.txt", "rb") as f:
    key = f.read()

s = socket.socket()

host = socket.gethostname()

port = 5555

s.bind((host, port))

s.listen(5)

print("Waiting for incoming connections...")

client, addr = s.accept()
print("Received connection from", addr)

while True:
    message = client.recv(1024).decode()
    if not message:
        break

    hash = hashlib.sha512(message.encode()).hexdigest()
    print("Received message:", message)

    h = hmac.new(key, message.encode(), hashlib.sha256)
    hmac_digest = h.hexdigest()

    encrypted_message = base64.b64encode(message.encode())

    client.send(encrypted_message)

client.close()
