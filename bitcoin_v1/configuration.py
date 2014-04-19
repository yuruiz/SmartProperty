

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
            '01'
            ]

PRIVATE_KEY_LIST = ["d3484a00246dee175bfc092b7ed7bb3067ec78083035d9cfd34cec06f40c4cc2",
                    "e97174e793c7524c0a68eda86458682bd9c5510e6e3614cc5cecdffe966c925b"
                    ]


# The transaction hash of the previous
PREVIOUS_TRANSACTION_HASH_LIST = ["3f2ff2c975e8997bd6f71870e2b306275d7da9b2da1137bfad5ddb2923379029",  # 17
                                  "1b73fe8e54a21e84d351ff947e073e11980086a72ace59c13a206f7b9978e34c" # .1
                                  ]

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          1
                                          ]


PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["mtBRkCj8GSc5kPYqhLdS4ahaTMXfk5trq1",
                                                   "mhZrFh3PaxfTEt1StR7oLHW7rPboyLjFs3"
                                                  #"n2SQWnkE8iSauDnTYd3i3NtrTBngT4DboX"
                                                   ]

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC

DESTINATION_SATOSHIS_LIST = [1650000000]

DESTINATION_PUBLIC_ADDRESS_LIST = ["myqGc9SzpYm3qFU83UNhMZ8mjCFqzmGi2x"
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
assert(len(DESTINATION_SATOSHIS_LIST) == len(DESTINATION_SATOSHIS_LIST))
NEW_TRANSACTION_OUTPUT = []
for x in xrange(0,len(DESTINATION_SATOSHIS_LIST)):
  NEW_TRANSACTION_OUTPUT.append([DESTINATION_SATOSHIS_LIST[x],
       DESTINATION_PUBLIC_ADDRESS_LIST[x]])
