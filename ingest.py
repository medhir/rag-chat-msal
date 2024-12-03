import os
import subprocess
from pathlib import Path
from langchain.text_splitter import Language
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import LanguageParser
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings

# Create temp directory and clone repo
repo_url = "https://github.com/AzureAD/microsoft-authentication-library-for-js.git"
repo_path = Path("./msal-js-repo").absolute()

if not repo_path.exists():
    print(f"Cloning MSAL.js repository to {repo_path}...")
    subprocess.run(["git", "clone", repo_url, str(repo_path)], check=True)

# load documents
lib_js_loader = GenericLoader.from_filesystem(
    str(repo_path / "lib"),
    glob='**/*',
    suffixes=[".js", ".ts", ".jsx", ".tsx"], 
    exclude=[".min.js"],
    parser=LanguageParser(language=Language.JS)
)

samples_js_loader = GenericLoader.from_filesystem(
    str(repo_path / "samples"),
    glob='**/*',
    suffixes=[".js", ".ts", ".jsx", ".tsx"], 
    exclude=[".min.js"],
    parser=LanguageParser(language=Language.JS)
)

lib_js_docs = lib_js_loader.load()
samples_js_docs = samples_js_loader.load()

# chunk documents 
js_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.JS, chunk_size=2000, chunk_overlap=200
)
js_texts = js_splitter.split_documents(lib_js_docs + samples_js_docs) 

# generate index
db = Chroma.from_documents(js_texts, OllamaEmbeddings(model="mixtral"), persist_directory="./chroma_db")