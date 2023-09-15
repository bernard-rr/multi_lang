import os
from dotenv import load_dotenv
import google.generativeai as palm

load_dotenv()

API_KEY = os.environ.get('API_KEY')

palm.configure(api_key=API_KEY)

model_id = 'models/text-bison-001'
prompt = '''
Write a marketing proposal to sell icecream
'''
completion = palm.generate_text(
    model=model_id,
    prompt=prompt,
    temperature=0.1,
    max_output_tokens=100,
    candidate_count=1
)
print(completion)