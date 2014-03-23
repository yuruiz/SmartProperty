import privateKey, publicKey
import time, datetime

KEY_GENERATION_LOG_FILE = "keyGenerationLog.txt"

#privKey = privateKey.getStrongRandomKey(256)
#privKey = "0C28FCA386C7A227600B2FE50B7CAE11EC86D3BF1FBE471BE89827E19D72AA1D"
#privKey = "f19c523315891e6e15ae0608a35eec2e00ebd6d1984cf167f46336dabd9b2de4"
#privKey = "52BB9A981288DF29D47E8020093C64CD9539876130F5492D24D303152A6FEA2A"
#privKey = "EF7BADE09BA08731A2AEC3BDA0FBCD06A235C497D32C9FB99A589700540BCA4B"
#privKey = "c9b74446725c99d429848f8093a347976784d133efec971343be004d5f9c7fdc"
privKey = "e97174e793c7524c0a68eda86458682bd9c5510e6e3614cc5cecdffe966c925b"

mainAddressWIF = privateKey.getWIFPrivateKey(privKey, "main")
testAddressWIF = privateKey.getWIFPrivateKey(privKey, "test")

mainPubKeyPublicAddress = publicKey.getPublicAddress(privKey, "main_pubkey")
mainScriptPublicAddress = publicKey.getPublicAddress(privKey, "main_script")
testPublicAddress = publicKey.getPublicAddress(privKey, "test")

file = open(KEY_GENERATION_LOG_FILE, "a")

getTimeNow = time.time()
getFormattedTime = datetime.datetime.fromtimestamp(getTimeNow).strftime('%Y-%m-%d %H:%M:%S')

file.write(getFormattedTime + ": " + "\n")
file.write("\t" + "Private Key: " + privKey + "\n")
file.write("\t\t" + "Main Address WIF: " + mainAddressWIF + "\n")
file.write("\t\t" + "Test Address WIF: " + testAddressWIF + "\n")
file.write("\t" + "Bitcoin Public Addresses: " + "\n")
file.write("\t\t" + "Main PubKey Address: " + mainPubKeyPublicAddress + "\n")
file.write("\t\t" + "Main Script Address: " + mainScriptPublicAddress + "\n")
file.write("\t\t" + "Test Address: " + testPublicAddress + "\n")
file.write("\n")
file.close()