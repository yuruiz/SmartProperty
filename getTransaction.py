import httplib
import json

servAddr = "blockchain.info"
servPort = 80
btcAddr = "1GyBNq4bjH9PwYtUwJS7HfcA7msk6Pbbx"
hash160 = "0305229d543e09c2ae9fc224e64287b1d499bcd6"

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

def connectServer(servAddr, servPort):
  httpServ = httplib.HTTPConnection(servAddr, servPort)
  httpServ.connect()
  return httpServ

def sendRequest(httpServ, btcAddr, addrType):
  requestURL = "/"
  if addrType == "hash160" or addrType == "address":
    requestURL += "address/" + btcAddr + "?format=json"
  if addrType == "raw":
    requestURL += "rawaddr/" + btcAddr
  httpServ.request('GET', requestURL)

def getResponse(httpServ):
  response = httpServ.getresponse()
  if response.status == httplib.OK:
    return response.read()

def disconnectServer(httpServ):
  httpServ.close()

def test():
  httpServ = connectServer(servAddr, servPort)
  sendRequest(httpServ, hash160, "hash160")
  #sendRequest(httpServ, btcAddr, "address")
  #sendRequest(httpServ, btcAddr, "raw")
  response = getResponse(httpServ)
  print "Output from HTML request"
  printText(response)
  responseJson = json.loads(response)
  disconnectServer(httpServ)
  return responseJson

# responseJson is a json object that contains all the info, can use as a dict
responseJson = test()

# Example: get a specific transaction's output
responseJson[u'txs'][0][u'out']
