import utils, sys

from Crypto.Random import random
from Crypto.Hash import SHA256


#Bitcoin Network Prefix
MAINNET_ADDRESS_PREFIX = 0x80
TESTNET_ADDRESS_PREFIX = 0xEF

#Four-Byte Checksum Length
CHECKSUM_LENGTH = 4 * 2

#This creates a cryptographically secure random 256bit private key
def getStrongRandomKey(bits):
    
    sRandom = random.StrongRandom()
    randomBits = sRandom.getrandbits(bits)
    stringRandomBits = str(randomBits)
    sRandomPrivateKey = SHA256.new(stringRandomBits).hexdigest()
        
    return sRandomPrivateKey

def getWIFPrivateKey(privateKey, networkType):
    
    if networkType == "main":
        mainAddress = "".join(("%x" % MAINNET_ADDRESS_PREFIX, privateKey))
        
        #Calculates the checksum
        oneSHA256MainAddress = SHA256.new(mainAddress.decode("hex")).hexdigest()
        twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.decode("hex")).hexdigest()
        mainAddressCheckSum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
        
        mainAddressWithChecksum = "".join((mainAddress, mainAddressCheckSum))
        mainAddressWIF = utils.base58encode(utils.base256decode(mainAddressWithChecksum.decode("hex")))
        return mainAddressWIF
    
    elif networkType == "test":
        testAddress = "".join(("%x" % TESTNET_ADDRESS_PREFIX, privateKey))
        
        #Calculates the checksum
        oneSHA256TestAddress = SHA256.new(testAddress.decode("hex")).hexdigest()
        twoSHA256TestAddress = SHA256.new(oneSHA256TestAddress.decode("hex")).hexdigest()
        testAddressCheckSum = twoSHA256TestAddress[0:CHECKSUM_LENGTH]
        
        testAddressWithChecksum = "".join((testAddress, testAddressCheckSum))
        testAddressWIF = utils.base58encode(utils.base256decode(testAddressWithChecksum.decode("hex")))
        return testAddressWIF
        
    else:
        print sys.stdout.write("getWIFPrivateKey Error") 
    
    return 0
    

#print keyUtils.privateKeyToWif(privateKey)
#print keyUtils.keyToAddr(privateKey)

