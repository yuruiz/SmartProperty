import socket
import message
import transaction
import txnUtils
import configuration

import deserialize
import ContractGeneration

import _tempConfig

def signedTxnConfig(config):
    
    # Builds signed transaction with specified private key and transaction input and outputs
    stxn = transaction.buildSignedTransaction(config.privateKeyList,
                                              config.inputTransactionList,
                                              config.outputTransactionList,
                                              config.hashType
                                              )
    
    return stxn

def sendTransmission(signedTransaction):
    versionMessage = message.buildVersionMessage(configuration.NETWORK_MAGIC, configuration.NETWORK_PORT)
    
    # Construct the transaction message to be sent from the transaction message
    transactionMessage = message.buildTransactionMessage(configuration.NETWORK_MAGIC, signedTransaction)
    
    # Builds the socket connection with the specified IP address and port number
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(10)
    sock.connect((configuration.NETWORK_ADDRESS, configuration.NETWORK_PORT))
    
    # Initialize the transaction transmission with server starting with the version message
    sock.send(versionMessage)
    
    # The server will reply with two messages corresponding to the sent version message
    #    - 1st Message: Server's Version
    #    - 2nd Message: Server's Version Acknowledgment
    sock.recv(1000)
    sock.recv(1000)
    
    # Prepares the server to receive the Transaction Message
    sock.send(message.buildInventoryMessage(configuration.NETWORK_MAGIC, [(1, signedTransaction.decode("hex"))]))
    sock.recv(1000)
    
    # Sends the actual transaction message
    sock.send(transactionMessage)
    sock.recv(1000)

# Loading configuration
#transmissionConfig = Configuration.config
transmissionConfig = _tempConfig.config
signedTxn = signedTxnConfig(transmissionConfig)

print signedTxn

result = txnUtils.getInputSectionAll(signedTxn)  

print result





'''
transactionHash = txnUtils.getTransactionHash(signedTxn)
transactionHashList = []
transactionHashIndexList = []


transactionOutputCount = transmissionConfig.getOutputTransactionsCount()

for x in xrange(0, transactionOutputCount):
    transactionHashList.append(transactionHash)
    transactionHashIndexList.append(x)
    
ownershipPrivateKey = "e3e8c85c7a97289107def568ad08bf08249c6a23cb727b2af538a796a5ce3fa1"
ownershipPublicKey = "mth3cd1j8957sFTo2TzAH29C82aQ9NezkN"

OwnerWalleptPubAddress = "mqSBwZkvZJvxgJvCcbFcFRz3iuEouHE3Ub"

TempKeyPublicAddressList = ["n4Tg3AStAAxiCGM4YQhm2iEcSoS1C9ZiJp",
                            "n2CRV3tZg9DDzG3Z1HWnE5dYhdTMxzVuEN",
                            "n3GmEYMgf3XRTVuoi7gwcuc5smxHmMrDiB",
                            ]

Nmonth = 3

Timelist = ["032014",
            "042014",
            "052014",
            ]

Payment = [100000000,
           100000000,
           100000000,
           ]

contractList = ContractGeneration.GenerateTxList(transactionHashList, 
                                                 transactionHashIndexList, 
                                                 ownershipPrivateKey, 
                                                 ownershipPublicKey, 
                                                 OwnerWalleptPubAddress, 
                                                 TempKeyPublicAddressList, 
                                                 Nmonth, 
                                                 Timelist, 
                                                 Payment
                                                 )    

print contractList
'''
