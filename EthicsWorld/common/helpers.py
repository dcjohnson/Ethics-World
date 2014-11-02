import hashlib
import uuid
from random import randint
from django.shortcuts import render

def GetHash(rawString):
    saltedString = rawString + uuid.uuid4().hex
    newHash = hashlib.sha1()
    newHash.update(bytes(saltedString, encoding = 'utf-8'))
    return newHash.hexdigest()

def Index(request):
    return render(request, 'basesite.html')
