def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            decrypted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            if is_upper:
                decrypted_char = decrypted_char.upper()
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

while True:
    print("Pilih tindakan:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

    choice = input("Masukkan pilihan (1/2/3): ")

    if choice == '1':
        text = input("Masukkan teks yang akan dienkripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (integer): "))  # Perbaiki tanda kurung tutup di sini
        encrypted_text = caesar_encrypt(text, shift)
        print("Teks Terenkripsi:", encrypted_text)
    elif choice == '2':
        text = input("Masukkan teks yang akan didekripsi: ")
        shift = int(input("Masukkan jumlah pergeseran (integer): "))  # Perbaiki tanda kurung tutup di sini
        decrypted_text = caesar_decrypt(text, shift)
        print("Teks Terdekripsi:", decrypted_text)
    elif choice == '3':
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan masukkan 1, 2, atau 3.")
