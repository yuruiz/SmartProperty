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


previousTransactionOutputPublicAddress = "133txdxQmwECTmXqAr9RWNHnzQ175jGb7e"
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



# Finds the Reverse Order of previousTransactionHash
#previousTransactionHash = "202ccf2aaae811e81a6392477210900582c8369a14ba9b72582b78b27edf62df"
#previousTransactionHash = "81b4c832d70cb56ff957589752eb4125a4cab78a25a8fc52d6a09e5bd4404d48"
#previousTransactionHash = "eccf7e3034189b851985d871f91384b8ee357cd47c3024736e5676eb2debb3f2"
previousTransactionHash = "c39e394d41e6be2ea58c2d3a78b8c644db34aeff865215c633fe6937933078a9"
#reversePreviousTransactionHash = previousTransactionHash.decode('hex')[::-1].encode('hex')

#print previousOutputTransactionHash
#print "\t" + reversePreviousOutputTransactionHash

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
previousTransactionOutputIndex = 0
#previousTransactionOutputIndexHex = struct.pack('<L', previousTransactionOutputIndex).encode('hex')

#print "\t" + previousOutputTransactionIndexHex


# scriptSig with Signature
#     scriptSig
#print "\t<scriptSig with Signature>"

#scriptSig = createScriptPublicKey(previousTransactionOutputPublicAddress)
#scriptSig = "76a914010966776006953d5567439e5e39f86a0d273bee88ac"


#scriptSigLength = '%02x' % len(scriptSig.decode('hex'))



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

scriptPubKey_1 = createScriptPublicKey(destinationPubAddress_1)
scriptPubKey_2 = createScriptPublicKey(destinationPubAddress_2)
#scriptPubKey = "76a914097072524438d003d23a2f23edb65aae1bb3e46988ac"

scriptPubKeyLength_1 = '%02x' % len(scriptPubKey_1.decode('hex'))
scriptPubKeyLength_2 = '%02x' % len(scriptPubKey_2.decode('hex'))


# New Transaction Inputs
# List of
#    - Previous Transaction Hash
#    - Previous Transaction Output Index
#    - Previous Transaction Output Public Address
#        - Signature will be calculate from this address
#        - This is the address where you are transferring the Bitcoin from
#        - You must have the private key to this public address
newTransactionInput = [
                       [previousTransactionHash,
                        previousTransactionOutputIndex,
                        previousTransactionOutputPublicAddress
                        ],
                       ]

newTransactionInputCount = "%02x" % len(newTransactionInput)

#print newTransactionInputCount

# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to
newTransactionOutput = [
                        [satoshis_1,
                         destinationPubAddress_1],
                        [satoshis_2,
                         destinationPubAddress_2],
                        ]

# This can support multiple transaction inputs but signing multiple inputs is not yet supported
def buildRawTransaction(transactionInputList, transactionOutputList):

    def buildTransactionInput(inputParameters):
        
        # Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
        #     - Sequence is intended to work with Replacements, but Replacement is currently disabled
        inputSequence = "ffffffff"
        (previousTransactionHash, 
         previousTransactionOutputIndex,
         previousTransactionOutputPublicAddress
         ) = inputParameters
        
        reversePreviousTransactionHash = previousTransactionHash.decode("hex")[::-1].encode("hex")
        previousTransactionOutputIndexHex = struct.pack('<L', previousTransactionOutputIndex).encode('hex')
        
        scriptSig = createScriptPublicKey(previousTransactionOutputPublicAddress)
        scriptSigLength = "%02x" % len(scriptSig.decode("hex"))
        
        transactionInput = (reversePreviousTransactionHash +
                            previousTransactionOutputIndexHex +
                            scriptSigLength +
                            scriptSig + 
                            inputSequence)
        
        return transactionInput
    
    def buildTransactionOutput(outputParameters):
        
        (outputSatoshis, 
         outputPublicAddress
         ) = outputParameters
        
        reverseOutputSatoshisHex = struct.pack("<Q", outputSatoshis).encode('hex')
        
        scriptPublicKey = createScriptPublicKey(outputPublicAddress)
        scriptPublicKeyLength = "%02x" % len(scriptPublicKey.decode("hex"))
        
        transactionOutput = (reverseOutputSatoshisHex +
                             scriptPublicKeyLength +
                             scriptPublicKey)
        
        return transactionOutput
    
    hxTransactionVersion = "01000000"
    hxTransactionInputListCount = "%02x" % len(transactionInputList)
    hxTransactionInputList = "".join(map(buildTransactionInput, transactionInputList))
    hxTransactionOutputListCount = "%02x" % len(transactionOutputList)
    hxTransactionOutputList = "".join(map(buildTransactionOutput, transactionOutputList))
    hxTransactionBlockLockTime = "00000000"
    hxTransactionHashCode = "01000000"

    transaction = (hxTransactionVersion +
                   hxTransactionInputListCount +
                   hxTransactionInputList + 
                   hxTransactionOutputListCount +
                   hxTransactionOutputList +
                   hxTransactionBlockLockTime +
                   hxTransactionHashCode)

    return transaction

