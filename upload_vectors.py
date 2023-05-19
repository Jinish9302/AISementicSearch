import requests, json
import pinecone as pc
# get your token in http://hf.co/settings/tokens
# retrive api key and environment

def upload_vectors():
    f = json.load(open("credentials.json"))
    # initialize token
    print("initializing session....")
    pc.init(api_key=f["api_key"], environment=f['env'])
    idx = pc.Index("my-index")
    model_id = "sentence-transformers/all-MiniLM-L6-v2"
    api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
    headers = {"Authorization": f"Bearer {f['hf_token']}"}

    with open("file.txt") as f:
        documents = f.read().split('\n')[1:101]
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
        if(id%10==0):
            print("Uploaded files: ", id)


if __name__ == '__main__':
    upload_vectors()