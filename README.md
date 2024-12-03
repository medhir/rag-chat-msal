# MSAL Javascript Chatbot

A proof-of-concept for helping developers use MSAL through a natural langauge interface. 

The aim of this demo is to show how Retrieval Augmented Generation (RAG) can be used to enhance the onboarding experience by: 

- Providing answers (including code samples) tailored to specific scenarios 
- Linking back to relevant documentation / source code for better library discovery

<img width="898" alt="Screen Shot 2024-01-14 at 1 19 30 PM" src="https://github.com/medhir/rag-chat-msal/assets/5160860/6150c118-ed4e-48fd-b172-9f736f38785d">

## Setup

This demo requires a GPU and enough RAM to load the [Mixtral 8x7b](https://mistral.ai/news/mixtral-of-experts/) Mixture-of-Experts Large Language Model (LLM). The original demo was built on a M1 Max Macbook Pro with 64GB of unified RAM, which is enough to load the 47B parameter model into memory. You may need to use a quantized version of the model or replace the local LLM with API calls to a cloud-based model if your system doesn't meet the minimum GPU / RAM requirements. 

### Environment Setup

Assuming you've met the system requirements, first we'll need to create a virtual environment to isolate the Python dependencies for this project. 

[Install conda using this guide](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html), then run the following command to create a new virtual enviornment: 

```sh
conda create -n msal-chat python=3.10 
```

Then activate the enviornment. 

```sh
conda activate msal-chat
```

With our python environment setup complete, install the required dependencies: 

```sh
pip install -r requirements.txt
```

### Ollama Setup

We will also need Ollama in order to run language models locally. [Download Ollama](https://ollama.com/download), move the mounted app to the `Applicatons` folder, and start it.

Once Ollama is installed and running, run the following command in your terminal to download and start running the `mixtral` model.

```sh
ollama run mixtral
```

This will take a while depending on your internet speed as the model is about 26GB in size. Note that while we use the `mixtral` model in this demo, you can use any of the models that Ollama offers. 

### Generate Vector Embeddings

Training data must be ingested as embeddings into a vector database for later reference as part of queries issued to the chatbot. To ingest the MSAL Javascript repository, run the following command: 

```sh
python ingest.py
```

## Running Locally

With the MSAL.js data ingested, you can now run the chatbot with the following commmand: 

```sh
streamlit run main.py
```
