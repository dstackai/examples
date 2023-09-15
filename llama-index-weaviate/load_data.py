import os
from pathlib import Path

import weaviate
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

from llama_index import (
    LangchainEmbedding,
    ServiceContext,
    StorageContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
)
from llama_index.vector_stores import WeaviateVectorStore

weaviate_api_key = os.getenv("WEAVIATE_API_TOKEN")
weaviate_url = os.getenv("WEAVIATE_URL")

if not weaviate_api_key or not weaviate_url:
    exit(
        "Make sure you've set WEAVIATE_API_TOKEN and WEAVIATE_URL environment variables"
    )

auth_config = weaviate.AuthApiKey(api_key=weaviate_api_key)

client = weaviate.Client(
    url=weaviate_url,
    auth_client_secret=auth_config,
)

client.schema.delete_class("llama-index-weaviate")

embed_model = LangchainEmbedding(HuggingFaceEmbeddings())

service_context = ServiceContext.from_defaults(
    embed_model=embed_model,
    llm=None,
)

vector_store = WeaviateVectorStore(
    weaviate_client=client, index_name="llama-index-weaviate"
)

storage_context = StorageContext.from_defaults(vector_store=vector_store)


documents = SimpleDirectoryReader(Path(__file__).parent / "data").load_data()

index = VectorStoreIndex.from_documents(
    documents,
    service_context=service_context,
    storage_context=storage_context,
)
