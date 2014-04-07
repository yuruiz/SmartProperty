

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
TESTNET3_PEER_HOST_IP = "198.50.215.81"
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
                    #"f19c523315891e6e15ae0608a35eec2e00ebd6d1984cf167f46336dabd9b2de4", 
                    #"d3484a00246dee175bfc092b7ed7bb3067ec78083035d9cfd34cec06f40c4cc2"
                    ]

# The transaction hash of the previous 
PREVIOUS_TRANSACTION_HASH_LIST = ["71c32e01e653e4940daa173f14218d660e5b1532ccf25c6c84312efa730812f4", #4.99
                                  #"a94b239a16e923df5e4a447062f9c71a9d5cfb765086d593caf41aa01abb2441",
                                  ] #.6.9


# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          #0
                                          ]

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
                                                   ]


# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC
DESTINATION_SATOSHIS_LIST = [499000000]

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
                         #[PREVIOUS_TRANSACTION_HASH_LIST[1],
                         # PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST[1],
                         # PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[1],
                         # PRIVATE_KEY_LIST[1]],
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
