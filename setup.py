import os, json
from create_index import create_index
from upload_vectors import upload_vectors
def ask_credentials():
    api_key = input("Enter Pinecone API key: ")
    env = input("Enter the pinecone env: ")
    hf_token = input("Enter Hugging Face token: ")
    obj = json.dumps({
        "api_key":api_key,
        "env":env,
        "hf_token":hf_token
    })
    with open("credentials.json", 'w') as f:
        f.write(obj)

def set_credetials():
    if(not os.path.exists("credentials.json")):
        ask_credentials()

set_credetials()
try:
    create_index()
except:
    print("Index already exists...")

try:
    upload_vectors()
except:
    print("Some Error occured while uploading vectors ")



    

