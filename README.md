# CheckpointAnalyzer

#### This script allows to get logs from checkpoint API

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
# For unix
source venv/bin/activate

# For windows
.\venv\Scripts\activate
```

Finally, you can install requirements
The following command will install the latest version of the utilities

```bash
pip install -r requirements.txt
```


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

