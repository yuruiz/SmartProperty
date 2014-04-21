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
    
    for x in xrange(0, inputIndexOffset + 1):
    
        startingInputSectionOffsetByte = 6
    
        if inputIndexOffset == 0:
            startingInputSectionOffsetByte = 6
        else:
            startingInputSectionOffsetByte = 6
            
            startingPrevOutputHashOffsetByte = startingInputSectionOffsetByte
            prevOutputHashSizeByte = 32
            startingPrevOutputHashIndexOffsetByte = startingPrevOutputHashOffsetByte + prevOutputHashSizeByte
            prevOutputHashIndexSizeByte = 4
            
            startingInputScriptLengthOffsetByte = startingPrevOutputHashIndexOffsetByte + prevOutputHashIndexSizeByte
            inputScriptLengthSizeByte =1
            inputScriptLengthOffset = (startingInputScriptLengthOffsetByte - 1) * 2
            inputScriptLengthOffsetSize = inputScriptLengthSizeByte * 2
            inputScriptLength = transaction[inputScriptLengthOffset : inputScriptLengthOffset + inputScriptLengthOffsetSize]
            
            print inputScriptLength
            
            # Input ScriptSig 
            startingInputScriptOffsetByte = startingInputScriptLengthOffsetByte + inputScriptLengthSizeByte
            inputScriptSizeByte = getInputScriptSizeByte(inputScriptLength)
            
            startingInputSequenceOffsetByte = startingInputScriptOffsetByte + inputScriptSizeByte
            inputSequenceSizeByte = 4
            
            startingInputSectionOffsetByte += (startingInputSequenceOffsetByte + inputSequenceSizeByte)
        
            

    return startingInputSectionOffsetByte

def getInputSection(transaction, inputCount=None, inputIndexOffset=None):

    '''
    if inputCount:
        for input in xrange(0, inputCount):
            
    '''
     
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
    inputScriptLengthSizeByte =1
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
    
    
    startingInputSectionOffsetByte = startingInputSequenceOffsetByte + inputSequenceSizeByte   

    
    return startingInputSectionOffsetByte
    
    '''
    
    
    inputScriptLengthSizeByte = 1
    
    
    inputSectionSizeByte = (prevOutputHashSizeByte + 
                            prevOutputHashIndexSizeByte +
                            inputScriptLengthSizeByte +
                            sequenceSizeByte)
    
    startingInputSectionOffset = (startingInputSectionOffsetByte - 1) * 2
    
    scriptSize = 
    
    inputSectionSize = inputSectionSizeByte * 2 
    
    for 
    
    '''
    
    
    