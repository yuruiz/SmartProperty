from Crypto.Hash import SHA256
import binascii, struct, translationUtil

def getInputScriptSizeByte(inputScriptLengthSizeHex):
        inputScriptSizeInt = int(inputScriptLengthSizeHex, 16)
        return inputScriptSizeInt

def getTransactionHash(signedTransaction):
    singleSHA256 = SHA256.new(binascii.unhexlify(signedTransaction))
    doubleSHA256 = SHA256.new(singleSHA256.digest()).digest().encode('hex')
    dHashed = doubleSHA256.decode("hex")[::-1].encode("hex")
    
    return dHashed

def getVersion(transaction):
    
    versionOffsetByte = 1
    versionSizeByte = 4
    
    versionOffset = (versionOffsetByte - 1) * 2
    versionOffsetSize = versionSizeByte * 2
    
    versionCount = transaction[versionOffset:versionOffset+versionOffsetSize]
    
    return versionCount

def getInputCount(transaction):
    
    inputCountOffsetByte = 5
    inputCountSizeByte = 1
    
    inputOffset = (inputCountOffsetByte - 1) * 2
    inputOffsetSize = inputCountSizeByte * 2
    
    inputCount = transaction[inputOffset:inputOffset+inputOffsetSize]
    
    return inputCount

def getInputSectionStartByte(transaction, inputIndexOffset):
    
    startingInputSectionOffsetByte = 0
    startingPrevOutputHashOffsetByte = 0
    startingPrevOutputHashIndexOffsetByte = 0
    startingInputScriptLengthOffsetByte = 0
    startingInputScriptOffsetByte = 0
    startingInputSequenceOffsetByte = 0

    for x in xrange(0, inputIndexOffset + 1):
    
        if x == 0:
            startingInputSectionOffsetByte = 6
        else:
            # Previous Transaction Hash
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            
            # Previous Transaction Hash Index
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            
            # Input Script Length
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte =1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            
            # Input Sequence 
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            
            startingInputSectionOffsetByte = (startingInputSequenceOffsetByte + inputSequenceSizeByte)
            
            #print "startingInputSectionOffsetByte Start: " + str(startingInputSequenceOffsetByte + inputSequenceSizeByte)

    return startingInputSectionOffsetByte

def getInputSectionAll(transaction):

    inputCount = int(getInputCount(transaction), 16)
    
    print inputCount
    
    startingInputSectionOffsetByte = 0
    startingPrevOutputHashOffsetByte = 0
    startingPrevOutputHashIndexOffsetByte = 0
    startingInputScriptLengthOffsetByte = 0
    startingInputScriptOffsetByte = 0
    startingInputSequenceOffsetByte = 0

    transactionInputList = []

    for x in xrange(0, inputCount):
    
        if x == 0:
            startingInputSectionOffsetByte = 6
            # Previous Transaction Hash
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            prevOutputHashOffset = (startingPrevOutputHashOffsetByte - 1) * 2
            prevOutputHashOffsetSize = prevOutputHashSizeByte * 2
            prevOutputHash = transaction[prevOutputHashOffset : prevOutputHashOffset + prevOutputHashOffsetSize]
            
            # Previous Transaction Hash Index
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            prevOutputHashIndexOffset = (startingPrevOutputHashIndexOffsetByte - 1) * 2
            prevOutputHashIndexOffsetSize = prevOutputHashIndexSizeByte * 2
            prevOutputHashIndex = transaction[prevOutputHashIndexOffset : prevOutputHashIndexOffset + prevOutputHashIndexOffsetSize]
            
            # Input Script Length
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte = 1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            inputScriptOffset = (startingInputScriptOffsetByte - 1) * 2
            inputScriptOffsetSize = inputScriptSizeByte * 2        
            inputScript = transaction[inputScriptOffset : inputScriptOffset + inputScriptOffsetSize]
                                      
            # Input Sequence 
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            inputSequenceOffset = (startingInputSequenceOffsetByte - 1) * 2
            inputSequenceOffsetSize = inputSequenceSizeByte * 2        
            inputSequence = transaction[inputSequenceOffset : inputSequenceOffset + inputSequenceOffsetSize]
            
            transactionInput = (prevOutputHash + 
                                prevOutputHashIndex +
                                inputScriptLength + 
                                inputScript + 
                                inputSequence)
                                
            transactionInputList.append(transactionInput)
            startingInputSectionOffsetByte = startingInputSequenceOffsetByte + inputSequenceSizeByte
            
        else:
            # Previous Transaction Hash
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            prevOutputHashOffset = (startingPrevOutputHashOffsetByte - 1) * 2
            prevOutputHashOffsetSize = prevOutputHashSizeByte * 2
            prevOutputHash = transaction[prevOutputHashOffset : prevOutputHashOffset + prevOutputHashOffsetSize]
            
            # Previous Transaction Hash Index
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            prevOutputHashIndexOffset = (startingPrevOutputHashIndexOffsetByte - 1) * 2
            prevOutputHashIndexOffsetSize = prevOutputHashIndexSizeByte * 2
            prevOutputHashIndex = transaction[prevOutputHashIndexOffset : prevOutputHashIndexOffset + prevOutputHashIndexOffsetSize]
            
            # Input Script Length
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte = 1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            inputScriptOffset = (startingInputScriptOffsetByte - 1) * 2
            inputScriptOffsetSize = inputScriptSizeByte * 2        
            inputScript = transaction[inputScriptOffset : inputScriptOffset + inputScriptOffsetSize]
            
            # Input Sequence 
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            inputSequenceOffset = (startingInputSequenceOffsetByte - 1) * 2
            inputSequenceOffsetSize = inputSequenceSizeByte * 2        
            inputSequence = transaction[inputSequenceOffset : inputSequenceOffset + inputSequenceOffsetSize]
            
            transactionInput = (prevOutputHash + 
                                prevOutputHashIndex +
                                inputScriptLength + 
                                inputScript + 
                                inputSequence)
                                
            transactionInputList.append(transactionInput)
            startingInputSectionOffsetByte = (startingInputSequenceOffsetByte + inputSequenceSizeByte)

    return transactionInputList
    
