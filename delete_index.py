import pinecone as pc

with open("api_key", 'r') as f:
    token, env = f.read().split(' ')

# initialize api
print("initializing session....")
pc.init(api_key=token, environment=env)

print("list of index: ", pc.list_indexes())


# deleting index
print("Deleting Index....")
pc.delete_index('my-index')

print("index deleted successfully....")