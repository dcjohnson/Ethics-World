import hashlib
import uuid
from random import randint

def GetHash(rawString):
    saltedString = rawString + uuid.uuid4().hex
    newHash = hashlib.sha1()
    newHash.update(bytes(saltedString, encoding = 'utf-8'))
    return newHash.hexdigest()
