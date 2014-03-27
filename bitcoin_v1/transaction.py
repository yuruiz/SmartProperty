from Crypto.Hash import SHA256

import ecdsa
import struct

import utils
import publicKey
import opCodeDefinitions
import configuration

#Four-Byte Checksum Length
CHECKSUM_BYTE_LENGTH = 4
CHECKSUM_LENGTH = CHECKSUM_BYTE_LENGTH * 2


# Returns the Public Key Hash <=> Same as the RIPEMD160
def get160BitHashFromPublicAddress(publicAddress):
    
    # Obtains the Hash of the Public Address
    leadingOnes = utils.countLeadingChars(publicAddress, '1')
    addressWithChecksum = utils.base256encode(utils.base58decode(publicAddress))
    addressWithLeadingZeros = '\0' * leadingOnes + addressWithChecksum[:-CHECKSUM_BYTE_LENGTH]
    publicAddress160BitHash = addressWithLeadingZeros[1:].encode("hex")
    
    # Parses the Public Address for Checksum
    providedChecksum = addressWithChecksum[-CHECKSUM_BYTE_LENGTH:].encode("hex")
    
    # Calculates the Checksum based on Parsed Address
    oneSHA256MainAddress = SHA256.new(addressWithLeadingZeros)
    twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.digest()).hexdigest()
    calculatedChecksum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]

    # Checks to make sure the checksum provided matches the calculated checksum
    #    of the 160bit of the public address
    assert(providedChecksum == calculatedChecksum)
    
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


scriptPubKey_1 = createScriptPublicKey(configuration.DESTINATION_PUBLIC_ADDRESS_1)
#scriptPubKey_2 = createScriptPublicKey(configuration.DESTINATION_PUBLIC_ADDRESS_2)

scriptPubKeyLength_1 = '%02x' % len(scriptPubKey_1.decode('hex'))
#scriptPubKeyLength_2 = '%02x' % len(scriptPubKey_2.decode('hex'))




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
    
    rawTransaction = buildRawTransaction(configuration.NEW_TRANSACTION_INPUT, configuration.NEW_TRANSACTION_OUTPUT)
    #print len(rawTransaction)
    def buildScriptSig(rawTransaction):
        singleSHA256_RawTransaction = SHA256.new(rawTransaction.decode("hex")).hexdigest()
        doubleSHA256_RawTransaction = SHA256.new(singleSHA256_RawTransaction.decode("hex")).digest()
        
        #double hash:5dafd07e944f532ed3c09e5f06f0da4e1aaa5b3490441c47fe5ced27d1b33c1b
        #print "double hash raw txn:" + doubleSHA256_RawTransaction.encode("hex")
        
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

    transaction = (hxTransactionVersion +
                   hxTransactionInputListCount +
                   hxTransactionInputList +
                   hxTransactionOutputListCount +
                   hxTransactionOutputList +
                   hxTransactionBlockLockTime)

    return transaction
