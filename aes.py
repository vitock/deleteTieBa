from Crypto.Cipher import AES
import hashlib
import base64
import os
import sys

class AEScoder():
    def __init__(self,key):
        md = hashlib.md5();
        md.update(key.encode('utf-8'))                   #制定需要加密的字符串
        realkey = md.hexdigest();
        self.__key = realkey.encode("utf-8");
    # AES加密
    def encrypt(self,data):
        BS = 16
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        cipher = AES.new(self.__key, AES.MODE_ECB)
        encrData = cipher.encrypt(pad(data))
        encrData = base64.b64encode(encrData)
        return encrData.decode('utf-8')
    # AES解密
    def decrypt(self,encrData):
        encrData = base64.b64decode(encrData)
        # unpad = lambda s: s[0:-s[len(s)-1]]
        unpad = lambda s: s[0:-s[-1]]
        cipher = AES.new(self.__key, AES.MODE_ECB)
        decrData = unpad(cipher.decrypt(encrData))
        return decrData.decode('utf-8')

if __name__ == "__main__":
    t = AEScoder("testkey");
    e = t.encrypt("123");
    print (e);
    p = t.decrypt(e);
    print ("\n",p);
    