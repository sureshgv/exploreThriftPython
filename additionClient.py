#!/usr/bin/env python

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from pygen.addition import AdditionService


try:
    transport = TSocket.TSocket('localhost', 30303)
    transport = TTransport.TBufferedTransport(transport)
    protocol = TBinaryProtocol.TBinaryProtocol(transport)
    client = AdditionService.Client(protocol)
    transport.open()
    print('Addition Service Initiated: ')
    a = 10
    b = 20
    result = client.add(a, b)
    print('Sum of ' +  str(a) + ' and ' + str(b) + ' is: ' + str(result))
    transport.close()

except Thrift.TException as tx:
    print(tx.message)
