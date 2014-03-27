

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

PRIVATE_KEY_LIST = ["c9b74446725c99d429848f8093a347976784d133efec971343be004d5f9c7fdc", 
                    "c9b74446725c99d429848f8093a347976784d133efec971343be004d5f9c7fdc",
                    "c9b74446725c99d429848f8093a347976784d133efec971343be004d5f9c7fdc"]

# The transaction hash of the previous 
PREVIOUS_TRANSACTION_HASH_LIST = ["415ac093bb4611a2cf2ff34c673afdb20d9b8c18eb355d1ab5d1f22e0da38603", #6.8
                                  "1df492ae7b95d6b1fe432a2c5ebf0acba8b5c861653bfc2f9ef6663bf239ddcc", #.55
                                  "94623ec9794b22bb20f86c16585ce0ea24f2f5f63970bc97e631b2096dd6f0bd"] #.1


# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          0,
                                          1]

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX",
                                                   "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX",
                                                   "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"]


# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC
DESTINATION_SATOSHIS_LIST = [680000000,
                             55000000,
                             10000000]

DESTINATION_PUBLIC_ADDRESS_LIST = ["myqGc9SzpYm3qFU83UNhMZ8mjCFqzmGi2x"]


# New Transaction Inputs
# List of
#    - Previous Transaction Hash
#    - Previous Transaction Output Index
#    - Previous Transaction Output Public Address
#        - Signature will be calculate from this address
#        - This is the address where you are transferring the Bitcoin from
#        - You must have the private key to this public address
NEW_TRANSACTION_INPUT = [
                         [PREVIOUS_TRANSACTION_HASH_LIST[0],
                          PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST[0],
                          PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[0],
                          PRIVATE_KEY_LIST[0]],
                         [PREVIOUS_TRANSACTION_HASH_LIST[1],
                          PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST[1],
                          PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[1],
                          PRIVATE_KEY_LIST[1]],
                         [PREVIOUS_TRANSACTION_HASH_LIST[2],
                          PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST[2],
                          PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[2],
                          PRIVATE_KEY_LIST[2]],
                         ]

# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to
NEW_TRANSACTION_OUTPUT = [
                          [DESTINATION_SATOSHIS_LIST[0],
                           DESTINATION_PUBLIC_ADDRESS_LIST[0]],
                          #[DESTINATION_SATOSHIS_LIST[1],
                          # DESTINATION_PUBLIC_ADDRESS_LIST[1]],
                          ]
