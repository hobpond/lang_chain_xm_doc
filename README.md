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
python src/openai_qa.py
```

### Notes
Based on examples from Sam Witteveen youtube videos