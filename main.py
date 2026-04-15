import cv2
import socket
import time

# =========================
# CONNECTION SETUP
# =========================
HOST = "192.168.137.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

print("✅ Connected to EZ-Robot")

# =========================
# SEND FUNCTION (FIXED)
# =========================
def send(cmd):
    print("📤 Sending:", cmd)
    client.sendall((cmd + "\r\n").encode())

# =========================
# STOP FUNCTION
# =========================
def stop():
    send("Servo(D0,90)")
    send("Servo(D1,90)")

# =========================
# COMMAND MAPPING (FINAL)
# =========================
def map_command(data):
    print("🎯 Executing:", data)

    if data == "START":
        send("SayEZB('Started')")

    elif data == "FORWARD":
        send("Servo(D0,0)")
        send("Servo(D1,180)")

    elif data == "LEFT":
        send("Servo(D0,0)")
        send("Servo(D1,90)")

    elif data == "RIGHT":
        send("Servo(D0,90)")
        send("Servo(D1,180)")

    elif data == "STOP":
        stop()

    else:
        print("❓ Unknown command:", data)

# =========================
# CAMERA + QR SETUP
# =========================
detector = cv2.QRCodeDetector()
cap = cv2.VideoCapture(0)

# =========================
# MAIN LOOP (STABLE)
# =========================
last_time = 0
cooldown = 1   # seconds

print("📷 QR Scanner Started (Press Q to exit)")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        data = data.strip().upper()

        current_time = time.time()

        if current_time - last_time > cooldown:
            print("🔍 Detected:", data)
            map_command(data)
            last_time = current_time

    cv2.imshow("QR Robot Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# =========================
# CLEANUP
# =========================
stop()
cap.release()
client.close()
cv2.destroyAllWindows()
