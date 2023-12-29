# PGP Encryption/Decryption with RSA

A Python program that uses the Crypto library to perform file encryption and decryption using the PGP (Pretty Good Privacy) encryption scheme. It supports RSA keys and employs the PKCS1_OAEP cipher. The program utilizes command-line arguments for specifying the encryption or decryption operation, the recipient's key file, input file, and output file. It reads data in chunks to handle large files efficiently. Exception handling is implemented to capture and print errors, and success messages are displayed upon completing encryption or decryption.

- main.py: This file contains the core functionality for encrypting and decrypting files. It utilizes the PyCryptodome library for RSA encryption and argparse for command-line argument parsing. The encrypt_file and decrypt_file functions take a recipient's public or private key file, an input file, and generate an encrypted or decrypted output file.

- KeyGeneration.py: This file handles RSA key pair generation. It uses the PyCryptodome library to generate a 2048-bit RSA key pair and exports the private key to a file named "private.key" and the public key to a file named "public.pem."

# Usage:

Run KeyGeneration.py to generate the RSA key pair.
Use main.py to perform encryption or decryption. The script accepts command-line arguments, including the recipient's key file, input file, and output file.

To encrypt: python main.py --encrypt recipient_key input_file output_file

To decrypt: python main.py --decrypt recipient_key input_file output_file

# Dependencies:

PyCryptodome: Install it using pip install pycryptodome.
Feel free to customize the code to fit your needs, and explore the world of RSA-based PGP encryption and decryption with this straightforward implementation.

