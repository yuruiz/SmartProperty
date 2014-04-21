

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
            #'81'
            ]


PRIVATE_KEY_LIST = ["fd3b98af3c17d6d29fed6f97c6f03519bbcd35a29fea632e0400090f2af61278",
                    #"e6758ad160b894567fcc1d9f7038cd19b92592a13768363c4c8d759b61a34332"
                    ]


PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["mjiu4Jwr48SzMhEvT6aaiNwPekPksXNRmf",
                                                   #"mjiu4Jwr48SzMhEvT6aaiNwPekPksXNRmf"
                                                  #"n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
                                                   ]


# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                         # 0
                                          ]

# The transaction hash of the previous
PREVIOUS_TRANSACTION_HASH_LIST = ["5eb23f5bd71b6f9fe4f2e55c1a3b9ed16a68b9bee917f86bac94002508a0ed46",  # 1.2
                                  #"" # 10
                                  ]

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC


DESTINATION_SATOSHIS_LIST = [120000000,
                             #50000000,
                             #50000000
                             ]

DESTINATION_PUBLIC_ADDRESS_LIST = ["mk9EgeaLZ26AL4Zb2hjgaU2mTLbYFUU8Ni",
                                   #"mk9EgeaLZ26AL4Zb2hjgaU2mTLbYFUU8Ni",
                                   #"msACxpHYZ2H8JAxuk8CSudG3Cn6ETYSE2e"
                                   ]


# New Transaction Inputs
# List of
#    - Previous Transaction Hash
#    - Previous Transaction Output Index
#    - Previous Transaction Output Public Address
#        - Signature will be calculate from this address
#        - This is the address where you are transferring the Bitcoin from
#        - You must have the private key to this public address

assert(len(PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST) == len(hashtype) == len(PRIVATE_KEY_LIST)\
      == len(PREVIOUS_TRANSACTION_HASH_LIST) == len(PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST))

NEW_TRANSACTION_INPUT = []
for x in xrange(0,len(PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST)):
    NEW_TRANSACTION_INPUT.append([PREVIOUS_TRANSACTION_HASH_LIST[x],
                                  PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST[x],
                                  PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[x],
                                  PRIVATE_KEY_LIST[x]])

# New Transaction Outputs
# List of
#    - Satoshis (Bitcoin Denominations <=> 100,000,000 -> 1 BTC)
#    - New Transaction Output Public Address
#        - This is the address where you are transferring the Bitcoin to

assert(len(DESTINATION_SATOSHIS_LIST) == len(DESTINATION_PUBLIC_ADDRESS_LIST))
NEW_TRANSACTION_OUTPUT = []
for x in xrange(0,len(DESTINATION_SATOSHIS_LIST)):
    NEW_TRANSACTION_OUTPUT.append([DESTINATION_SATOSHIS_LIST[x],
                                   DESTINATION_PUBLIC_ADDRESS_LIST[x]])

