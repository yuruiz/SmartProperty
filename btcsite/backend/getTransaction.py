import httplib
import json
import os
import sys

servAddr = "blockr.io"
transaction = "60c1f1a3160042152114e2bba45600a5045711c3a8a458016248acec59653471"

def printText(txt):
    lines = txt.split('\n')
    for line in lines:
        print line.strip()

def connectServer(servAddr):
  httpServ = httplib.HTTPConnection(servAddr)
  httpServ.connect()
  return httpServ

def sendRequest(httpServ, transaction, returnType):
  requestURL = "/api/v1/tx/" + returnType + "/" + transaction
  httpServ.request('GET', requestURL)

def getResponse(httpServ):
  response = httpServ.getresponse()
  if response.status == httplib.OK:
    return response.read()

def disconnectServer(httpServ):
  httpServ.close()

def test():
  httpServ = connectServer(servAddr)
  sendRequest(httpServ, transaction, "info")
  #sendRequest(httpServ, transaction, "raw")
  response = getResponse(httpServ)
  print "Output from HTML request"
  printText(response)
  responseJson = json.loads(response)
  disconnectServer(httpServ)
  return responseJson

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btcsite.settings")

    from django.core.management import execute_from_command_line

    # responseJson is a json object that contains all the info, can use as a dict
    responseJson = test()

    # Example: get a specific transaction's output
    print "Result:"
    print responseJson[u'data'][u'tx']
    
    execute_from_command_line(sys.argv)
