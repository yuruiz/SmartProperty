import generateAddress, publicKey, configUtils
import time, datetime

CREDITOR_OWNERSHIP_LOG_FILE = "creditorOwnershipLog.txt"

HASH_TYPE = ["01",
            ]

PRIVATE_KEY_LIST = ["fd3b98af3c17d6d29fed6f97c6f03519bbcd35a29fea632e0400090f2af61278",
                    ]

PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST = ["mjiu4Jwr48SzMhEvT6aaiNwPekPksXNRmf",
                                                   ]
# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
PREVIOUS_TRANSACTION_OUTPUT_INDEX_LIST = [0,
                                          ]

PREVIOUS_TRANSACTION_HASH_LIST = ["1646cd77cc90849e3cada74270a5103b4886535624f2e0bb8a765a675ef7bc3e",
                                  ]

INPUT_SATOSHIS = 499983620

INITIAL_OUTPUT_TRANSACTIONS = 3
SINGLE_OUTPUT_TRANSACTION_AMOUNT = 5460

TRANSFER_BACK_AMOUNT = INPUT_SATOSHIS - (INITIAL_OUTPUT_TRANSACTIONS * SINGLE_OUTPUT_TRANSACTION_AMOUNT)

ownershipKey = generateAddress.privKey
ownershipPublicAddress = publicKey.getPublicAddress(ownershipKey, "test")

file = open(CREDITOR_OWNERSHIP_LOG_FILE, "a")
getTimeNow = time.time()
getFormattedTime = datetime.datetime.fromtimestamp(getTimeNow).strftime('%Y-%m-%d %H:%M:%S')
file.write(getFormattedTime + ": " + ownershipKey + "," + ownershipPublicAddress)
file.write("\n")
file.close()

DESTINATION_SATOSHIS_LIST = []
DESTINATION_PUBLIC_ADDRESS_LIST = []

DESTINATION_SATOSHIS_LIST.append(TRANSFER_BACK_AMOUNT)
DESTINATION_PUBLIC_ADDRESS_LIST.append(PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST[0])

for outputIndex in xrange(0, INITIAL_OUTPUT_TRANSACTIONS):
    DESTINATION_SATOSHIS_LIST.append(SINGLE_OUTPUT_TRANSACTION_AMOUNT)
    DESTINATION_PUBLIC_ADDRESS_LIST.append(ownershipPublicAddress)

# New Transaction Inputs
# List of
#    - Previous Transaction Hash
#    - Previous Transaction Output Index
#    - Previous Transaction Output Public Address
#        - Signature will be calculate from this address
#        - This is the address where you are transferring the Bitcoin from
#        - You must have the private key to this public address
assert(len(PREVIOUS_TRANSACTION_OUTPUT_PUBLIC_ADDRESS_LIST) == len(HASH_TYPE) == len(PRIVATE_KEY_LIST)\
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

config = configUtils.TransactionConfiguration(PRIVATE_KEY_LIST,
                                              NEW_TRANSACTION_INPUT,
                                              NEW_TRANSACTION_OUTPUT,
                                              HASH_TYPE
                                              )


