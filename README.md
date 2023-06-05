# lang_chain_xm_doc

This project aims to create a Python program that uses langchain and takes the XMatters API documentation and feeds it to the OpenAI GPT-3 API. The purpose is to create an AI model that has in-depth knowledge about XMatters API and can assist developers in working with XMatters APIs more efficiently.



## Getting Started

### Prerequisites

- Python 3.10
- An OpenAI API key

### Installing

To start with the project, clone the repository to your local machine

```bash
git clone https://github.com/hobpond/lang_chain_xm_doc.git
cd lang_chain_xm_doc
```

### Then, install the necessary Python packages:
```bash
pip install -r requirements.txt
```

### Environment Variables
* Make a copy of the .env_template into a file namd .env
* Enter your openai key

### Usage
``` bash
python src/openai_url_qa.py
```

### Test prompt
```
Can you help me write a python script that gets the on-call details of a group in xMatters.
Finding the first Primary on-call person, note down their TimeZone and then output the result 
as a map where the key is a Group and the vlaue is a Person object that has the per id,
their name and their time zone?
```

### Sample output
Sure, here's an example script that should do what you're asking for:

```
import requests
import json

# Set up the API request
base_url = "https://acmeco.xmatters.com/api/xm/1"
group_id = "your_group_id_here"
endpoint_url = f"/groups/{group_id}/on-call"
url = base_url + endpoint_url
auth = requests.auth.HTTPBasicAuth("your_username_here", "your_password_here")
headers = {"Content-Type": "application/json"}

# Make the API request
response = requests.get(url, auth=auth, headers=headers)

# Parse the response JSON
response_json = json.loads(response.text)

# Find the first primary on-call person and get their time zone
primary_on_call = None
for member in response_json["data"]:
    if member["onCall"]["priority"] == "PRIMARY":
        primary_on_call = member
        break

if primary_on_call is None:
    print("No primary on-call person found.")
else:
    # Build the output map
    output_map = {
        "group": group_id,
        "person": {
            "id": primary_on_call["recipient"]["id"],
            "name": primary_on_call["recipient"]["targetName"],
            "time_zone": primary_on_call["timeZone"]
        }
    }

    # Print the output map
    print(output_map)
```

Replace "your_group_id_here", "your_username_here", and "your_password_here" with the appropriate values for your
xMatters instance. When you run the script, it should output a map with the group ID and the details of the first
primary on-call person, including their ID, name, and time zone.


Sources:
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api

### Notes
Based on examples from Sam Witteveen youtube videos
