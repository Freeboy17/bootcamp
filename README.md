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
- **api_key**: The api_key is API key often generated and provided by the organization or service that is using Checkpoint. [Here](https://sc1.checkpoint.com/documents/R81/WebAdminGuides/EN/CP_R81_SecurityManagement_AdminGuide/Topics-SECMG/Configuring_Authentication_through_an_API_Key.htm), you can find instructions how to generate api key.
- **server**: This value is meant to be IP address of the api server.
- **port**: This value is meant to be api server port.
- **username**: User name used to login into checkpoint API.

Use following command to run script:

```bash
python main.py
```

Logs will be saved in **/var/log/checkpoint-analyzer/checkpoint** directory
