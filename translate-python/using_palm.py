import os
import pprint
import google.generativeai as palm
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()
API_KEY = os.environ.get('API_KEY')

palm.configure(api_key=API_KEY)

model = "models/text-bison-001"

# prompt = """
# You are an expert at solving word problems.

# Solve the following problem:

# I have three houses, each with three cats.
# each cat owns 4 mittens, and a hat. Each mitten was
# knit from 7m of yarn, each hat from 4m.
# How much yarn was needed to make all the items?

# Think about it step by step, and show your work.
# """
def using_palm(text, api_key):
    palm.configure(api_key=api_key)

    model = "models/text-bison-001"
    prompt_template = PromptTemplate.from_template(
        '''
        You are a professional summarizer of YouTube video transcripts. 
        You know how to take the readers on a journey to make your summary interesting. 
        You end the summary with suspense to try to get the user to watch the YouTube video. 
        In 300 words, give a detailed and fun summary of this text: ```{text}```
        '''
    )

    formatted_prompt = prompt_template.format(text=text)

    completion = palm.generate_text(
        model=model,
        prompt=formatted_prompt,
        temperature=0.0,
        max_output_tokens=800,
    )

    return completion.result

text = '''
Then multiply the number of cats by the number 
of hats per cat to find the total number 
of hats: 9 cats * 1 hat / cat = 9 hats. 
Then multiply the number of hats by the length 
of yarn per hat to find the total length of 
yarn used for hats: 9 hats * 4m / hat = 36m. Then add the length of yarn used for mittens and hats to find the total length of yarn used: 252m + 36m = 288m.
'''
language="Spanish"
summary=using_palm(text, API_KEY)
print(summary)