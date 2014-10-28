import hashlib

def GetHash(rawString):
    newHash = hashlib.sha1()
    newHash.update(bytes(rawString, encoding = 'utf-8'))
    return newHash.hexdigest()
