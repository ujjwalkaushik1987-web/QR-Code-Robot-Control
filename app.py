import cv2
import time
from tkinter import *
from PIL import Image, ImageTk
from commands import execute_command

# Window
root = Tk()
root.title("QR Command System PRO")
root.geometry("900x700")

# Camera
cap = cv2.VideoCapture(0)

detector = cv2.QRCodeDetector()

last_data = ""
last_time = 0
running = False

# UI Elements
video_label = Label(root)
video_label.pack()

command_label = Label(root, text="Command: None", font=("Arial", 20))
command_label.pack(pady=10)

# Start Function
def start():
    global running
    running = True
    update_frame()

# Stop Function
def stop():
    global running
    running = False

# Update Camera Frame
def update_frame():
    global last_data, last_time

    if running:
        ret, frame = cap.read()

        if ret:
            data, bbox, _ = detector.detectAndDecode(frame)

            if bbox is not None and data:
                data = data.strip()

                if data != last_data or (time.time() - last_time > 2):
                    execute_command(data)

                    last_data = data
                    last_time = time.time()

                    command_label.config(text=f"Command: {data}")

                # Draw box
                for i in range(len(bbox)):
                    pt1 = tuple(map(int, bbox[i][0]))
                    pt2 = tuple(map(int, bbox[(i+1) % len(bbox)][0]))
                    cv2.line(frame, pt1, pt2, (0,255,0), 2)

            # Convert for Tkinter
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)

            video_label.imgtk = imgtk
            video_label.configure(image=imgtk)

        video_label.after(10, update_frame)

# Buttons
Button(root, text="Start", command=start, width=15, bg="green", fg="white").pack(pady=5)
Button(root, text="Stop", command=stop, width=15, bg="red", fg="white").pack(pady=5)

# Run App
root.mainloop()

cap.release()
cv2.destroyAllWindows()
