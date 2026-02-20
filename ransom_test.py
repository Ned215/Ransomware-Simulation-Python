from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print(" Done: Key generated and saved to secret.key")

def encrypt_files(folder_path):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted_data = fernet.encrypt(data)
            with open(file_path, "wb") as f:
                f.write(encrypted_data)
            print(f" Encrypted: {file}")

def decrypt_files(folder_path):
    with open("secret.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    for file in os.listdir(folder_path):
        if file.endswith(".txt"):
            file_path = os.path.join(folder_path, file)
            with open(file_path, "rb") as f:
                data = f.read()
            decrypted_data = fernet.decrypt(data)
            with open(file_path, "wb") as f:
                f.write(decrypted_data)
            print(f" Decrypted: {file}")

# --- الأوامر التشغيلية ---
# تأكدي أن اسم المجلد هنا يطابق اسم المجلد على سطح المكتب تماماً (test_folder)
folder_name = "test_folder" 

#generate_key()            
#encrypt_files(folder_name)  
decrypt_files(folder_name) 
