import keyUtils
import privateKey

privKey = privateKey.getStrongRandomKey(256)


print keyUtils.privateKeyToWif(privKey)
print keyUtils.keyToAddr(privKey)

