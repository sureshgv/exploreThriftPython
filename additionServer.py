#!/usr/bin/env python

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from pygen.addition import AdditionService


class AdditionServiceHandler:
    def __init__(self):
        self.log = {}

    def add(self, a, b):
        print("Sending the sub a and b")
        return a + b


handler = AdditionServiceHandler()
processor = AdditionService.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print("Starting python server...")
server.serve()
print("done!")
