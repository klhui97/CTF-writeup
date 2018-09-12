from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from base64 import b64decode

rsa_key = RSA.importKey(open('private.txt', "rb").read())
verifier = PKCS1_v1_5.new(rsa_key)
raw_cipher_data = b64decode('R1ywgy8D14DFhZVImslTjsZ5Ixso3ljxJiG7luayGwbBH/vE94as4/LXJ3hOfXsMmAsUwB/vYQE5ScxGrkTRxw==')
phn = rsa_key.decrypt(raw_cipher_data)
print(phn)