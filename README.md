bitcoins
========

3rd Party Python Packages Required:
- Pycrypto 2.6 - https://www.dlitz.net/software/pycrypto/ 
	- WIN: http://www..voidspace.org.uk/python/modules.shtml#pycrypto
	- OTHER: See official site
- ECDSA - https://pypi.python.org/pypi/ecdsa

Note: If you are not using Eclipse as IDE, then you can ignore the two project files, using Eclipse will greatly simplify stuff though.

2014-04-11 - Breakthrough Milestone:
====================================

Added support for SIGHASH_ANYONECANPAY.

http://tbtc.blockr.io/tx/info/8f736e16f482e861bd1432dee3d5d2a5b5453832ea0b310703c755127e4fb2d4
http://testnet.btclook.com/txn/8f736e16f482e861bd1432dee3d5d2a5b5453832ea0b310703c755127e4fb2d4


2014-03-27 (bitcoin_v1):
========================

Added support for multi-input transactions.

Successfully tested against TESTNET3 with the following transaction:
https://www.biteasy.com/testnet/transactions/b11c5c3359087f6646b3ea2648bb9f33bfa7f1ea4e255b0ed92caafe23de79a0

2014-03-25 (bitcoin_v1):
========================

Added configurations file to make parameter changes easier.

Successfully performed test against TESTNET3 by broadcasting the following transactions:
- https://www.biteasy.com/testnet/transactions/56ae1f0b9133765424925e19a54604f6745c75465c542c439ac9c861031539de
- https://www.biteasy.com/testnet/transactions/09b91ce9638a7a6dcd93a102a7f5dd0a21d947cb0d5d7e246d146fecef0615ff
- https://www.biteasy.com/testnet/transactions/1f3e58541e81946a142a809816a174b420ecc336531ba4d95ff3f8618328710f


2014-03-24 (bitcoin_v1):
========================

Rewrote most of the code forked from the version created by Ken Shirriff over at: 
http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html

There is still an issue when trying to broadcast transaction via TESTNET3, have not yet tried the MAIN NET yet.

- Run by executing transmission.py
- All the transaction details can be found inside the transaction.py file
- Message file helps the construction of the required messages needed to facilitate sending transactions.
- {publicKey,PrivateKey}.py files are required to generate keys within the keyGenerationLog.txt
- Keys generated here are cryptopgraphically secure, an improvement from Ken's previous code by adopting the use of the pycrypto package.

