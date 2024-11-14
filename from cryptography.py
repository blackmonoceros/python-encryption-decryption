from cryptography.fernet import Fernet
import os
import sys

# Funkcja do generowania klucza
def generate_key(password: str) -> bytes:
    # Użyj hasła do stworzenia klucza
    return Fernet.generate_key()

# Funkcja do szyfrowania pliku
def encrypt_file(file_name: str, key: bytes):
    fernet = Fernet(key)
    with open(file_name, 'rb') as file:
        original = file.read()
    
    encrypted = fernet.encrypt(original)

    with open(file_name + '.enc', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print(f'Plik {file_name} został zaszyfrowany!')

# Funkcja do deszyfrowania pliku
def decrypt_file(encrypted_file_name: str, key: bytes):
    fernet = Fernet(key)
    with open(encrypted_file_name, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(encrypted_file_name.replace('.enc', ''), 'wb') as decrypted_file:
        decrypted_file.write(decrypted)

    print(f'Plik {encrypted_file_name} został odszyfrowany!')

def main():
    # Klucz powinien być generowany lub wprowadzony (w tym przypadku to jest tylko przykładowy klucz!)
    password = input("Podaj hasło (używamy tego samego dla szyfrowania i deszyfrowania): ")
    key = generate_key(password) 
     # W prawdziwej aplikacji klucz powinien być generowany z hasła

    action = input("Wybierz akcję (szyfruj/odszyfruj): ").strip().lower()
    file_name = input("Podaj nazwę pliku: ")

    if action == 'szyfruj':
        encrypt_file(file_name, key)
    elif action == 'odszyfruj':
        decrypt_file(file_name, key)
    else:
        print("Nieprawidłowa akcja!")

if __name__ == "__main__":
    main()
