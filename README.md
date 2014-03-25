bitcoins
========


3rd Party Python Packages Required:
- Pycrypto 2.6 - https://www.dlitz.net/software/pycrypto/ 
	WIN: https://www.dlitz.net/software/pycrypto/
	OTHER: See official site
- ECDSA - https://pypi.python.org/pypi/ecdsa


2014-03-24 (bitcoin_v1):

Rewrote most of the code forked from the version created by Ken Shirriff over at: 
http://www.righto.com/2014/02/bitcoins-hard-way-using-raw-bitcoin.html

This is still issue when trying to broadcast transaction via TESTNET3, have not yet tried the MAIN NET yet.

- Run by executing transmission.py
- All the transaction details can be found inside the transaction.py file
- Message file helps the construction of the required messages needed to facilitate sending transactions.
- {publicKey,PrivateKey}.py files are required to generate keys within the keyGenerationLog.txt
- Keys generated here are cryptopgraphically secure, an improvement from Ken's previous code by adopting the use of the pycrypto package.

