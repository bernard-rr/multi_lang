import os
from dotenv import load_dotenv
import google.generativeai as palm
from langchain.prompts import PromptTemplate

load_dotenv()

API_KEY = os.environ.get('API_KEY')

palm.configure(api_key=API_KEY)

model_id = 'models/chat-bison-001'

text = '''
The Word was with God
'''
language = "French"

prompt_template = PromptTemplate.from_template(
    '''
    You are an English to {language} translator.
    I will ask you a question and you will give me a straight response with just the answer.
    what is ```{text}``` in ```{language}```.
    '''
    )

formatted_prompt = prompt_template.format(text=text, language=language)

# prompt = '''
# How are you in french
# '''

# prompt = '''
# Write a marketing proposal to sell icecream
# '''
response = palm.chat(
    model=model_id,
    prompt=formatted_prompt,
    temperature=0.0,
    candidate_count=1
)
# for message in response.messages:
#     print(message["content"][1])
# author1_content = next(item['content'] for item in response.messages if item['author'] == '1')
# print(author1_content)
print(response.messages)