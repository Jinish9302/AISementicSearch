# AI Semantic Search Application

Wonder How Google Bard, ChatGPT and search engines know exactly what we want with only one line of prompt? AI Semantic Search application is used to get relevant results to your prompt with help of Artificial Intelligence. Here's the miniature version of such applications.

## Installation of application

<b>Step 1:</b><br>
To install relevant libraries necessary for the given application run the following command in terminal (make sure you are in the same directory in which all the codes are stored)
```bash
pip install -r requirements.txt
```
<b>Step 2:</b><br>
Run the following program in the terminal. you only need to run this command when running the code for the first time
```bash
python setup.py
```
If api keys are not configured the program will ask the api keys for hugging face api and pinecone api as well as environment for pinecone api here. to get the apk keys and environment for pinecone api go to [Pinecone](https://www.pinecone.io/). and for hugging face token go to [Hugging Face](http://hf.co/settings/tokens)

After running the setup.py json file named "credentials.json" in folder. which will look like tgus

```json
{
    "api_key": "YOUR_API_KEY", 
    "env": "asia-southeast1-gcp-free", 
    "hf_token": "YOUR_HF_KEY"
}
```

<b>Step 3:</b><br>
Run the following command on Terminal to open the application
```bash
flask --app app run
```

## APIs used for application
[Pinecone](https://www.pinecone.io/): Provides an efficient way to store and retrieve the most relevant<br>
[Hugging Face](http://hf.co/settings/tokens): To retrieve Vector embeddings of given document

