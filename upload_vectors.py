import requests
import pinecone as pc
# get your token in http://hf.co/settings/tokens
# retrive api key and environment
with open("api_key", 'r') as f:
    token, env = f.read().split(' ')
# initialize token
print("initializing session....")
pc.init(api_key=token, environment=env)
idx = pc.Index("my-index")


with open("file.txt") as f:
    documents = f.read().split('\n')[1:101]


model_id = "sentence-transformers/all-MiniLM-L6-v2"
with open("hf_token", 'r') as f:
    hf_token = f.read()
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {hf_token}"}
def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

print("Getting Vectors: ")
id = 0
for doc in documents:
    document_vec = query(doc)
    try:
        idx.upsert(vectors = [{
            'id':str(id),
            'values': document_vec,
            'metadata': {
                'text':doc
            }
        }])
    except:
        print("Something went wrong in id-"+str(id));
    id += 1;
    print("Uploaded files: ", id)