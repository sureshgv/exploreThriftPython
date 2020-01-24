import thriftpy2

addition_thrift = thriftpy2.load("addition.thrift", module_name="addition_thrift")
from thriftpy2.rpc import make_client
client = make_client(addition_thrift.AdditionService, '127.0.0.1', 6000)
a = 10
b = 20
print(client.add(a,b))