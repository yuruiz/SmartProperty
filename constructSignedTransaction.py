import ecdsa
import hashlib
import struct
import unittest

import utils
import keyUtils
import publicKey
import privateKey

from Crypto.Hash import SHA256
import generateAddress
import opCodeDefinitions
import txnUtils

#Four-Byte Checksum Length
CHECKSUM_BYTE_LENGTH = 4
CHECKSUM_LENGTH = CHECKSUM_BYTE_LENGTH * 2

privKey = generateAddress.privKey
#privKey = privateKey.getWIFPrivateKey(privKey, "main")
#privKey = keyUtils.wifToPrivateKey("5Kb6aGpijtrb8X28GzmWtbcGZCG8jHQWFJcWugqo3MwKRvC8zyu")
print privKey 


sourcePubAddress = "133txdxQmwECTmXqAr9RWNHnzQ175jGb7e"
destinationPubAddress_1 = "1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa"
destinationPubAddress_2 = "15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7"
#print pubAddress.encode("hex")
#print utils.base58CheckDecode("1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa").encode('hex')

# Returns the Public Key Hash <=> Same as the RIPEMD160
def get160BitHashFromPublicAddress(publicAddress):
    
    # Obtains the Hash of the Public Address
    leadingOnes = utils.countLeadingChars(publicAddress, '1')
    addressWithChecksum = utils.base256encode(utils.base58decode(publicAddress))
    addressWithLeadingZeros = '\0' * leadingOnes + addressWithChecksum[:-CHECKSUM_BYTE_LENGTH]
    publicAddress160BitHash = addressWithLeadingZeros[1:].encode("hex")
    
    # Parses the Public Address for Checksum
    providedChecksum = addressWithChecksum[-CHECKSUM_BYTE_LENGTH:].encode("hex")
    #print providedChecksum
    
    # Calculates the Checksum based on Parsed Address
    oneSHA256MainAddress = SHA256.new(addressWithLeadingZeros)
    twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.digest()).hexdigest()
    calculatedChecksum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
    #print calculatedChecksum
    
    # Checks to make sure the checksum provided matches the calculated checksum
    #    of the 160bit of the public address
    assert(providedChecksum == calculatedChecksum)
    
    # Version of the Bitcoin Network
    # PUBKEY - Normal Transactions (0x00)
    # SCRIPT - MULTI_SIG Transactions (0x05)
    # TESTNET - Test Network (0x6F)
    version = addressWithLeadingZeros[0]
    
    return publicAddress160BitHash

# Requires the outgoing public address to create the output script
def createScriptPublicKey(publicAddress):
    assert(len(publicAddress) == 34)
    
    publicAddress160BitHash = get160BitHashFromPublicAddress(publicAddress)
    
    buildScript = (("%02x" % opCodeDefinitions.OP_DUP) +
                   ("%02x" % opCodeDefinitions.OP_HASH160) +
                   ("%02x" % opCodeDefinitions.PUSH_DATA14) +
                   publicAddress160BitHash +
                   ("%02x" % opCodeDefinitions.OP_EQUALVERIFY) +
                   ("%02x" % opCodeDefinitions.OP_CHECKSIG))
    
    return buildScript

# 4 bytes version
version = "01000000"
#print version

# Number of Inputs for the New Transaction
newTransactionNumInput = "01"

#print newTransactionNumInput

# Finds the Reverse Order of previousOutputTransactionHash
#previousOutputTransactionHash = "202ccf2aaae811e81a6392477210900582c8369a14ba9b72582b78b27edf62df"
#previousOutputTransactionHash = "81b4c832d70cb56ff957589752eb4125a4cab78a25a8fc52d6a09e5bd4404d48"
#previousOutputTransactionHash = "eccf7e3034189b851985d871f91384b8ee357cd47c3024736e5676eb2debb3f2"
previousOutputTransactionHash = "c39e394d41e6be2ea58c2d3a78b8c644db34aeff865215c633fe6937933078a9"
reversePreviousOutputTransactionHash = previousOutputTransactionHash.decode('hex')[::-1].encode('hex')

#print previousOutputTransactionHash
#print "\t" + reversePreviousOutputTransactionHash

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
previousOutputTransactionIndex = 0
previousOutputTransactionIndexHex = struct.pack('<L', previousOutputTransactionIndex).encode('hex')

#print "\t" + previousOutputTransactionIndexHex


# scriptSig with Signature
#     scriptSig
#print "\t<scriptSig with Signature>"

scriptSig = createScriptPublicKey(sourcePubAddress)
#scriptSig = "76a914010966776006953d5567439e5e39f86a0d273bee88ac"


# scriptSig Length
#     '%02x' % len(scriptSig.decode('hex')) + 
#print "\t<scriptSig Length>"

scriptSigLength = '%02x' % len(scriptSig.decode('hex'))

# Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
#     - Sequence is intended to work with Replacements, but Replacement is currently disabled
transactionSequence = "ffffffff"
#print "\t" + transactionSequence

