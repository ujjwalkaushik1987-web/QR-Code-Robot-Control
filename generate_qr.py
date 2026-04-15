import qrcode

commands = [
    "START",
    "STOP",
    "LEFT",
    "RIGHT",
    "FORWARD",
    "BACKWARD",
    "SPEED UP",
    "SLOW DOWN",
    "LIGHT ON",
    "LIGHT OFF",
    "FAN ON",
    "FAN OFF"
]

for cmd in commands:
    img = qrcode.make(cmd)
    img.save(f"{cmd}.png")

print("✅ All QR Codes Generated Successfully!")
