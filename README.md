# Caesar-Cipher


This program is an implementation of the Caesar Cipher, a simple encryption technique that has been used for centuries. The program allows users to encrypt and decrypt messages using a key (a numerical value) to shift the letters of the alphabet.

## Usage

To use the program, users must first clone the repository and navigate to the appropriate directory. Then, the program can be run from the command line by using the following command:

```
python3 caesar_cipher.py
```

This will prompt the user to enter a message and a key. The user can then enter their desired message and key, and the program will encrypt or decrypt the message depending on the user's choice.

## Encryption

The encryption process works by shifting the letters of the message by the key value entered by the user. For example, if the key is 3 and the message is "hello", the program will shift the letters three places to the right, resulting in the encrypted message "khoor".

## Decryption

The decryption process works by shifting the letters of the message back by the key value entered by the user. Using the same example, if the key is 3 and the encrypted message is "khoor", the program will shift the letters three places to the left, resulting in the decrypted message "hello".

## Note

This program is intended for educational and demonstration purposes only. It should not be used for any serious encryption or decryption needs as it can be easily broken by anyone with knowledge of the Caesar Cipher technique.

## Requirements

Python 3.x
