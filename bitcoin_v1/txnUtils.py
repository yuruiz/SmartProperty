from Crypto.Hash import SHA256
import binascii

def getTransactionHash(signedTransaction):
    singleSHA256 = SHA256.new(binascii.unhexlify(signedTransaction))
    doubleSHA256 = SHA256.new(singleSHA256.digest()).digest().encode('hex')
    dHashed = doubleSHA256.decode("hex")[::-1].encode("hex")
    
    return dHashed

