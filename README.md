# python-encryption-decryption

How the program works:

The program takes the password from the user, but in a simple example does not convert
it to a key (in a real application this could be done using PBKDF2 or another method).
The user chooses whether to encrypt or decrypt the file.
Depending on the selected action, the appropriate function is performed.


Important notes:

The key should actually be generated from the password or should be stored securely.
Encryption and decryption should be performed on files with appropriate formats, 
not on binary files that may contain non-text data.
