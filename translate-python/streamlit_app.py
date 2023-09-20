import streamlit as st
import base64
from get_transcript import get_transcript_from_url
from summarize import summarize_text
from summarize import random_sentences_from_text



def summarize_transcript(youtube_url):
	transcript = get_transcript_from_url(youtube_url)
	shortened_text = random_sentences_from_text(transcript, num_sentences=500)
	summary = summarize_text(shortened_text)
	print(summary)

url = "https://www.youtube.com/watch?v=3jGYHuBrYYQ"
summarize_transcript(url)



# # Function to generate a download link for the translated text
# def get_text_file_download_link(text, filename="translated_transcript.txt"):
#     """Generate a link to download the text as a .txt file"""
#     b64 = base64.b64encode(text.encode()).decode()
#     return f'<a href="data:text/plain;base64,{b64}" download="{filename}">Download Translated Transcript</a>'

# # Streamlit UI
# st.title("YouTube Transcript Translator")

# # Input for YouTube URL
# youtube_url = st.text_input("Enter YouTube Video URL:", "")

# # Dropdown for language selection
# language = st.selectbox("Select Target Language:", SUPPORTED_LANGUAGES)

# # Translate button
# if st.button("Translate"):
#     if not youtube_url:
#         st.warning("Please provide a valid YouTube URL.")
#     else:
#         try:
#             transcript = get_transcript_from_url(youtube_url)
#             translated_text = translate_text(transcript, language)
#             st.text_area("Translated Transcript:", value=translated_text, height=300)

#             # Display download link
#             st.markdown(get_text_file_download_link(translated_text), unsafe_allow_html=True)

#         except Exception as e:
#             st.error(f"An error occurred: {e}")

# st.write("Note: This app uses AI for translation, and while it is powerful, it might not always be 100% accurate.")
