import string

# Fungsi untuk mengenkripsi pesan
def affine_cipher_encrypt(text, a, b):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                encrypted_char = chr(((a * x + b) % 26) + ord('a'))
            else:
                x = ord(char) - ord('A')
                encrypted_char = chr(((a * x + b) % 26) + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

# Fungsi untuk mendekripsi pesan
def affine_cipher_decrypt(text, a, b):
    decrypted_text = ""
    # Mencari nilai a inverse (angka yang ketika dikalikan dengan a menghasilkan 1 mod 26)
    for i in range(26):
        if (a * i) % 26 == 1:
            a_inverse = i
            break
    for char in text:
        if char.isalpha():
            if char.islower():
                x = ord(char) - ord('a')
                decrypted_char = chr(((a_inverse * (x - b)) % 26) + ord('a'))
            else:
                x = ord(char) - ord('A')
                decrypted_char = chr(((a_inverse * (x - b)) % 26) + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

# Meminta dua kunci dari pengguna
a = int(input("Masukkan kunci a (angka yang relatif prima dengan 26): "))
b = int(input("Masukkan kunci b (angka bulat): "))

# Menu di awal program
while True:
    print("Menu:")
    print("1. Enkripsi pesan")
    print("2. Dekripsi pesan")
    print("3. Keluar")

    choice = int(input("Pilih opsi: "))

    if choice == 1:
        plaintext = input("Masukkan pesan yang akan dienkripsi: ")
        encrypted_text = affine_cipher_encrypt(plaintext, a, b)
        print("Pesan Terenkripsi:", encrypted_text)
    elif choice == 2:
        encrypted_text = input("Masukkan pesan terenkripsi: ")
        decrypted_text = affine_cipher_decrypt(encrypted_text, a, b)
        print("Pesan Terdekripsi:", decrypted_text)
    elif choice == 3:
        break
    else:
        print("Pilihan tidak valid. Pilih 1 untuk enkripsi, 2 untuk dekripsi, atau 3 untuk keluar.")
