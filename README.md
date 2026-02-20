# Ransomware Simulation & Recovery Tool (Educational)

A Python-based project demonstrating how ransomware encrypts files and how data can be recovered using secure key management.

##  Purpose
This project was developed for **educational and cybersecurity awareness purposes**. It illustrates the mechanics of symmetric encryption (AES) and the importance of encryption key security.

##  Features
- **Key Generation:** Creates a secure `.key` file using the Fernet (cryptography) library.
- **File Encryption:** Encrypts all `.txt` files within a specified directory.
- **Data Recovery:** Provides a decryption mechanism to restore files to their original state.

##  Requirements
- Python 3.x
- `cryptography` library

##  How it Works
1. Run the script to generate a key and encrypt files in the target folder.
2. To recover files, use the generated `secret.key` with the decryption function.

**Disclaimer:** This tool is for authorized educational use only.
