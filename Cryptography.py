#Cryptography
from cryptography.fernet import Fernet
#generate a key from the module
key = Fernet.generate_key()
print(key)
print("\n")
#Create a fernet object to encrypt text
f = Fernet(key)

#create token using the text
token = f.encrypt(b"I Love You")
print(token)

#decrypt the token using the ferent object
print(f.decrypt(token))
