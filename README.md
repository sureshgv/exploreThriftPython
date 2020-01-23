# exploreThirftPython
Explore Thrift in Python


## Generate

```bash
thrift -out pygen/ --gen py example.thrift
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
