import socket
import hashlib
import hmac
import base64

with open(r"C:\Users\Rohit\Desktop\Bios\Chat app\key.txt", "rb") as f:
    key = f.read()

s = socket.socket()

host = socket.gethostname()

port = 5555

s.connect((host, port))

while True:
    message = input("Enter a message: ")
    s.send(message.encode())

    encrypted_message = s.recv(1024)

    message = base64.b64decode(encrypted_message).decode()
    print("Decrypted message:", message)

    hash = hashlib.sha512(message.encode()).hexdigest()

    h = hmac.new(key, message.encode(), hashlib.sha256)
    hmac_digest = h.hexdigest()
