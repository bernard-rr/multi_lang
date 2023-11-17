# Translate Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

Translate Python is a Python package that provides functionality for translating and summarizing YouTube video transcripts. It utilizes the `youtube_transcript_api` and `googletrans` libraries to retrieve the transcript and perform language translation.

## Installation

To install Translate Python, follow these steps:

1. Clone this repository:

```
git clone https://github.com/username/repo.git
```

2. Change into the repository directory:

```
cd repo
```

3. Install the required Python dependencies from `requirements.txt`:

```
pip install -r requirements.txt
```

4. Create a `.env` file with an empty `ACCESS_TOKEN`:

```
echo "ACCESS_TOKEN=\"\"" > .env
```

5. Install the Google Cloud Code VS Code extension:

```
code --install-extension GoogleCloudTools.cloudcode
```

6. Install the Google Cloud SDK:

```
curl https://sdk.cloud.google.com | bash
```

7. Reload the VS Code environment:

```
code .
```

8. Install Google Cloud CLI components:

```
gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin
```

## Usage

Translate Python provides two main modules:

### `get_transcript.py`
This module includes functions for extracting the YouTube video ID and retrieving the transcript from a given YouTube URL.

Example usage:
```python
from youtube_transcript_api import YouTubeTranscriptApi
import re

def get_youtube_video_id(url):
    # Extract video id using regular expression
    video_id_match = re.search(r'(?:v=|\\/)([A-Za-z0-9_-]{11})', url)
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

url = "https://m.youtube.com/watch?si=RExS6uPuY3JB2YSi&v=ZekOplAHwqs&feature=youtu.be"
print(get_transcript_from_url(url))
```

### `lang_translator.py`
This module includes functions for translating text using the Google Translate API.

Example usage:
```python
import googletrans
from googletrans import Translator, LANGUAGES

def translate_text(input_text, target_language):
    # Initialize the translator
    translator = Translator()

    # Translate the input text to the specified target language
    try:
        translation = translator.translate(input_text, dest=target_language)
        return translation.text
    except Exception as e:
        return f"Translation Error: {str(e)}"

input_text = "Hello, how are you?"
target_language = "es"  # Change this to "en", "fr", or "zh-CN" for different languages
translated_text = translate_text(input_text, target_language)
print(translated_text)
```

## Features

Translate Python provides the following features:

- Retrieval of YouTube video transcripts
- Language translation of text

## Contributing

Contributions are welcome! To contribute to Translate Python, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b my-branch-name`.
3. Make your changes and commit them: `git commit -m 'My changes'`.
4. Push to the original branch: `git push origin my-branch-name`.
5. Create a pull request.

## License

This project is licensed under the [MIT license](https://opensource.org/licenses/MIT).

## Contact

For any questions or suggestions, please feel free to [contact us](mailto:example@example.com).