newTransactionOutputCount = 2
newTransactionOutputCountHex = "%02x" % newTransactionOutputCount
#print newTransactionOutputCountHex

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC
#satoshis = 99900000
#satoshis = 40000000
satoshis_1 = 24321
satoshisToRedeem_1 = struct.pack("<Q", satoshis_1).encode('hex')
satoshis_2 = 20000
satoshisToRedeem_2 = struct.pack("<Q", satoshis_2).encode('hex')

#print "\t" + satoshisToRedeem

# scriptPubKey with Signature
#     scriptPubKey
#print "\t<scriptPubKey with Signature>"

scriptPubKey_1 = createScriptPublicKey(destinationPubAddress_1)
scriptPubKey_2 = createScriptPublicKey(destinationPubAddress_2)
#scriptPubKey = "76a914097072524438d003d23a2f23edb65aae1bb3e46988ac"

# scriptPubKey Length
#     '%02x' % len(scriptSig.decode('hex')) + 
#print "\t<scriptPubKey Length>"

scriptPubKeyLength_1 = '%02x' % len(scriptPubKey_1.decode('hex'))
scriptPubKeyLength_2 = '%02x' % len(scriptPubKey_2.decode('hex'))

# Lock Time
blockLockTime = "00000000"
#print blockLockTime



transactionToBeSigned = (version +
                         newTransactionNumInput +
                         reversePreviousOutputTransactionHash +
                         previousOutputTransactionIndexHex +
                         scriptSigLength +
                         scriptSig +
                         transactionSequence +
                         newTransactionOutputCountHex +
                         satoshisToRedeem_1 +
                         scriptPubKeyLength_1 +
                         scriptPubKey_1 +
                         satoshisToRedeem_2 +
                         scriptPubKeyLength_2 +
                         scriptPubKey_2 +
                         blockLockTime +
                         "01000000" # hash code
                         )
'''
transactionToBeSigned = (version + "\n" +
                         newTransactionNumInput +  "\n" +
                         reversePreviousOutputTransactionHash + "\n" +
                         previousOutputTransactionIndexHex + "\n" +
                         scriptSigLength + "\n" +
                         scriptSig + "\n" +
                         transactionSequence + "\n" +
                         newTransactionOutputCountHex + "\n" +
                         satoshisToRedeem +  "\n" +
                         scriptPubKeyLength + "\n" +
                         scriptPubKey + "\n" +
                         blockLockTime +  "\n" +
                         "01000000" # hash code
                         )
'''


#print transactionToBeSigned

oneSHA256_TransactionToBeSigned = SHA256.new(transactionToBeSigned.decode("hex")).hexdigest()
twoSHA256_TransactionToBeSigned = SHA256.new(oneSHA256_TransactionToBeSigned.decode("hex")).digest()

#double hash:5dafd07e944f532ed3c09e5f06f0da4e1aaa5b3490441c47fe5ced27d1b33c1b
print "double hash:" + twoSHA256_TransactionToBeSigned.encode("hex")

sk =  ecdsa.SigningKey.from_string(privKey.decode('hex'), curve=ecdsa.SECP256k1)
sig = sk.sign_digest(twoSHA256_TransactionToBeSigned, sigencode=ecdsa.util.sigencode_der) + '\01' # 01 is hashtype
pubKey = publicKey.getECDAPublicKeyWithPrefix(publicKey.BITCOIN_PROTOCOL_PUBLIC_KEY_PREFIX, privKey)
scriptSig = utils.varstr(sig).encode('hex') + utils.varstr(pubKey.decode('hex')).encode('hex')
print scriptSig


# scriptSig Length
#     '%02x' % len(scriptSig.decode('hex')) + 
#print "\t<scriptSig Length>"

scriptSigLength = '%02x' % len(scriptSig.decode('hex'))

print scriptSigLength

'''
signedTransaction = (version + "\n" +
                     newTransactionNumInput +  "\n" +
                     reversePreviousOutputTransactionHash + "\n" +
                     previousOutputTransactionIndexHex + "\n" +
                     scriptSigLength + "\n" +
                     scriptSig + "\n" +
                     transactionSequence + "\n" +
                     newTransactionOutputCountHex + "\n" +
                     satoshisToRedeem +  "\n" +
                     scriptPubKeyLength + "\n" +
                     scriptPubKey + "\n" +
                     blockLockTime +  "\n" +
                     "01000000" # hash code
                     )
'''
outputs = [[satoshis_1, scriptPubKey_1],[20000, createScriptPublicKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7")]]
signedTransaction = txnUtils.makeRawTransaction(previousOutputTransactionHash, 
                                                previousOutputTransactionIndex, 
                                                scriptSig, 
                                                outputs)

txnUtils.verifyTxnSignature(signedTransaction)

print signedTransaction



#signedTransaction = 

#signed_txn = makeRawTransaction(outputTransactionHash, sourceIndex, scriptSig, outputs)
#verifyTxnSignature(signed_txn)
