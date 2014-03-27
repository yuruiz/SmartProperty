

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
MAINNET_PEER_HOST_IP = "1.1.1.1"
TESTNET3_PEER_HOST_IP = "95.211.121.211"

selectNetwork = "test"

if selectNetwork == "main":
    NETWORK_MAGIC = MAIN_NETWORK_MAGIC
    NETWORK_PORT = MAIN_NETWORK_PORT
    NETWORK_ADDRESS = MAINNET_PEER_HOST_IP
else: 
    NETWORK_MAGIC =  TEST_NETWORK3_MAGIC
    NETWORK_PORT = TEST_NETWORK_PORT
    NETWORK_ADDRESS = TESTNET3_PEER_HOST_IP

PRIVATE_KEY = "d3484a00246dee175bfc092b7ed7bb3067ec78083035d9cfd34cec06f40c4cc2"

# The transaction hash of the previous 
PREVIOUS_TRANSACTION_HASH = "09b91ce9638a7a6dcd93a102a7f5dd0a21d947cb0d5d7e246d146fecef0615ff"

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX = 0

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC

DESTINATION_SATOSHIS_1 = 98000000
DESTINATION_SATOSHIS_2 = 20000000

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS = "mtBRkCj8GSc5kPYqhLdS4ahaTMXfk5trq1"
DESTINATION_PUBLIC_ADDRESS_1 = "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
#DESTINATION_PUBLIC_ADDRESS_2 = "mtBRkCj8GSc5kPYqhLdS4ahaTMXfk5trq1"


# New Transaction Inputs
# List of
#    - Previous Transaction Hash
#    - Previous Transaction Output Index
#    - Previous Transaction Output Public Address
#        - Signature will be calculate from this address
#        - This is the address where you are transferring the Bitcoin from
#        - You must have the private key to this public address
NEW_TRANSACTION_INPUT = [
                       [PREVIOUS_TRANSACTION_HASH,
                        PREVIOUS_TRANSACTION_OUTPUT_INDEX,
                        PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS
                        ],
                       ]



# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to
NEW_TRANSACTION_OUTPUT = [
                        [DESTINATION_SATOSHIS_1,
                         DESTINATION_PUBLIC_ADDRESS_1],
                        
                        ]
