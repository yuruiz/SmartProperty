import socket
import message
import transaction
import txnUtils
import configuration

print configuration.NETWORK_ADDRESS

versionMessage = message.buildVersionMessage(configuration.NETWORK_MAGIC, configuration.NETWORK_PORT)

# Builds signed transaction with specified private key and transaction input and outputs 
stxn = transaction.buildSignedTransaction(configuration.PRIVATE_KEY_LIST, 
                                          configuration.NEW_TRANSACTION_INPUT, 
                                          configuration.NEW_TRANSACTION_OUTPUT)

# Verifies the signed transaction, any error here will abort the socket creation
#txnUtils.verifyTxnSignature(stxn)

# Construct the transaction message to be sent from the transaction message
transactionMessage = message.buildTransactionMessage(configuration.NETWORK_MAGIC,stxn)

# Builds the socket connection with the specified IP address and port number
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(30)
sock.connect((configuration.NETWORK_ADDRESS, configuration.NETWORK_PORT))

# Initialize the transaction transmission with server starting with the version message
sock.send(versionMessage)

# The server will reply with two messages corresponding to the sent version message
#    - 1st Message: Server's Version
#    - 2nd Message: Server's Version Acknowledgment
sock.recv(1000)
sock.recv(1000)

# Prepares the server to receive the Transaction Message
sock.send(message.buildInventoryMessage(configuration.NETWORK_MAGIC, [(1,stxn.decode("hex"))]))
sock.recv(1000)

# Sends the actual transaction message
sock.send(transactionMessage)
sock.recv(1000)
sock.recv(1000)
sock.recv(1000)
sock.recv(1000)