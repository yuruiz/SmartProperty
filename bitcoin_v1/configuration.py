

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
#TESTNET3_PEER_HOST_IP = "95.211.121.211"
TESTNET3_PEER_HOST_IP = "testnet-seed.bitcoin.petertodd.org"

selectNetwork = "test"

if selectNetwork == "main":
    NETWORK_MAGIC = MAIN_NETWORK_MAGIC
    NETWORK_PORT = MAIN_NETWORK_PORT
    NETWORK_ADDRESS = MAINNET_PEER_HOST_IP
else: 
    NETWORK_MAGIC =  TEST_NETWORK3_MAGIC
    NETWORK_PORT = TEST_NETWORK_PORT
    NETWORK_ADDRESS = TESTNET3_PEER_HOST_IP

PRIVATE_KEY = "c9b74446725c99d429848f8093a347976784d133efec971343be004d5f9c7fdc"

# The transaction hash of the previous 
PREVIOUS_TRANSACTION_HASH = "e1caff9c55ffe85a070ff2e1d37eed2cb9a491c3bf8b9f4900acc35cd05474ec"

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX = 0

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC
DESTINATION_SATOSHIS_1 = 55000000
DESTINATION_SATOSHIS_2 = 40000000

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS = "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
DESTINATION_PUBLIC_ADDRESS_1 = "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
DESTINATION_PUBLIC_ADDRESS_2 = "mtBRkCj8GSc5kPYqhLdS4ahaTMXfk5trq1"

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
                          PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS],
                         ]

# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to
NEW_TRANSACTION_OUTPUT = [
                          [DESTINATION_SATOSHIS_1,
                           DESTINATION_PUBLIC_ADDRESS_1],
                          [DESTINATION_SATOSHIS_2,
                           DESTINATION_PUBLIC_ADDRESS_2],
                          ]