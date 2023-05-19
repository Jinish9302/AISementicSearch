import pinecone as pc
import json


def create_index():
    f = json.load(open("credentials.json"))
    # initialize token

    print("initializing session....")
    pc.init(api_key=f['api_key'], environment=f['env'])

    # create index
    print("creating my-index...")
    pc.create_index("my-index", dimension=384, metric = 'euclidean')

    print("Index Created Successfully")

if __name__ == "__main__":
    create_index()