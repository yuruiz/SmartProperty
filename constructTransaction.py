import ecdsa
import hashlib
import struct
import unittest

import utils
import keyUtils

# 4 bytes version
version = "01000000"

print version

# Number of Inputs for the New Transaction
newTransactionNumInput = "01"

print newTransactionNumInput

# Finds the Reverse Order of previousOutputTransactionHash
#previousOutputTransactionHash = "202ccf2aaae811e81a6392477210900582c8369a14ba9b72582b78b27edf62df"
previousOutputTransactionHash = "81b4c832d70cb56ff957589752eb4125a4cab78a25a8fc52d6a09e5bd4404d48"
reversePreviousOutputTransactionHash = previousOutputTransactionHash.decode('hex')[::-1].encode('hex')

#print previousOutputTransactionHash
print "\t" + reversePreviousOutputTransactionHash

# The Previous Output Transaction Index
#     - This indicates which of the outputs in the previous transaction
#       to send money from.
#     - 0: First, 1: Second, ...
previousOutputTransactionIndex = 0
previousOutputTransactionIndexHex = struct.pack('<L', previousOutputTransactionIndex).encode('hex')

print "\t" + previousOutputTransactionIndexHex


# scriptSig Length
#     '%02x' % len(scriptSig.decode('hex')) + 
print "\t<scriptSig Length>"

# scriptSig with Signature
#     scriptSig
print "\t<scriptSig with Signature>"

# Sequence is set to UNIT_MAX = "FFFFFFFF" because this will permanently lock this transaction
#     - Sequence is intended to work with Replacements, but Replacement is currently disabled
sequence = "ffffffff"
print "\t" + sequence

newTransactionOutputCount = 1
newTransactionOutputCountHex = "%02x" % newTransactionOutputCount
print newTransactionOutputCountHex

# BTC Denomination <=> Satoshis: 100,000,000 -> 1 BTC
#     - 0.40 BTC
#satoshis = 99900000
#satoshis = 40000000
satoshis = 91234
satoshisToRedeem = struct.pack("<Q", satoshis).encode('hex')
print "\t" + satoshisToRedeem

# scriptPubKey Length
#     '%02x' % len(scriptSig.decode('hex')) + 
print "\t<scriptPubKey Length>"

# scriptPubKey with Signature
#     scriptPubKey
print "\t<scriptPubKey with Signature>"

# Lock Time
blockLockTime = "00000000"
print blockLockTime
