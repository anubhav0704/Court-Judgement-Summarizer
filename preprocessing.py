import re
from typing import List

def clean_text(text: str) -> str:
    """
    Cleans legal text by removing extra whitespace, normalizing citations, 
    and handling common legal abbreviations if necessary.
    """
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove numbering like "1.", "2." at start of lines if they exist in the raw block
    # (Though we often get a single blob strings)
    
    # Basic citation normalization (e.g., "AIR 1953 SC 1" -> "AIR_1953_SC_1") - optional but helps tokens
    # For now, we will keep it simple to avoid over-cleaning useful info.
    
    return text

def sentence_segmentation(text: str) -> List[str]:
    """
    Splits text into sentences.
    Simple heuristic splitting on periods followed by spaces/capital letters.
    """
    # A simple regex for sentence splitting.
    # Look for a period, followed by a space, followed by an uppercase letter (if casing exists)
    # Since our text might be lowercased (based on analysis), we just split on period+space.
    # Warning: Abbreviations like 'v.' or 'no.' might break this.
    
    # Let's try to be slightly smarter about common abbrevs.
    cleaned = text
    abbreviations = {'v.', 'no.', 'mr.', 'mrs.', 'dr.', 'corp.', 'ltd.', 'art.', 'sec.', 's.'}
    
    # This is a basic custom splitter logic
    words = cleaned.split(' ')
    sentences = []
    current_sent = []
    
    for word in words:
        current_sent.append(word)
        if word.endswith('.') or word.endswith('?') or word.endswith('!'):
            # Check if it's an abbreviation
            if word.lower() in abbreviations:
                continue
            # Also check if it looks like an acronym e.g. U.S.A.
            if len(word) > 2 and word[-2] == '.': # crude check
                 pass
            else:
                 # End of sentence
                 sentences.append(" ".join(current_sent))
                 current_sent = []
                 
    if current_sent:
        sentences.append(" ".join(current_sent))
        
    return sentences

def chunk_text(text: str, tokenizer, max_tokens: int = 16384) -> List[str]:
    """
    Chunks text directly using the tokenizer to ensure we fit within limits.
    Returns a list of decoded strings.
    """
    # Tokenize full text
    tokens = tokenizer.encode(text, add_special_tokens=False)
    
    if len(tokens) <= max_tokens:
        return [text]
    
    # Split into chunks
    chunks = []
    for i in range(0, len(tokens), max_tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunk_str = tokenizer.decode(chunk_tokens, skip_special_tokens=True)
        chunks.append(chunk_str)
        
    return chunks
