import numpy as np
import sympy

# Fungsi untuk menghitung invers modulo 26
def modulo_multiplicative_inverse(A, M):
    for i in range(1, M):
        if (A * i) % M == 1:
            return i
    return -1

# Fungsi untuk mengenkripsi pesan
def encrypt_hill(plain_text, key_matrix):
    dimension = len(key_matrix)
    encrypted_text = ""

    for index in range(0, len(plain_text), dimension):
        vector = []
        for j in range(dimension):
            if index + j < len(plain_text):
                vector.append(ord(plain_text[index + j]) - ord('a'))
            else:
                vector.append(0)
        vector = np.array(vector).reshape(dimension, 1)
        result = (key_matrix @ vector) % 26
        for j in range(dimension):
            encrypted_text += chr(result[j, 0] + ord('a'))

    return encrypted_text

# Fungsi untuk mendekripsi pesan
def decrypt_hill(encrypted_text, key_matrix):
    dimension = len(key_matrix)
    decrypted_text = ""
    det = int(np.round(np.linalg.det(key_matrix))) % 26
    inverse_det = modulo_multiplicative_inverse(det, 26)
    adjugate = (sympy.Matrix(key_matrix).adjugate() % 26)
    inverse_key = (inverse_det * adjugate) % 26

    for index in range(0, len(encrypted_text), dimension):
        vector = []
        for j in range(dimension):
            if index + j < len(encrypted_text):
                vector.append(ord(encrypted_text[index + j]) - ord('a'))
            else:
                vector.append(0)
        vector = np.array(vector).reshape(dimension, 1)
        result = (inverse_key @ vector) % 26
        for j in range(dimension):
            decrypted_text += chr(result[j, 0] + ord('a'))

    return decrypted_text

while True:
    print("Menu:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")
    choice = input("Pilih 1 untuk mengenkripsi, 2 untuk mendekripsi, atau 3 untuk keluar: ")

    if choice == '1':
        # Input key matrix dari pengguna
        print("Masukkan Matriks Kunci (contoh: 17 17 5; 21 18 21; 2 2 19)")
        key_input = []
        for i in range(3):
            row = list(map(int, input("Baris ke-" + str(i + 1) + ": ").split()))
            key_input.append(row)
        key_matrix = np.matrix(key_input)

        # Input plain text dari pengguna
        plain_text = input("Masukkan Plain Text: ").lower()  # Konversi teks ke huruf kecil

        # Enkripsi pesan
        encrypted_text = encrypt_hill(plain_text, key_matrix)
        print("\nEncrypted Text: " + encrypted_text)

    elif choice == '2':
        # Input key matrix dari pengguna
        print("Masukkan Matriks Kunci (contoh: 17 17 5; 21 18 21; 2 2 19)")
        key_input = []
        for i in range(3):
            row = list(map(int, input("Baris ke-" + str(i + 1) + ": ").split()))
            key_input.append(row)
        key_matrix = np.matrix(key_input)

        # Input encrypted text dari pengguna
        encrypted_text = input("Masukkan Encrypted Text: ").lower()  # Konversi teks ke huruf kecil

        # Dekripsi pesan
        decrypted_text = decrypt_hill(encrypted_text, key_matrix)
        print("\nDecrypted Text: " + decrypted_text)

    elif choice == '3':
        print("Terima kasih telah menggunakan program ini.")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")