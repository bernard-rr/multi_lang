from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_youtube_video_id(url):
    # Extract video id using regular expression
    video_id_match = re.search(r'(?:v=|\/)([A-Za-z0-9_-]{11})', url)
    if video_id_match:
        return video_id_match.group(1)
    return None

def get_transcript_from_url(url):
    video_id = get_youtube_video_id(url)
    if video_id:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)
        # Combine all text segments into a single string
        combined_text = " ".join([entry['text'] for entry in transcript_data])
        return combined_text
    else:
        raise ValueError("Invalid YouTube URL")

# # Example usage:
# url = "https://m.youtube.com/watch?si=RExS6uPuY3JB2YSi&v=ZekOplAHwqs&feature=youtu.be"
# print(get_transcript_from_url(url))
