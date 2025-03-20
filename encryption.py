from cryptography.fernet import Fernet
from keymanager import load_key

def encrypt_file(filename):
    key = load_key()
    fernet = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = fernet.encrypt(file_data)

    with open(filename + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"File '{filename}' encrypted successfully as '{filename}.enc'.")

def decrypt_file(encrypted_filename, output_filename):
    key = load_key()
    fernet = Fernet(key)

    with open(encrypted_filename, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    decrypted_data = fernet.decrypt(encrypted_data)

    with open(output_filename, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"File '{encrypted_filename}' decrypted successfully as '{output_filename}'.")
