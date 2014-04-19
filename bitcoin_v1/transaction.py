from Crypto.Hash import SHA256

import ecdsa
import struct

import utils
import publicKey
import opCodeDefinitions
import configuration

# Four-Byte Checksum Length
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
    assert providedChecksum == calculatedChecksum

    return publicAddress160BitHash

# Requires the outgoing public address to create the output script


def createScriptPublicKey(publicAddress):
    assert len(publicAddress) == 34

    publicAddress160BitHash = get160BitHashFromPublicAddress(publicAddress)

    buildScript = (("%02x" % opCodeDefinitions.OP_DUP) +
                   ("%02x" % opCodeDefinitions.OP_HASH160) +
                   ("%02x" % opCodeDefinitions.PUSH_DATA14) +
                   publicAddress160BitHash +
                   ("%02x" % opCodeDefinitions.OP_EQUALVERIFY) +
                   ("%02x" % opCodeDefinitions.OP_CHECKSIG) + 
                   ("%02x" % opCodeDefinitions.OP_CHECKSIGVERIFY) +
                   ("%02x" % opCodeDefinitions.OP_TRUE)
                   )

    return buildScript

def createPreviousScriptPublicKey(publicAddress):
    assert len(publicAddress) == 34

    publicAddress160BitHash = get160BitHashFromPublicAddress(publicAddress)

    buildScript = (("%02x" % opCodeDefinitions.OP_DUP) +
                   ("%02x" % opCodeDefinitions.OP_HASH160) +
                   ("%02x" % opCodeDefinitions.PUSH_DATA14) +
                   publicAddress160BitHash +
                   ("%02x" % opCodeDefinitions.OP_EQUALVERIFY) +
                   ("%02x" % opCodeDefinitions.OP_CHECKSIG) 
                   )

    return buildScript


# This can support multiple transaction inputs but signing multiple inputs is not yet supported


def buildRawTransaction(transactionInputList, transactionOutputList, hashtype):

    def buildTransactionInput(transactionInputList, hashtype):

        # Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
        #     - Sequence is intended to work with Replacements, but Replacement is currently disabled
        inputSequence = "ffffffff"

        inputListLength = len(transactionInputList)

        reversePreviousTransactionHash = []
        previousTransactionOutputIndexHex = []
        scriptSig = []
        scriptSigLength = []

        count = 0
        for x in transactionInputList:
            (previousTransactionHash,
             previousTransactionOutputIndex,
             previousTransactionOutputPublicAddress,
             privateKey
             ) = x

            reversePreviousTransactionHash.append(previousTransactionHash.decode("hex")[::-1].encode("hex"))
            previousTransactionOutputIndexHex.append(struct.pack('<L', previousTransactionOutputIndex).encode('hex'))
            scriptSig.append(createPreviousScriptPublicKey(previousTransactionOutputPublicAddress))
            scriptSigLength.append("%02x" % len(scriptSig[count].decode("hex")))

            count += 1
        # print inputListLength
        # print scriptSig[0]

        transactionInput = []
        for x in xrange(0, inputListLength):
            transactionInput.append("")
            if hashtype[x] == '01':
                for y in xrange(0, inputListLength):
                    if x == y:
                        transactionInput[x] += (reversePreviousTransactionHash[y] +
                                                previousTransactionOutputIndexHex[y] +
                                                scriptSigLength[y] +
                                                scriptSig[y] +
                                                inputSequence)
                    else:
                        transactionInput[x] += (reversePreviousTransactionHash[y] +
                                                previousTransactionOutputIndexHex[y] +
                                                "00" +
                                                inputSequence)
            elif hashtype[x] == '81':
                transactionInput[x] = (reversePreviousTransactionHash[x] +
                                       previousTransactionOutputIndexHex[x] +
                                       scriptSigLength[x] +
                                       scriptSig[x] +
                                       inputSequence)

        # print transactionInput
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

    hxTransactionInputListCount = []
    # print len(hashtype)
    for x in xrange(0, len(hashtype)):
        if hashtype[x] == '01':
            hxTransactionInputListCount.append("%02x" % len(transactionInputList))
        elif hashtype[x] == '81':
            hxTransactionInputListCount.append("%02x" % 1)
    print hxTransactionInputListCount

    #hxTransactionInputList = "".join(map(buildTransactionInput, transactionInputList))

    hxTransactionInputList = buildTransactionInput(transactionInputList, hashtype)

    #hxTransactionInputList = buildTransactionInput(singleTransactionInput)
    hxTransactionOutputListCount = "%02x" % len(transactionOutputList)
    hxTransactionOutputList = "".join(map(buildTransactionOutput, transactionOutputList))
    hxTransactionBlockLockTime = "00000000"
    # hxTransactionHashCode = "01000000"

    transaction = []
    transactioncount = 0
    # print len(hxTransactionInputListCount)
    for x in hxTransactionInputList:
        if hashtype[transactioncount] == '01':
            hxTransactionHashCode = "01000000"
        elif hashtype[transactioncount] == '81':
            hxTransactionHashCode = "81000000"
        transaction.append(hxTransactionVersion +
                           hxTransactionInputListCount[transactioncount] +
                           x +
                           hxTransactionOutputListCount +
                           hxTransactionOutputList +
                           hxTransactionBlockLockTime +
                           hxTransactionHashCode)
        transactioncount += 1

    # print transaction
    return transaction


def buildSignedTransaction(privateKeyList, transactionInputList, transactionOutputList, hashtype):

    rawTransactionList = buildRawTransaction(
        configuration.NEW_TRANSACTION_INPUT, configuration.NEW_TRANSACTION_OUTPUT, hashtype)

    def buildScriptSig(privateKey, doubleSHA256_RawTransaction, hashtype):

        sk = ecdsa.SigningKey.from_string(privateKey.decode('hex'), curve=ecdsa.SECP256k1)
        
        # 01 is hashtype
        sig = sk.sign_digest(doubleSHA256_RawTransaction, sigencode=ecdsa.util.sigencode_der) + hashtype.decode('hex')
       
        pubKey = publicKey.getECDAPublicKeyWithPrefix(publicKey.BITCOIN_PROTOCOL_PUBLIC_KEY_PREFIX, privateKey)
        scriptSig = utils.varstr(sig).encode('hex') + utils.varstr(pubKey.decode('hex')).encode('hex')

        return scriptSig

    def buildTransactionInput(inputParameters, rawTransaction, hashtype):

        # Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
        #     - Sequence is intended to work with Replacements, but Replacement is currently disabled
        inputSequence = "ffffffff"
        (previousTransactionHash,
         previousTransactionOutputIndex,
         previousTransactionOutputPublicAddress,
         privateKey
         ) = inputParameters

        reversePreviousTransactionHash = previousTransactionHash.decode("hex")[::-1].encode("hex")
        previousTransactionOutputIndexHex = struct.pack('<L', previousTransactionOutputIndex).encode('hex')

        singleSHA256_RawTransaction = SHA256.new(rawTransaction.decode("hex")).hexdigest()
        doubleSHA256_RawTransaction = SHA256.new(singleSHA256_RawTransaction.decode("hex")).digest()

        scriptSig = buildScriptSig(privateKey, doubleSHA256_RawTransaction, hashtype)
        scriptSigLength = "%02x" % len(scriptSig.decode("hex"))

        transactionInput = (reversePreviousTransactionHash +
                            previousTransactionOutputIndexHex +
                            scriptSigLength +
                            scriptSig +
                            inputSequence)

        # print transactionInput
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
    hxTransactionInputList = "".join(map(buildTransactionInput, transactionInputList, rawTransactionList, hashtype))
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