# 🤖 QR Code Based Robot Control System

![Python](https://img.shields.io/badge/Python-3.10-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green)
![Status](https://img.shields.io/badge/Status-Working-brightgreen)

---

## 📌 Overview
A real-time robot control system using QR codes and computer vision.  
The system detects QR codes via webcam and sends commands to a robot using TCP communication.

---

## 🚀 Features
- 📷 Real-time QR code detection  
- 🤖 Direct robot control (no paid ARC modules)  
- 🌐 TCP socket communication  
- ⚡ Fast and responsive control system  

---

## 🧠 How It Works

QR Code → Camera → Python → TCP → Servo Motors → Robot Movement


---

## 🎯 Commands

| QR Code | Action |
|--------|--------|
| START  | Robot speaks |
| FORWARD | Move forward |
| LEFT   | Turn left |
| RIGHT  | Turn right |
| STOP   | Stop robot |

---

## 🛠️ Tech Stack
- Python  
- OpenCV  
- Socket Programming  
- EZ-Robot  

---

## ⚙️ Installation

```bash
git clone https://github.com/YOUR_USERNAME/QR-Code-Robot-Control.git
cd QR-Code-Robot-Control
pip install -r requirements.txt
python main.py
