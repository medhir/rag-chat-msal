# MSAL Javascript Chatbot

A proof-of-concept for helping developers use MSAL through a natural langauge interface. 

The aim of this demo is to show how Retrieval Augmented Generation (RAG) can be used to enhance the onboarding experience by: 

- Providing answers (including code samples) tailored to specific scenarios 
- Linking back to relevant documentation / source code for better library discovery

<img width="898" alt="Screen Shot 2024-01-14 at 1 19 30 PM" src="https://github.com/medhir/rag-chat-msal/assets/5160860/6150c118-ed4e-48fd-b172-9f736f38785d">

## Setup

This demo requires a GPU and enough RAM to load the [Mixtral 8x7b](https://mistral.ai/news/mixtral-of-experts/) Mixture-of-Experts Large Language Model (LLM). The original demo was built on a M1 Max Macbook Pro with 64GB of unified RAM, which is enough to load the 47B parameter model into memory. You may need to use a quantized version of the model or replace the local LLM with API calls to a cloud-based model if your system doesn't meet the minimum GPU / RAM requirements. 


## Running Locally

Training data must be ingested as embeddings into a vector database for later reference as part of queries issued to the chatbot. To ingest the MSAL Javascript repository, run the following command: 

```
```

With the data ingested, you can now run the chatbot with the following commmand: 

```sh
streamlit run main.py
```
