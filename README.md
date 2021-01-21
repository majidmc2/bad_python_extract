# bad_python_extract
A vulnerable web application written in Python3 Flask to demonstrate insecure file extraction

### Usage
At first you should clone the repository
> git clone https://github.com/majidmc2/bad_python_extract

Then install requirements packages with  **pip3.***

> cd bad_python_extract

> pip3 install -r requirements.txt

Next you should run the server

> python3 server.py

This will start the server at `http://0.0.0.0:6005`

### Attack
**paload.py** is an example that you cam use it for command injection.should

> python3 paload.py

It creates **payload.zip** for inject "print('--------- Injection ---------')" in to **config/__init__.py**.
