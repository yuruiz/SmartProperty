import hashlib
import random
import struct
import time
import socket
import unittest

from Crypto.Hash import SHA256
from Crypto.Random import random

import utils

#https://en.bitcoin.it/wiki/Protocol_specification#version


# Main Network Port Number
MAIN_NETWORK_PORT = 8333

# Test Network Port Number
TEST_NETWORK_PORT = 18333

def buildMessage(networkType, command, payload):
    
    singleSHA256_Payload = SHA256.new(payload).digest()
    doubleSHA256_Payload = SHA256.new(singleSHA256_Payload).digest()
    payloadChecksum = doubleSHA256_Payload[0:4]
    
    #build
    
    
    message = struct.pack('<L12sL4s', networkType, command, len(payload), payloadChecksum) + payload
    
    #print payload
    #print len(payload)
    return message

def buildVersionMessage(networkType, portNumber):
    
    # This format of Network Address applies to version message because it
    #    does not have the timestamp in the prefix
    def formatVersionNetworkAddress(timestamp, service, ipAddressV4, portNumber):
        ipAddressV4ByteString = ("".join([ ("%02x" % int(octet)) for octet in ipAddressV4.split(".") ])).decode("hex")
        #ipAddressV4ByteString = "".join([ chr(int(octet)) for octet in ipAddressV4.split(".") ])
        #print ipAddressV4ByteString
        
        
        networkAddress = []
        networkAddress.append(struct.pack("<Q", 
                                          service))
        networkAddress.append(struct.pack("<10sH", 
                                          "", 
                                          0xffff))
        networkAddress.append(struct.pack(">4sH", 
                                          ipAddressV4ByteString, 
                                          portNumber))
        
        formattedNetworkAddress = "".join(networkAddress)
        
        return (formattedNetworkAddress)
  
    # Version: Identifies protocol version being used by the node
    protocolVersion = 70001
    #print protocolVersion.encode("hex")
    # Service: 1 - NODE_NETWORK
    service = 1
    
    timestamp = int(time.time())
    addressReceived = formatVersionNetworkAddress(timestamp, service, "127.0.0.1", portNumber)
    addressFrom = formatVersionNetworkAddress(timestamp, service, "127.0.0.1", portNumber)
    nonce = random.getrandbits(64)
    userAgent = utils.varstr("")
    startHeight = 0 
    relay = True
    
    versionMessagePayload = []
    versionMessagePayload.append(struct.pack("<LQQ", 
                                             protocolVersion,
                                             service,
                                             timestamp))
    versionMessagePayload.append(struct.pack("<26s26s", 
                                             addressReceived,
                                             addressFrom))
    versionMessagePayload.append(struct.pack("<Q",nonce))
    versionMessagePayload.append(struct.pack("<s",userAgent))
    versionMessagePayload.append(struct.pack("<L",startHeight))
    versionMessagePayload.append(struct.pack("<?",relay))
    
    formattedVersionMessagePayload = "".join(versionMessagePayload)    
    
    
    #print versionMessagePayload
    '''
    struct.pack('<LQQ26s26sQsL?', protocolVersion, service, timestamp, addressReceived,
        addressFrom, nonce, userAgent, startHeight, relay)
    '''
    return buildMessage(networkType, "version", formattedVersionMessagePayload)

def buildInventoryMessage(networkType, inventory):
    invHashes = []
    for item in inventory:
        invHashes.append(struct.pack("<L", item[0]) + 
            hashlib.sha256(hashlib.sha256(item[1]).digest()).digest()[::-1])
    return buildMessage(networkType, "inv", utils.varint(len(invHashes)) + "".join(invHashes))

def buildTransactionMessage(networkType, transactionPayload):
    transactionPayload = transactionPayload.decode("hex")
    transactionMessage = buildMessage(networkType, "tx", transactionPayload)
    
    #print transactionMessage
    
    return transactionMessage
