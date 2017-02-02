#Cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
print(key)
print("\n")
f = Fernet(key)
token = f.encrypt(b"I Love You")
print(token)
print(f.decrypt(token))