def encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
       
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Encryption/Decryption Program")
    
    
    action = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    
    
    if action not in ['e', 'd']:
        print("Invalid option. Please choose 'e' to encrypt or 'd' to decrypt.")
        return
    
    
    message = input("Enter the message: ")

   
    while True:
        try:
            shift = int(input("Enter the shift value (an integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the shift value.")
    
    if action == 'e':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif action == 'd':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
