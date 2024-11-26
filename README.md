Caesar Cipher - Python Program
Description
This Python program implements the Caesar Cipher encryption technique, a type of substitution cipher where each letter in the plaintext is shifted by a certain number of places down or up the alphabet. The program allows you to encrypt and decrypt messages with a specified shift value.

Features:
Encrypt: Encrypts a given plaintext using a shift value.
Decrypt: Decrypts a given ciphertext using the same shift value.
Customizable Shift: Allows the user to choose the shift value for encryption or decryption.
Handles Uppercase and Lowercase Letters: Maintains the case of the original letters during encryption and decryption.
Handles Non-Alphabetical Characters: Ignores numbers, punctuation, and spaces while processing the text.

The program will prompt you to either:

Encrypt a message by entering the plaintext and choosing a shift value.
Decrypt a message by entering the ciphertext and choosing the same shift value used during encryption.

Example
Encrypting a Message:
Enter operation (encrypt/decrypt): encrypt
Enter shift value: 3
Enter the plaintext: Hello, World!
Encrypted text: Khoor, Zruog!
Decrypting a Message:


Decrypting a Message:

Enter operation (encrypt/decrypt): decrypt
Enter shift value: 3
Enter the ciphertext: Khoor, Zruog!
Decrypted text: Hello, World!

Let's say you want to encrypt the message "HELLO" with a shift of 3.

'H' becomes 'K'
'E' becomes 'H'
'L' becomes 'O'
'L' becomes 'O'
'O' becomes 'R'
So, the encrypted message is "KHOOO".

Similarly, for decryption, you would shift each letter by -3.
