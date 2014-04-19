

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

PRIVATE_KEY_LIST = ["b48f16ae18643c3c20892ca21389744f53ab66474e007c670e59ceba9ed05f72",
                    "4207f3eb1177e64f358694d954f6be47692a87b9a552bedc26ce1986735d25cd"
                    ]

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["mp3pCv8oWH1sNrDp3SPPhg8SwRLtNnXnD5",
                                                   "mpzoAtjbX6sDZUny3BVSnbQS5Gvhs9vF4E"
                                                  #"n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
                                                   ]

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [1,
                                          0
                                          ]

# The transaction hash of the previous
PREVIOUS_TRANSACTION_HASH_LIST = ["242ab494e96cfb7bfab68cbdea805f2ead5e1c43be93d835ae283dbb883f29b2",  # 2.7
                                  "904330c0d98bbb19e10c98fb69a2fdc488b5db7b078220f3ded9ce57af1ab5c5" # 2.5
                                  ]

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC

DESTINATION_SATOSHIS_LIST = [200000000,
                             200000000,
                             100000000]

DESTINATION_PUBLIC_ADDRESS_LIST = ["miy7SPbChbUK9Wy99GPZZgxYiK3ZsVgJKZ",
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
