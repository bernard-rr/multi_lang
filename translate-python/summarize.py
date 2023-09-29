import os
import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import nltk
import random
from nltk.tokenize import sent_tokenize
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import subprocess

load_dotenv()

# Download NLTK data (if not already downloaded)
nltk.download('punkt')

# Get the current working directory
current_directory = os.getcwd()

# Specify the relative path to the 'translate-python' directory
relative_path = 'multi_lang/translate-python'

# Construct the full path
full_path = os.path.join(current_directory, relative_path)

# Switch to the translate-python directory
os.chdir(full_path)

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Preprocess the transcript
def preprocess_transcript(transcript_text):
    doc = nlp(transcript_text)
    sentences = [sent.text for sent in doc.sents]
    return sentences

# Text summarization using TF-IDF
def summarize_transcript(transcript_text, num_sentences=5):
    sentences = preprocess_transcript(transcript_text)
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()

    # Calculate TF-IDF scores for sentences
    tfidf_matrix = vectorizer.fit_transform(sentences)

    # Calculate sentence scores based on TF-IDF
    sentence_scores = tfidf_matrix.sum(axis=1)

    # Get the indices of the top-ranked sentences
    top_sentence_indices = np.array(sentence_scores).flatten().argsort()[-num_sentences:][::-1]

    # Generate the summary
    summary = [sentences[i] for i in top_sentence_indices]
    return ' '.join(summary)


def summarize_text(text, language):
    API_ENDPOINT = "us-central1-aiplatform.googleapis.com"
    PROJECT_ID = "text-translation-399014"
    MODEL_ID = "text-bison@001"
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

    prompt_template = PromptTemplate.from_template(
        '''
        You are a professional summarizer of YouTube video transcripts. 
        You know how to take the readers in a journey to make your summary interesting. 
        You end the summary with suspense to try to get the user to watch the YouTube video. 
        You also finish your summaries with a full stop because you are very calculative.
        You also know multiple languages especially Spanish, Chinese and French.

        Follow the instructions carefully and be calculative.

        In 300 words, give a detailed summary of this text: {text} in {language}
        '''
    )

    formatted_prompt = prompt_template.format(text=text, language=language)

    url = f"https://{API_ENDPOINT}/v1/projects/{PROJECT_ID}/locations/us-central1/publishers/google/models/{MODEL_ID}:predict"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "instances": [
            {
                "content": f"{formatted_prompt}"
            }
        ],
        "parameters": {
            "candidateCount": 1,
            "maxOutputTokens": 256,
            "temperature": 0.0,
            "topP": 0.8,
            "topK": 40
        }
    }

    response = requests.post(url, headers=headers, json=data)
    translation_result = response.json()
    content = translation_result['predictions'][0]['content']

    return content

# text_to_translate = '''
# In that light, I'm currently looking to join an Engineering team where my 
# skills will be more aligned with the company activities. 
# It would be a great opportunity to join your team as a Software Engineer where 
# I know the team will benefit from my experience and I also will benefit from the vast experience of the team.
# '''

# translation = summarize_text(text_to_translate)
# print(translation)


# response = requests.post(url, headers=headers, json=data)
# response_data = response.json()
# content = response_data['predictions'][0]['content']
# print(content)