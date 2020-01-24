# exploreThirftPython
Explore Thrift in Python

We can create the thrift client and server from thrift protocol or we can direct use the thriftpy2 library for doing that.

In the examples, additionClient.py and additionServer.py implements the thrift protocol using the thirft commnd line generated code. 
Where as additionClientThrifyPy2.py and additionServerThriftPy2.py uses and implements thrift protocol from library generated thrift code.

## Generate

```bash
thrift -out pygen/ --gen py addition.thrift
```

### Requirements
* Python: `$ pip install -r requirements.txt`

### Run
* Pyyhon Server: `$ ./additionServer.py`,
* Python client: `$ ./additionClient.py` 

### Output
```bash
$ ./additionServer.py
Starting python server...
```
```bash
$ ./additionClient.py
Addition Service Initiated: 
Sum of 10 and 20 is: 30
```
