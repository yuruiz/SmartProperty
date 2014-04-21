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