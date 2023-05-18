# from transformers import BertModel, BertTokenizer
import pinecone as pc
import requests



# retrive api key and environment
with open("api_key", 'r') as f:
    token, env = f.read().split(' ')
# initialize session and getting index
pc.init(api_key=token, environment=env)
idx = pc.Index("my-index")

# retriving token from file
model_id = "sentence-transformers/all-MiniLM-L6-v2"
# hf_token = "get your token in http://hf.co/settings/tokens"
with open("hf_token", 'r') as f:
    hf_token = f.read()
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}

# import torch

# print("Loading Bert Model and Tokenizer.....")
# model = BertModel.from_pretrained("bert_model")
# tokenizer = BertTokenizer.from_pretrained("tokenizer")

def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()
with open("api_key", 'r') as f:
    token, env = f.read().split(' ')

# initialize token
print("initializing session....")
pc.init(api_key=token, environment=env)

# get index
print("load index.....")
idx = pc.Index("my-index")

a = input("Enter the search prompt: ")
document_vec = query(a)

result = idx.query(
  vector=document_vec,
  top_k=3,
  include_metadata=True
)

print(result)