def buildSignedTransaction(privateKey, transactionInputList, transactionOutputList):
    
    rawTransaction = buildRawTransaction(newTransactionInput, newTransactionOutput)
    
    def buildScriptSig(rawTransaction):
        singleSHA256_RawTransaction = SHA256.new(rawTransaction.decode("hex")).hexdigest()
        doubleSHA256_RawTransaction = SHA256.new(singleSHA256_RawTransaction.decode("hex")).digest()
        
        #double hash:5dafd07e944f532ed3c09e5f06f0da4e1aaa5b3490441c47fe5ced27d1b33c1b
        print "double hash raw txn:" + doubleSHA256_RawTransaction.encode("hex")
        
        sk =  ecdsa.SigningKey.from_string(privateKey.decode('hex'), curve=ecdsa.SECP256k1)
        sig = sk.sign_digest(doubleSHA256_RawTransaction, sigencode=ecdsa.util.sigencode_der) + '\01' # 01 is hashtype
        pubKey = publicKey.getECDAPublicKeyWithPrefix(publicKey.BITCOIN_PROTOCOL_PUBLIC_KEY_PREFIX, privateKey)
        scriptSig = utils.varstr(sig).encode('hex') + utils.varstr(pubKey.decode('hex')).encode('hex')
    
        return scriptSig
    
    def buildTransactionInput(inputParameters):
        
        # Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
        #     - Sequence is intended to work with Replacements, but Replacement is currently disabled
        inputSequence = "ffffffff"
        (previousTransactionHash, 
         previousTransactionOutputIndex,
         previousTransactionOutputPublicAddress
         ) = inputParameters
        
        reversePreviousTransactionHash = previousTransactionHash.decode("hex")[::-1].encode("hex")
        previousTransactionOutputIndexHex = struct.pack('<L', previousTransactionOutputIndex).encode('hex')
        
        scriptSig = buildScriptSig(rawTransaction)
        scriptSigLength = "%02x" % len(scriptSig.decode("hex"))
        
        transactionInput = (reversePreviousTransactionHash +
                            previousTransactionOutputIndexHex +
                            scriptSigLength +
                            scriptSig + 
                            inputSequence)
        
        return transactionInput
    
    def buildTransactionOutput(outputParameters):
        
        (outputSatoshis, 
         outputPublicAddress
         ) = outputParameters
        
        reverseOutputSatoshisHex = struct.pack("<Q", outputSatoshis).encode('hex')
        
        scriptPublicKey = createScriptPublicKey(outputPublicAddress)
        scriptPublicKeyLength = "%02x" % len(scriptPublicKey.decode("hex"))
        
        transactionOutput = (reverseOutputSatoshisHex +
                             scriptPublicKeyLength +
                             scriptPublicKey)
        
        return transactionOutput
    
    hxTransactionVersion = "01000000"
    hxTransactionInputListCount = "%02x" % len(transactionInputList)
    hxTransactionInputList = "".join(map(buildTransactionInput, transactionInputList))
    hxTransactionOutputListCount = "%02x" % len(transactionOutputList)
    hxTransactionOutputList = "".join(map(buildTransactionOutput, transactionOutputList))
    hxTransactionBlockLockTime = "00000000"
    #hxTransactionHashCode = "01000000"

    transaction = (hxTransactionVersion +
                   hxTransactionInputListCount +
                   hxTransactionInputList +
                   hxTransactionOutputListCount +
                   hxTransactionOutputList +
                   hxTransactionBlockLockTime)

    return transaction



stxn = buildSignedTransaction(privKey, newTransactionInput, newTransactionOutput)

txnUtils.verifyTxnSignature(stxn)
    
print stxn












'''    
    outputs = [
                [satoshis_1, createScriptPublicKey("1KKKK6N21XKo48zWKuQKXdvSsCf95ibHFa")],
                [satoshis_2, createScriptPublicKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7")]
               ]

    outputs = [[satoshis_1, scriptPubKey_1],[20000, createScriptPublicKey("15nhZbXnLMknZACbb3Jrf1wPCD9DWAcqd7")]]

    signedTransaction = txnUtils.makeRawTransaction(previousTransactionHash, 
                                                previousTransactionOutputIndex, 
                                                scriptSig, 
                                                outputs) #newTransactionOutput)
    txnUtils.verifyTxnSignature(signedTransaction)
    print signedTransaction






buildSignedTransaction(newTransactionInput, newTransactionOutput)
'''









