# 🛡️ System Monitoring & Keylogging Tool (For Ethical Use)

A Python-based surveillance tool designed for **ethical hacking**, **cybersecurity research**, and **digital forensics**. This tool performs system reconnaissance, keylogging, clipboard and screenshot capture, and securely transmits data via email. It also supports secure AES encryption and decryption of log files for later analysis.

---

## 🚀 Features

- ⌨️ **Keylogging**  
  Captures and timestamps user keystrokes using `pynput`.

- 🖥️ **System Information Collection**  
  Gathers system details including OS, processor, and machine info using `platform`.

- 📋 **Clipboard Data Capture**  
  Extracts current clipboard contents via `win32clipboard`.

- 📸 **Screenshot Capture**  
  Takes full-screen screenshots using `Pillow (PIL)`.

- 🔐 **AES Encryption & Decryption**  
  Encrypts logs using `cryptography.Fernet` for secure transmission.

- 🧩 **Decryption Script**  
  Includes `decryptfile.py` to securely decrypt previously encrypted log files.

- 📧 **Email Reporting**  
  Automatically sends encrypted logs and screenshots to a specified email using `smtplib`.

---

## 📂 File Structure

| File / Folder           | Description                                           |
|-------------------------|-------------------------------------------------------|
| `keylogger.py`          | Main script for logging keys and capturing system data |
| `decryptfile.py`        | Script for decrypting AES-encrypted log files         |
| `encryption.key`        | Generated AES encryption key used by Fernet           |
| `e_log.txt`             | Encrypted keystroke log                               |
| `e_sysinfo.text`        | Encrypted system info                                 |
| `e_clipboard.txt`       | Encrypted clipboard content                           |
| `de_log.txt`            | Decrypted keystroke log (output)                      |
| `screenshot.png`        | Captured screenshot                                   |

---

## 🛠️ Requirements

Install the required packages with:

```bash
pip install pynput cryptography Pillow scipy sounddevice pywin32
