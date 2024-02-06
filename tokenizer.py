import re
from advanced_data_processing import stem_tokens

def tokenize(text):

    tokens = re.findall(r'\b\w+\b', text.lower())
    return tokens

def tokenize_with_stemming(text):
    tokens = tokenize(text)  # Use the existing tokenize function
    stemmed_tokens = stem_tokens(tokens)
    return stemmed_tokens

def tokenize_with_positions(text):
    import re
    tokens_with_positions = []
    for match in re.finditer(r'\b\w+\b', text.lower()):
        start, end = match.span()
        token = text[start:end]
        tokens_with_positions.append((token, start))
    return tokens_with_positions