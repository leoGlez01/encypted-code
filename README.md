<h1>Encrypted Code - L0123 Algorithm</h1>

> [!INFO]
EncryptedCode is a python library accessible to everyone that is under development where I use a new encryption algorithm created by &copy; Software Engineer <a href="https://leoglez.vercel.app/">Leandro Gonzalez Espinosa.</a> and named L0123.

# INSTALATION
pip install encryptedcode

>[!IMPORTANT]
 REMEMBER SAVE THE KEY INSIDE TO ENVIROMENT VARIABLE FOR YOUR SECURITY

### USAGE EXAMPLE
key = generate_key()
cadena = "Hey! I'm a simple String"
encoded = encode(cadena, key)
print(f"Encoded: {encoded}")
decoded = decode(encoded, key)
print(f"Decoded: {decoded}")