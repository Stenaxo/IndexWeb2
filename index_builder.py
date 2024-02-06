from tokenizer import tokenize, tokenize_with_stemming, tokenize_with_positions

def build_index(docs):
    index = {}
    for doc_id, doc in enumerate(docs):
        tokens = tokenize(doc['title'])
        for token in tokens:
            if token not in index:
                index[token] = []
            if doc_id not in index[token]:
                index[token].append(doc_id)
    return index

def build_index_with_stemming(docs):
    index = {}
    for doc_id, doc in enumerate(docs):
        tokens = tokenize_with_stemming(doc['title'])  # Use the new tokenizer function with stemming
        for token in tokens:
            if token not in index:
                index[token] = []
            if doc_id not in index[token]:
                index[token].append(doc_id)
    return index

def build_positional_index(docs):
    index = {}
    for doc_id, doc in enumerate(docs):
        tokens_with_positions = tokenize_with_positions(doc['title'])
        for token, position in tokens_with_positions:
            if token not in index:
                index[token] = {}
            if doc_id not in index[token]:
                index[token][doc_id] = []
            index[token][doc_id].append(position)
    return index

def build_content_index(docs):
    content_index = {}
    for doc_id, doc in enumerate(docs):
        # Assurez-vous d'avoir un champ 'content' dans vos docs
        tokens = tokenize(doc.get('content', ''))
        for token in tokens:
            if token not in content_index:
                content_index[token] = []
            if doc_id not in content_index[token]:
                content_index[token].append(doc_id)
    return content_index