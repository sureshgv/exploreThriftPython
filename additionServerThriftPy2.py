import thriftpy2
addition_thrift = thriftpy2.load("addition.thrift", module_name="addition_thrift")

from thriftpy2.rpc import make_server

class AdditionServiceHandler:
    def __init__(self):
        self.log = {}

    def add(self, a, b):
        print("Sending the sub a and b")
        return a + b

server = make_server(addition_thrift.AdditionService, AdditionServiceHandler(), '127.0.0.1', 6000)
server.serve()