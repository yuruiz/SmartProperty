import utils, sys

from ecdsa import SigningKey, SECP256k1

from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160

#Bitcoin Network Address Prefix
# PUBKEY - Normal Transactions
# SCRIPT - MULTI_SIG Transactions
# TESTNET - Test Network
MAINNET_ADDRESS_PUBKEY_PREFIX = 0x00
MAINNET_ADDRESS_SCRIPT_PREFIX = 0x05
TESTNET_ADDRESS_PREFIX = 0x6F

#Four-Byte Checksum Length
CHECKSUM_LENGTH = 4 * 2

#Bitcoin Protocol Public Key Prefix
BITCOIN_PROTOCOL_PUBLIC_KEY_PREFIX = "\04"

def getECDAPublicKeyWithPrefix(prefix, privateKey):
    signingKey = SigningKey.from_string(privateKey.decode("hex"), curve=SECP256k1)
    verifyingKey = signingKey.verifying_key
    publicKeyWithPrefix = (prefix + verifyingKey.to_string()).encode("hex")
    
    return publicKeyWithPrefix

def get160BitPublicKeyHash(publicKeyWithPrefix):
    SHA256_PublicKeyWithPrefix = SHA256.new(publicKeyWithPrefix.decode("hex"))
    RIPEMD160_SHA256PublicKeyWithPrefix = RIPEMD160.new(SHA256_PublicKeyWithPrefix.digest())
    RIPEMD160SHA256Hash = RIPEMD160_SHA256PublicKeyWithPrefix.hexdigest()
    #print RIPEMD160SHA256Hash
    return RIPEMD160SHA256Hash

def getAddress(RIPEMD160SHA256Hash, addressType):
    if addressType == "main_pubkey":
        address = "".join(("%02x" % MAINNET_ADDRESS_PUBKEY_PREFIX, RIPEMD160SHA256Hash))
        
        #Calculates the checksum
        oneSHA256MainAddress = SHA256.new(address.decode("hex")).hexdigest()
        twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.decode("hex")).hexdigest()
        addressCheckSum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
        
        addressWithChecksum = "".join((address, addressCheckSum))
        addressPublicKey = utils.base58encode(utils.base256decode(addressWithChecksum.decode("hex")))
        
        #leading zero to account for adding the 1 prefix to the bitcoin address
        leadingZeros = utils.countLeadingChars(address.decode("hex"), '\0')
        
        return '1' * leadingZeros + addressPublicKey
    
    elif addressType == "main_script":
        address = "".join(("%02x" % MAINNET_ADDRESS_SCRIPT_PREFIX, RIPEMD160SHA256Hash))
        
        #Calculates the checksum
        oneSHA256MainAddress = SHA256.new(address.decode("hex")).hexdigest()
        twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.decode("hex")).hexdigest()
        addressCheckSum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
        
        addressWithChecksum = "".join((address, addressCheckSum))
        addressPublicKey = utils.base58encode(utils.base256decode(addressWithChecksum.decode("hex")))
        return addressPublicKey
    
    elif addressType == "test":
        address = "".join(("%02x" % TESTNET_ADDRESS_PREFIX, RIPEMD160SHA256Hash))
        
        #Calculates the checksum
        oneSHA256MainAddress = SHA256.new(address.decode("hex")).hexdigest()
        twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.decode("hex")).hexdigest()
        addressCheckSum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
        
        addressWithChecksum = "".join((address, addressCheckSum))
        addressPublicKey = utils.base58encode(utils.base256decode(addressWithChecksum.decode("hex")))
        return addressPublicKey
        
    else:
        print sys.stdout.write("getWIFPrivateKey Error") 
    
    return 0

def getPublicAddress(privateKey, addressType):
    publicKeyWithPrefix = getECDAPublicKeyWithPrefix(BITCOIN_PROTOCOL_PUBLIC_KEY_PREFIX, privateKey)
    RIPEMD160SHA256Hash = get160BitPublicKeyHash(publicKeyWithPrefix)
    publicAddress = getAddress(RIPEMD160SHA256Hash, addressType)
    
    return publicAddress
