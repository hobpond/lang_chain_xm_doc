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
Sure, here's an example script that should do what you're asking for:

```python
import requests
from requests.auth import HTTPBasicAuth
import json

base_URL = "https://acmeco.xmatters.com/api/xm/1"
group_id = "954ada78-7b89-4356-b02c-df85ff30dfd2"

# Make the API request to get the on-call details for the group
response = requests.get(f"{base_URL}/on-call?groups={group_id}", auth=HTTPBasicAuth("username", "password"))

# Output the result as a map
result = {
    "Group": group_id,
    "Person": person
}

print(result)
```


Make sure to replace "username" and "password" with your actual xMatters credentials, and
"954ada78-7b89-4356-b02c-df85ff30dfd2" with the ID of the group you want to get the on-call details for.


Sources:
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\on-call\_get-on-call.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\on-call-summary\_get-on-call-summary.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\group-roster\_get-group-roster.md
d:\work\lang_chain_xm_doc\src\help-docs\endpoints\shifts\_get-shift-member.md

### Notes
Based on examples from Sam Witteveen youtube videos
https://youtu.be/KUDn7bVyIfc
