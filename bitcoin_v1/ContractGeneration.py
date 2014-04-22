from Crypto.Hash import SHA256
import transaction

def GenerateTxList(PreTxHashList, PreTxOutputIndexList, OwnershipPrviateKey, OwnershipPubkey, OwnerWalleptPubAddr,
	TempKeyPubAddrList, Nmounth, Timelist, Payment):
	assert(len(TempKeyPubAddrList) == Nmounth == len(Timelist) == len(Payment))

	hashtype = ['81']
	SATOSHIS = 1000000
	TransactionInput = []
	TransactionOutput = []
	for x in xrange(0,Nmounth):
		TransactionInput.append([[PreTxHashList[x], PreTxOutputIndexList[x], OwnershipPubkey, OwnershipPrviateKey]])
		TransactionOutput.append([[SATOSHIS, TempKeyPubAddrList[x]], [Payment[x], OwnerWalleptPubAddr]])
	transactionlist = []
	for x in xrange(0,Nmounth):
		if x == 0:
			OutputScript = [Timelist[x].encode('hex') , None]
		elif x == Nmounth - 1:
			OutputScript = [None, None]
		else:
			OutputScript = [Timelist[x].encode('hex') + SHA256.new(transactionlist[x-1].decode("hex")).hexdigest(), None]

		transactionlist.append(transaction.buildSignedTransaction(OwnershipPrviateKey, TransactionInput[x],
			TransactionOutput[x], hashtype, OutputScript))

	return transactionlist
