import pinecone as pc

with open("api_key", 'r') as f:
    token, env = f.read().split(' ')
# initialize token

print("initializing session....")
pc.init(api_key=token, environment=env)

# create index
print("creating my-index")
pc.create_index("my-index", dimension=384, metric = 'euclidean')

print("Index Created Successfully")