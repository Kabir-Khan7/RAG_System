from src.data_loader import load_all_document
from src.embedding import EmbeddingPipeline
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    #docs = load_all_document("data")
    store = FaissVectorStore("faiss_store")
    # store.build_from_documents(docs)
    store.load()
    #print(store.query("Tell me about MoZeus app what does it do and how does it work i want in details answer", top_k=3))
    
    rag_search = RAGSearch()
    query = "Tell me about MoZeus app what does it do and how does it work i want in details answer"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)
