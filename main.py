import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

msal_js_url = "https://github.com/AzureAD/microsoft-authentication-library-for-js/blob/dev"
local_msal_js_path = "/Users/medhirbhargava/code/msal/microsoft-authentication-library-for-js/"

llm = Ollama(model="mixtral")
db = Chroma(persist_directory="./chroma_db", embedding_function=OllamaEmbeddings(model="mixtral"))
retriever = db.as_retriever(
    search_type="mmr", 
    search_kwargs={"k":8},
)

# Prompt
template = """
You are an expert programmer and problem solver, tasked with answering any question about Microsoft Authentication Library for Javascript (MSAL.js)

Generate a comprehensive and informative answer for the \
given question based solely on the provided context.
If you don't know the answer, just say that you don't know, don't try to make up an answer. \
If you are asked questions about MSAL library usage, provide holistic answers with code samples if necessary.
Keep the answer as concise as possible. 
{context}
Question: {input}
Helpful Answer:"""

QA_CHAIN_PROMPT = PromptTemplate(
    input_variables=["context", "question"],
    template=template,
)

combine_docs_chain = create_stuff_documents_chain(llm, QA_CHAIN_PROMPT)
retrieval_chain = create_retrieval_chain(retriever, combine_docs_chain)

st.title("MSAL Javascript Chatbot")

def generate_response(question):
    # generate answer 
    response = retrieval_chain.invoke({"input":question})
    st.info(response["answer"])

    # format retrieved sources 
    st.write("Referenced sources")
    docs = response["context"]
    for doc in docs:
        link = st.columns(1)
        local_source = doc.metadata['source']
        github_url = msal_js_url + '/' + local_source.removeprefix(local_msal_js_path)
        link[0].markdown(f" - {github_url}")

with st.form("my_form"):
    text = st.text_area("Enter question:", "Can you provide a code sample showing how to authenticate a user with MSAL React?")
    submitted = st.form_submit_button("Ask Question")
    if submitted:
        generate_response(text)