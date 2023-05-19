from flask import Flask, render_template, request
import requests, json
import pinecone as pc


f = json.load(open("credentials.json"))


pc.init(api_key=f['api_key'], environment=f['env'])
idx = pc.Index("my-index")

model_id = "sentence-transformers/all-MiniLM-L6-v2"
api_url = f"https://api-inference.huggingface.co/pipeline/feature-extraction/{model_id}"
headers = {"Authorization": f"Bearer {f['hf_token']}"}

def query(texts):
    response = requests.post(api_url, headers=headers, json={"inputs": texts, "options":{"wait_for_model":True}})
    return response.json()

def get_result(vec, cnt):
    return idx.query(
        vector = vec,
        top_k = int(cnt),
        include_metadata = True,
        include_values = False
    )

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])
def serve_page(name = None):
    if request.method == 'POST':
        prompt = request.form.get("prompt")
        result_count = request.form.get("count")
        if(prompt == "" or type(prompt) != type("str")):
            return render_template('index.html', variable = [])
        result_count = int(result_count)
        print(prompt, result_count)
        vec = query(prompt)
        ret = get_result(vec, result_count)
        print(ret["matches"])
        return render_template('index.html', variable = ret['matches'])
    return render_template('index.html', variable = [])
if __name__ == "__main__":
    app.run()