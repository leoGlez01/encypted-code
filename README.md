<h1>Encrypted Code - L0123 Algorithm</h1>

>[!NOTE]
 EncryptedCode is a python library accessible to everyone that is under improvements where I use a new encryption algorithm created by &copy; Software Engineer <a href="https://leoglez.vercel.app/">Leandro Gonzalez Espinosa.</a> and named L0123.

## INSTALATION
``` bash
pip install encryptedcode
```
>[!IMPORTANT]
 REMEMBER SAVE THE KEY INSIDE TO ENVIROMENT VARIABLE FOR YOUR SECURITY

### USAGE EXAMPLE
```python
#imports
from encryptedcode.encrypted_code import generate_key, encode, decode

key = generate_key()
cadena = "Hey! I'm a simple String"
encoded = encode(cadena, key)
print(f"Encoded: {encoded}")
decoded = decode(encoded, key)
print(f"Decoded: {decoded}")
```
