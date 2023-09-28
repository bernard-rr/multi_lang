import nltk
nltk.download('punkt')

import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# Check if the spaCy model is installed, and if not, install it
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Preprocess the transcript
def preprocess_transcript(transcript_text):
    # Tokenize the transcript into sentences using spaCy
    doc = nlp(transcript_text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

# Text summarization using TF-IDF based on the number of tokens
def summarize_transcript_by_tokens(transcript_text, num_tokens=100):
    sentences = preprocess_transcript(transcript_text)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Calculate TF-IDF scores for sentences
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Calculate sentence scores based on TF-IDF
    sentence_scores = tfidf_matrix.sum(axis=1)

    # Initialize variables for the summary
    summary = []
    summary_tokens = 0

    # Select sentences until the specified number of tokens is reached
    for i in range(len(sentences)):
        summary.append(sentences[i])
        summary_tokens += len(sentences[i].split())
        if summary_tokens >= num_tokens:
            break

    return ' '.join(summary)

# YouTube transcript as a single string
youtube_transcript = """
    This is the YouTube transcript without punctuation and it's a long string.
    It contains the spoken content from the video.
    The transcript just flows as one long string.
    You want to summarize this transcript.
    """

# Summarize the transcript based on the number of tokens (e.g., 100 tokens)
summary = summarize_transcript_by_tokens(youtube_transcript, num_tokens=100)

# Print the summary
print(summary)