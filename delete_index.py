import pinecone as pc
import json

def delete_index():
    f = json.load(open("credentials.json"))

    # initialize api
    print("initializing session....")
    pc.init(api_key=f['api_key'], environment=f['env'])

    print("list of index: ", pc.list_indexes())


    # deleting index
    print("Deleting Index....")
    pc.delete_index('my-index')

    print("index deleted successfully....")


if __name__ == "__main__":
    delete_index()