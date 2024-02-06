from tokenizer import tokenize

def generate_statistics(docs):
    total_docs = len(docs)
    total_tokens = sum(len(tokenize(doc['title'])) for doc in docs)
    avg_tokens_per_doc = total_tokens / total_docs if total_docs else 0
    return {
        'total_documents': total_docs,
        'total_tokens': total_tokens,
        'average_tokens_per_document': avg_tokens_per_doc
    }
