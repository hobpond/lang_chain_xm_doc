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
Can you help me write a python script that goes through a list of Groups and find the first primary OnCall person,
note down their TimeZone and then output the result as a map where the key is a Group and the vlaue is a 
Person object that has the per id, their name and their time zone?"
```

### Sample output
Yes, I can help you with that. Here's an example script that should accomplish what you're looking for:

``` python
import requests
import json

# Define the base URL and authentication credentials
base_url = "https://acmeco.xmatters.com/api/xm/1"
auth = ("username", "password")

# Define a function to get the primary on-call person for a group
def get_primary_oncall_person(group_id):
    # Build the URL for the group endpoint
    url = f"{base_url}/groups/{group_id}/memberships"

    # Send a GET request to the group endpoint
    response = requests.get(url, auth=auth)

    # Parse the response JSON
    memberships = json.loads(response.text)

    # Loop through the memberships to find the primary on-call person
    for membership in memberships:
        if membership["role"] == "PRIMARY":
            # Build the URL for the person endpoint
            url = f"{base_url}/people/{membership['person']['id']}"

            # Send a GET request to the person endpoint
            response = requests.get(url, auth=auth)

            # Parse the response JSON
            person = json.loads(response.text)

            # Return the person object
            return person

    # If no primary on-call person was found, return None
    return None

# Define a list of group IDs to check
group_ids = ["group1", "group2", "group3"]

# Define a dictionary to store the results
results = {}

# Loop through the group IDs and get the primary on-call person for each group
for group_id in group_ids:
    person = get_primary_oncall_person(group_id)
    if person is not None:
        # Add the person object to the results dictionary
        results[group_id] = {
            "id": person["id"],
            "name": person["targetName"],
            "timezone": person["timezone"]
        }

# Print the results
print(json.dumps(results, indent=4))
```

This script defines a function `get_primary_oncall_person` that takes a group ID as input and returns the primary on-
call person for that group. It then loops through a list of group IDs, calls this function for each group, and stores
the results in a dictionary. Finally, it prints the results as a JSON-formatted string.

Note that you'll need to replace the `base_url` and `auth` variables with the appropriate values for your xMatters
instance, and you'll need to replace the `group_ids` list with the IDs of the groups you want to check.


Sources:
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api
https://help.xmatters.com/xmapi/index.html#xmatters-rest-api 


### Notes
Based on examples from Sam Witteveen youtube videos

