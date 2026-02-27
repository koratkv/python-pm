import base64
import os
from argon2 import PasswordHasher
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 

class Crypto:
    def __init__(self):
        self.salt = os.urandom(16)
        self.ph = PasswordHasher()

    def hash(self, data):
        hashedPassword = self.ph.hash(data)
        return hashedPassword, self.salt
    
    def verify(self, hashedPassword, data):
        return self.ph.verify(hashedPassword, data)

    def generateEncryptionKey(self, salt, data):
        kdf = PBKDF2HMAC(
            algorithm = hashes.SHA256(),
            length = 32,
            salt = salt,
            iterations = 1_200_000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(data.encode()))

        return key

    def encrypt(self, key, data):
        fernet = Fernet(key)
        encryptedPassword = fernet.encrypt(data)
        return encryptedPassword

    def decrypt(self, key, data):
        fernet = Fernet(key)
        decryptedPassword = fernet.decrypt(data)
        return decryptedPassword
