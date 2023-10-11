# CheckpointAnalyzer

#### This script allows to get logs from Сheckpoint API

#### instalation

First you need to create a virtual environment. If you don't have virtualenv package installed run:

```bash
pip install virtualenv
```

Then, create a new environment

```bash
# Create a virtual environment called 'venv'
python -m virtualenv venv
```

Activate created virtual environment 'venv'

```bash
# For Linux/MacOS
source venv/bin/activate

# For Windows (command prompt)
venv\bin\activate.bat

# For Windows (power shell)
venv\Scripts\Activate.ps1
```

Finally, you can install requirements
The following command will install the latest version of the utilities

```bash
pip install -r requirements.txt
```
This command will install **cyberoo_utils** and **requests**

**NOTE**: it tells to have a python version 3.6+

#### Getting started

Add customer credentials to **customer** folder, this file has to be json file which looks like this:

```bash
{

    "api_key": "API_KEY_VALUE",

    "server": "SERVER_IP",

    "port": "SERVER_PORT",

    "username": "USERNAME"

  }
```


Use following command to run script:

```bash
# Windows
python main.py

# Linux
python3 main.py
```
