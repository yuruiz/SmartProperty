

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

PRIVATE_KEY_LIST = ["d3484a00246dee175bfc092b7ed7bb3067ec78083035d9cfd34cec06f40c4cc2",
                    "fd3b98af3c17d6d29fed6f97c6f03519bbcd35a29fea632e0400090f2af61278"
                    ]


# The transaction hash of the previous
PREVIOUS_TRANSACTION_HASH_LIST = ["c53ad48b65d4cd085f61e1646b63bd3afe22409ba63ac03bc0368a8710db2acd",  # 17
                                  "7111f64e39114e76958971f350216d4922a34aa83b620ccba16bea11f8a47ba8" # 1.3
                                  ]  

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          0
                                          ]


PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["mtBRkCj8GSc5kPYqhLdS4ahaTMXfk5trq1",
                                                   "mjiu4Jwr48SzMhEvT6aaiNwPekPksXNRmf"
                                                   #"    "
                                                   ]

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC

DESTINATION_SATOSHIS_LIST = [500000000,
                             300000000,
                             300000000,
                             500000000]

DESTINATION_PUBLIC_ADDRESS_LIST = ["mhZrFh3PaxfTEt1StR7oLHW7rPboyLjFs3",
                                   "n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX",
                                   "myqGc9SzpYm3qFU83UNhMZ8mjCFqzmGi2x",
                                   "mhZrFh3PaxfTEt1StR7oLHW7rPboyLjFs3"
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
     DESTINATION_PUBLIC_ADDRESS_LIST[2]],
    [DESTINATION_SATOSHIS_LIST[3],
     DESTINATION_PUBLIC_ADDRESS_LIST[3]]
    #[DESTINATION_SATOSHIS_LIST[1],
    # DESTINATION_PUBLIC_ADDRESS_LIST[1]],
]
