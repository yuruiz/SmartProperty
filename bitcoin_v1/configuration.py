

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
#TESTNET3_PEER_HOST_IP = "188.226.176.87"
TESTNET3_PEER_HOST_IP = "testnet-seed.bitcoin.petertodd.org"

selectNetwork = "test"

if selectNetwork == "main":
    NETWORK_MAGIC = MAIN_NETWORK_MAGIC
    NETWORK_PORT = MAIN_NETWORK_PORT
    NETWORK_ADDRESS = MAINNET_PEER_HOST_IP
else:
    NETWORK_MAGIC = TEST_NETWORK3_MAGIC
    NETWORK_PORT = TEST_NETWORK_PORT
    NETWORK_ADDRESS = TESTNET3_PEER_HOST_IP

hashtype = ['01',
            '81'
            ]

PRIVATE_KEY_LIST = ["58d0987eb71b473ce41059fdabe6967cffeaf14e6e3a9d036ee1b0fd83d9b80a",
                    "4207f3eb1177e64f358694d954f6be47692a87b9a552bedc26ce1986735d25cd"
                    ]

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["miy7SPbChbUK9Wy99GPZZgxYiK3ZsVgJKZ",
                                                   "mpzoAtjbX6sDZUny3BVSnbQS5Gvhs9vF4E"
                                                  #"n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
                                                   ]

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          1
                                          ]

# The transaction hash of the previous
PREVIOUS_TRANSACTION_HASH_LIST = ["b13b56946175584049409b0715bf9fe3527b524d3438ee118eac67d07b3ff68c",  # 5
                                  "b13b56946175584049409b0715bf9fe3527b524d3438ee118eac67d07b3ff68c" # 10
                                  ]

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC

DESTINATION_SATOSHIS_LIST = [500000000,
                             500000000,
                             500000000]

DESTINATION_PUBLIC_ADDRESS_LIST = ["mp3pCv8oWH1sNrDp3SPPhg8SwRLtNnXnD5",
                                   "mk9EgeaLZ26AL4Zb2hjgaU2mTLbYFUU8Ni",
                                   "msACxpHYZ2H8JAxuk8CSudG3Cn6ETYSE2e"
                                   ]


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
     PRIVATE_KEY_LIST[1]]
]

# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to
NEW_TRANSACTION_OUTPUT = [
    [DESTINATION_SATOSHIS_LIST[0],
     DESTINATION_PUBLIC_ADDRESS_LIST[0]],
    [DESTINATION_SATOSHIS_LIST[1],
     DESTINATION_PUBLIC_ADDRESS_LIST[1]],
    [DESTINATION_SATOSHIS_LIST[2],
     DESTINATION_PUBLIC_ADDRESS_LIST[2]]
]