def getInputSection(transaction, inputIndex):

    inputCount = int(getInputCount(transaction), 16)
    print inputCount
    
    if inputCount <= inputIndex:
        return "Input Index Error"
    
    startingInputSectionOffsetByte = 0
    startingPrevOutputHashOffsetByte = 0
    startingPrevOutputHashIndexOffsetByte = 0
    startingInputScriptLengthOffsetByte = 0
    startingInputScriptOffsetByte = 0
    startingInputSequenceOffsetByte = 0

    transactionInputSection = []

    for x in xrange(0, inputIndex + 1):
    
        if x == 0:
            startingInputSectionOffsetByte = 6
            # Previous Transaction Hash
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            prevOutputHashOffset = (startingPrevOutputHashOffsetByte - 1) * 2
            prevOutputHashOffsetSize = prevOutputHashSizeByte * 2
            prevOutputHash = transaction[prevOutputHashOffset : prevOutputHashOffset + prevOutputHashOffsetSize]
            
            # Previous Transaction Hash Index
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            prevOutputHashIndexOffset = (startingPrevOutputHashIndexOffsetByte - 1) * 2
            prevOutputHashIndexOffsetSize = prevOutputHashIndexSizeByte * 2
            prevOutputHashIndex = transaction[prevOutputHashIndexOffset : prevOutputHashIndexOffset + prevOutputHashIndexOffsetSize]
            
            # Input Script Length
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte = 1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            inputScriptOffset = (startingInputScriptOffsetByte - 1) * 2
            inputScriptOffsetSize = inputScriptSizeByte * 2        
            inputScript = transaction[inputScriptOffset : inputScriptOffset + inputScriptOffsetSize]
                                      
            # Input Sequence 
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            inputSequenceOffset = (startingInputSequenceOffsetByte - 1) * 2
            inputSequenceOffsetSize = inputSequenceSizeByte * 2        
            inputSequence = transaction[inputSequenceOffset : inputSequenceOffset + inputSequenceOffsetSize]
            
            transactionInputSection = (prevOutputHash + 
                                       prevOutputHashIndex +
                                       inputScriptLength + 
                                       inputScript + 
                                       inputSequence)
            
            startingInputSectionOffsetByte = startingInputSequenceOffsetByte + inputSequenceSizeByte
            
        else:
            # Previous Transaction Hash
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            prevOutputHashOffset = (startingPrevOutputHashOffsetByte - 1) * 2
            prevOutputHashOffsetSize = prevOutputHashSizeByte * 2
            prevOutputHash = transaction[prevOutputHashOffset : prevOutputHashOffset + prevOutputHashOffsetSize]
            
            # Previous Transaction Hash Index
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            prevOutputHashIndexOffset = (startingPrevOutputHashIndexOffsetByte - 1) * 2
            prevOutputHashIndexOffsetSize = prevOutputHashIndexSizeByte * 2
            prevOutputHashIndex = transaction[prevOutputHashIndexOffset : prevOutputHashIndexOffset + prevOutputHashIndexOffsetSize]
            
            # Input Script Length
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte = 1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            inputScriptOffset = (startingInputScriptOffsetByte - 1) * 2
            inputScriptOffsetSize = inputScriptSizeByte * 2        
            inputScript = transaction[inputScriptOffset : inputScriptOffset + inputScriptOffsetSize]
            
            # Input Sequence 
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            inputSequenceOffset = (startingInputSequenceOffsetByte - 1) * 2
            inputSequenceOffsetSize = inputSequenceSizeByte * 2        
            inputSequence = transaction[inputSequenceOffset : inputSequenceOffset + inputSequenceOffsetSize]
            
            transactionInputSection = (prevOutputHash + 
                                       prevOutputHashIndex +
                                       inputScriptLength + 
                                       inputScript + 
                                       inputSequence)
            
            startingInputSectionOffsetByte = (startingInputSequenceOffsetByte + inputSequenceSizeByte)

    return transactionInputSection
    