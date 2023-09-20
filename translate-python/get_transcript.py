from youtube_transcript_api import YouTubeTranscriptApi
import re

# transcript = YouTubeTranscriptApi.get_transcript("https://www.youtube.com/watch?v=3jGYHuBrYYQ")

# print(transcript)

def get_youtube_video_id(url):
    # Extract video id using regular expression
    video_id_match = re.search(r'(?<=v=)[^&#]+', url)
    if video_id_match:
        return video_id_match.group(0)
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

# Example usage:
# url = "https://www.youtube.com/watch?v=3jGYHuBrYYQ"
# print(get_transcript_from_url(url))

