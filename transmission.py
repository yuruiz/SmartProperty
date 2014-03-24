import random
import struct
import time
import socket

import message
import msgUtils
import generateAddress
import transaction
import txnUtils

# Main Network Magic Value
MAIN_NETWORK_MAGIC = 0xD9B4BEF9

# TestNet3 Magic Value
TEST_NETWORK3_MAGIC = 0x0709110B

# Main Network Port Number
MAIN_NETWORK_PORT = 8333

# Test Network Port Number
TEST_NETWORK_PORT = 18333

# Peer Host IP, do nslookup of domains below to find IP
#    - MAINNET SEEDS: 
#        - bitseed.xf2.org
#        - dnsseed.bluematt.me
#        - dnsseed.bitcoin.dashjr.org
#    - TESTNET3 SEEDS: 
#        - testnet-seed.bitcoin.petertodd.org
#        - testnet-seed.bluematt.me
#MAINNET_PEER_HOST_IP = 
TESTNET3_PEER_HOST_IP = "46.105.173.28"
TESTNET3_PEER_HOST_IP = "24.247.20.162"

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)
sock.connect((TESTNET3_PEER_HOST_IP, TEST_NETWORK_PORT))


versionMessage = message.buildVersionMessage(TEST_NETWORK3_MAGIC, TEST_NETWORK_PORT)

stxn = transaction.buildSignedTransaction(generateAddress.privKey, 
                                          transaction.newTransactionInput, 
                                          transaction.newTransactionOutput)

txnUtils.verifyTxnSignature(stxn)
#print len(versionMessage)
#print len(stxn.decode("hex"))



transactionMessage = message.buildTransactionMessage(TEST_NETWORK3_MAGIC,stxn)


#sock.send(transactionMessage)

#print (''.join( [ "%02X " % ord( x ) for x in versionMessage ] ).strip())

#sock.send(transactionMessage)
sock.send(versionMessage)

sock.recv(1000)
sock.recv(1000)

#print (''.join( [ "%02X " % ord( x ) for x in transactionMessage ] ).strip())


sock.send(message.buildInventoryMessage(TEST_NETWORK3_MAGIC, [(1,stxn.decode("hex"))]))

sock.recv(1000)

sock.send(transactionMessage)

#sock.recv(1000)
'''
sock.close()
'''