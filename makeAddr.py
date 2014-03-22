import keyUtils, time, datetime, utils

from Crypto.Random import random
from Crypto.Hash import SHA256
from Crypto.Hash import RIPEMD160


#Bitcoin Network Prefix
MAINNET_ADDRESS_PREFIX = 0x80
TESTNET_ADDRESS_PREFIX = 0xEF

#Four-Byte Checksum Length
CHECKSUM_LENGTH = 4 * 2

#private_key = ''.join(['%x' % random.randrange(16) for x in range(0, 64)])

#This creates a cryptographically secure random 256bit private key
sRandom = random.StrongRandom()
randomBits = sRandom.getrandbits(256)
stringRandomBits = str(randomBits)

#Appends prefix to distinguish between Main Net vs. Test Net
privateKey = SHA256.new(stringRandomBits).hexdigest()
#privateKey = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"
mainAddress = "".join(("%x" % MAINNET_ADDRESS_PREFIX, privateKey))
testAddress = "".join(("%x" % TESTNET_ADDRESS_PREFIX, privateKey))

#Calculates the checksum
oneSHA256MainAddress = SHA256.new(mainAddress.decode("hex")).hexdigest()
oneSHA256TestAddress = SHA256.new(testAddress.decode("hex")).hexdigest()
twoSHA256MainAddress = SHA256.new(oneSHA256MainAddress.decode("hex")).hexdigest()
twoSHA256TestAddress = SHA256.new(oneSHA256TestAddress.decode("hex")).hexdigest()
mainAddressCheckSum = twoSHA256MainAddress[0:CHECKSUM_LENGTH]
testAddressCheckSum = twoSHA256TestAddress[0:CHECKSUM_LENGTH]

mainAddressWithChecksum = "".join((mainAddress, mainAddressCheckSum))
testAddressWithChecksum = "".join((testAddress, testAddressCheckSum))

mainAddressWIF = utils.base58encode(utils.base256decode(mainAddressWithChecksum.decode("hex")))
testAddressWIF = utils.base58encode(utils.base256decode(testAddressWithChecksum.decode("hex")))


file = open("keyGenerationLog.txt", "a")

getTimeNow = time.time()
getFormattedTime = datetime.datetime.fromtimestamp(getTimeNow).strftime('%Y-%m-%d %H:%M:%S')

file.write(getFormattedTime + ": " + "\n")
file.write("\t" + "Private Key: " + privateKey + "\n")
file.write("\t" + "Main Net Address: " + mainAddress + "\n")
file.write("\t" + "Test Net Address: " + testAddress + "\n")
file.write("\t" + "Main Address Checksum: " + mainAddressCheckSum + "\n")
file.write("\t" + "Test Address Checksum: " + testAddressCheckSum + "\n")
file.write("\t" + "Main Address With Checksum: " + mainAddressWithChecksum + "\n")
file.write("\t" + "Test Address With Checksum: " + testAddressWithChecksum + "\n")
file.write("\t" + "Main Address WIF: " + mainAddressWIF + "\n")
file.write("\t" + "Test Address WIF: " + testAddressWIF + "\n")


#file.write("\n")
file.close()



print keyUtils.privateKeyToWif(privateKey)
print keyUtils.keyToAddr(privateKey)

