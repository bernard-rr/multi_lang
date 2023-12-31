import os
import requests
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import nltk
import random
from nltk.tokenize import sent_tokenize

load_dotenv()

nltk.download('punkt')  # Download the NLTK data (if not already downloaded)



def random_sentences_from_text(text, num_sentences=800):
    # Tokenize the input text into sentences
    sentences = sent_tokenize(text)

    # Ensure the requested number of sentences does not exceed the total number of sentences available
    num_sentences = min(num_sentences, len(sentences))

    # Randomly select `num_sentences` from the list of sentences
    selected_sentences = random.sample(sentences, num_sentences)

    # Combine the selected sentences into a shorter text
    shorter_text = ' '.join(selected_sentences)

    return shorter_text

def summarize_text(text):
    API_ENDPOINT = "us-central1-aiplatform.googleapis.com"
    PROJECT_ID = "text-translation-399014"
    MODEL_ID = "text-bison@001"
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')

    prompt_template = PromptTemplate.from_template(
        '''
        You are a professional summarizer of YouTube video transcripts. You know how to take the readers in a journey to make your summary interesting. You end the summary with suspense to try to get the user to watch the YouTube video. You also finish your summaries with a full stop because you are very calculative.

        Follow the instructions carefully and be calculative.

        In 300 words, give a detailed summary of this text: {text} 
        '''
    )

    formatted_prompt = prompt_template.format(text=text)

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

    return translation_result

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