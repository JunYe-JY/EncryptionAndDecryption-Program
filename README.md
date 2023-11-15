# EncryptionAndDecryption_Program

A Python program that uses the Crypto library to perform file encryption and decryption using the PGP (Pretty Good Privacy) encryption scheme. It supports RSA keys and employs the PKCS1_OAEP cipher. The program utilizes command-line arguments for specifying the encryption or decryption operation, the recipient's key file, input file, and output file. It reads data in chunks to handle large files efficiently. Exception handling is implemented to capture and print errors, and success messages are displayed upon completing encryption or decryption.

To run this program you must the follow commands:

TO ENCRYPT:
- python3 main.py --encrypt public.pem plaintext.txt encryptedfile.txt
  
TO DECRYPT:
- python3 main.py --decrypt private.key encryptedfile.txt decryptedfile.txt


REQUIRED PYTHON MODULES:
- pycryptodome

