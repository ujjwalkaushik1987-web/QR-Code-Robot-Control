import socket
import time

HOST = "192.168.137.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("Connected")

# MOVE FORWARD
client.sendall(b"Servo(D0, 0)\r\n")
client.sendall(b"Servo(D1, 180)\r\n")

time.sleep(3)

# STOP
client.sendall(b"Servo(D0, 90)\r\n")
client.sendall(b"Servo(D1, 90)\r\n")

client.close()
