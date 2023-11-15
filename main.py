from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from KeyGeneration import generateKey
import argparse
import sys

def encrypt_file(recipient_public_key_file, input_file, output_file):
    try:
        with open(recipient_public_key_file, "rb") as public_key_file:
            recipient_public_key = RSA.import_key(public_key_file.read())

        cipher = PKCS1_OAEP.new(recipient_public_key)
        with open(input_file, "rb") as in_file, open(output_file, "wb") as out_file:
            while True:
                chunk = in_file.read(128)  # Read 128 bytes at a time
                if not chunk:
                    break
                encrypted_chunk = cipher.encrypt(chunk)
                out_file.write(encrypted_chunk)

        print("Encryption Successful.")
    except Exception as e:
        print(f"Encryption failed: {str(e)}")

def decrypt_file(recipient_private_key_file, input_file, output_file):
    try:
        with open(recipient_private_key_file, "rb") as private_key_file:
            recipient_private_key = RSA.import_key(private_key_file.read())

        cipher = PKCS1_OAEP.new(recipient_private_key)
        with open(input_file, "rb") as in_file, open(output_file, "wb") as out_file:
            while True:
                chunk = in_file.read(256)  # Read 256 bytes at a time
                if not chunk:
                    break
                decrypted_chunk = cipher.decrypt(chunk)
                out_file.write(decrypted_chunk)

        print("Decryption Successful.")
    except Exception as e:
        print(f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    generateKey()
    parser = argparse.ArgumentParser(description="PGP Encryption/Decryption")
    parser.add_argument("--encrypt", action="store_true", help="Perform encryption")
    parser.add_argument("--decrypt", action="store_true", help="Perform decryption")
    parser.add_argument("recipient_key", help="Recipient's public or private key file")
    parser.add_argument("input_file", help="Input file")
    parser.add_argument("output_file", help="Output file")

    args = parser.parse_args()

    if args.encrypt:
        encrypt_file(args.recipient_key, args.input_file, args.output_file)
    elif args.decrypt:
        decrypt_file(args.recipient_key, args.input_file, args.output_file)
    else:
        print("Please specify either --encrypt or --decrypt.")
