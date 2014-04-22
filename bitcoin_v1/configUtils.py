PREV_TRANSACTION_HASH_OFFSET = 0
PREV_TRANSACTION_HASH_LIST_OFFSET = 1

class TransactionConfiguration(object):
    privateKeyList = []
    inputTransactionList = []
    outputTransactionList = []
    hashType = []
        
    # "Constructor" - It's actually an initializer 
    def __init__(self, privateKeyList, 
                 inputTransactionList, 
                 outputTransactionList,
                 hashType):
        
        self.privateKeyList = privateKeyList
        self.inputTransactionList = inputTransactionList
        self.outputTransactionList = outputTransactionList
        self.hashType = hashType
        
    def getPreviousTransactionsHashList(self):
        
        previousTransactionsHashList = []
        for inputTransaction in self.inputTransactionList:
            previousTransactionsHashList.append(inputTransaction[PREV_TRANSACTION_HASH_OFFSET])
        
        return previousTransactionsHashList
    
    
    def getPreviousTransactionsHashIndexList(self):
        
        previousTransactionsHashIndexList = []
        for inputTransaction in self.inputTransactionList:
            previousTransactionsHashIndexList.append(inputTransaction[PREV_TRANSACTION_HASH_LIST_OFFSET])
        
        return previousTransactionsHashIndexList
    
    def getOutputTransactionsCount(self):
        
        count = len(self.outputTransactionList)
        
        return count