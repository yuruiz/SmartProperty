import socket
import message
import transaction
import txnUtils
import configuration

print configuration.NETWORK_ADDRESS

versionMessage = message.buildVersionMessage(configuration.NETWORK_MAGIC, configuration.NETWORK_PORT)

# Loading configuration
transmissionConfig = configuration.config

# Builds signed transaction with specified private key and transaction input and outputs
stxn = transaction.buildSignedTransaction(transmissionConfig.privateKeyList,
                                          transmissionConfig.inputTransactionList,
                                          transmissionConfig.outputTransactionList,
                                          transmissionConfig.hashType
                                          )

#stxn = '0100000001124308fc31ae0171d9f811dc443f1543c6e7a4bdc44e18af3012141c6ac66970010000008a4730440220309a62d368eec1ac1222683be5998c119b2664a6111eedf43c8650bffa5ac99602201690c82740bf99348c0b3df183d587a61a73de89d9eb89cc69d2e22327c957cf014104e55500c1103d9d7b84fdd7635071d29cde6e35e5d242a1dbaf4ede0d3cafb57f63c64bb18cabb7cd3c5b5a705861be5d9344efcf95c2ca2724e116c582209e8fffffffff030065cd1d000000001b76a9142e22cae79f1725eacbdeda8a1e3cf22217c1ba3588acad510065cd1d000000001b76a9142e22cae79f1725eacbdeda8a1e3cf22217c1ba3588acad510065cd1d000000001b76a9142e22cae79f1725eacbdeda8a1e3cf22217c1ba3588acad5100000000'

transactionHash = txnUtils.getTransactionHash(stxn)

print (str(stxn))
print (str(transactionHash))
# Verifies the signed transaction, any error here will abort the socket creation
# txnUtils.verifyTxnSignature(stxn)

# Construct the transaction message to be sent from the transaction message
transactionMessage = message.buildTransactionMessage(configuration.NETWORK_MAGIC, stxn)

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
sock.send(message.buildInventoryMessage(configuration.NETWORK_MAGIC, [(1, stxn.decode("hex"))]))
sock.recv(1000)

# Sends the actual transaction message
sock.send(transactionMessage)
sock.recv(1000)
