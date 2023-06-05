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
python src/openai_dir_qa.py
```

### Test prompt
```
Can you help me write a python script that gets the on-call details of a group in xMatters.
Finding the first Primary on-call person, note down their TimeZone and then output the result 
as a map where the key is a Group and the vlaue is a Person object that has the per id,
their name and their time zone?
```

### Sample output
Sure, here's an example Python script that should do what you're asking for:

```python
import requests
from requests.auth import HTTPBasicAuth
import json

# Set up the xMatters API endpoint and credentials
base_URL = "https://acmeco.xmatters.com/api/xm/1"
username = "your_username"
password = "your_password"

# Set up the group ID for the group you want to get on-call details for
group_id = "your_group_id"

# Make the API call to get the on-call details for the group
response = requests.get(f"{base_URL}/on-call-summary?groups={group_id}", auth=HTTPBasicAuth(username, password))

# Parse the response JSON and find the first primary on-call person
on_call_data = json.loads(response.text)
primary_on_call = None
for recipient in on_call_data:
    if recipient["shift"]["name"] == "Primary":
        primary_on_call = recipient
        break

# If we found a primary on-call person, create a Person object with their details
if primary_on_call:
    person = {
        "id": primary_on_call["recipient"]["id"],
        "name": primary_on_call["recipient"]["targetName"],
        "time_zone": primary_on_call["recipient"]["timeZone"]
    }
else:
    person = None

# Output the result as a map with the group ID as the key and the Person object as the value
result = {group_id: person}
print(result)
```

You'll need to replace the `base_URL`, `username`, `password`, and `group_id` variables with the appropriate values for
your xMatters instance and the group you want to get on-call details for. Let me know if you have any questions!


Sources:
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\on-call\_get-on-call.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\on-call-summary\_get-on-call-summary.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\group-roster\_get-group-roster.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\shifts\_get-shift-member.md

### Notes
Based on examples from Sam Witteveen youtube videos
https://youtu.be/KUDn7bVyIfc
