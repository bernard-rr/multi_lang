# Translate Python

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/<username>/<repository>/blob/main/LICENSE)

This repository contains Python scripts for translating and summarizing YouTube video transcripts using the YouTube Transcript API, Google Translate API, and AI-based summarization.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

The Translate Python repository provides a set of Python scripts for translating and summarizing YouTube video transcripts. It leverages the `youtube-transcript-api` library to retrieve the transcript from a YouTube video URL and the `googletrans` library for language translation.

The repository includes the following scripts:

- `get_transcript.py`: Retrieves the transcript from a YouTube video URL using the YouTube Transcript API.
- `lang_translator.py`: Translates text to a specified target language using the Google Translate API.
- `summarize.py`: Uses TF-IDF to summarize a transcript text into a specified number of sentences.
- `streamlit_app.py`: A Streamlit web app that allows users to summarize and translate YouTube video transcripts.
- `setup.sh`: A shell script for setting up the required dependencies and environment.

## Installation

To use the scripts in this repository, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/<username>/<repository>.git
   ```

2. Install the required Python dependencies from the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with an `ACCESS_TOKEN` variable. For example:

   ```
   ACCESS_TOKEN=""
   ```

4. Install the Google Cloud Code extension for Visual Studio Code:

   ```bash
   code --install-extension GoogleCloudTools.cloudcode
   ```

5. Install the Google Cloud SDK:

   ```bash
   curl https://sdk.cloud.google.com | bash
   ```

6. Reload the Visual Studio Code environment (if using a Visual Studio Code terminal):

   ```bash
   code .
   ```

7. Install the required Google Cloud CLI components:

   ```bash
   gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin
   ```

## Usage

This repository provides various scripts for translating and summarizing YouTube video transcripts. Here is an example of the usage for each script:

### `get_transcript.py`

The `get_transcript` module provides a function `get_transcript_from_url` to retrieve the transcript from a YouTube video URL:

```python
from get_transcript import get_transcript_from_url

url = "https://www.youtube.com/watch?v=VIDEO_ID"
transcript = get_transcript_from_url(url)
print(transcript)
```

### `lang_translator.py`

The `lang_translator` module provides a function `translate_text` to translate text to a specified target language:

```python
from lang_translator import translate_text

input_text = "Hello, how are you?"
target_language = "es"  # Change this to "en", "fr", or "zh-CN" for different languages
translated_text = translate_text(input_text, target_language)
print(translated_text)
```

### `summarize.py`

The `summarize` module provides a function `summarize_transcript` to summarize a transcript:

```python
from summarize import summarize_transcript

transcript_text = "This is a long transcript text..."
summary = summarize_transcript(transcript_text, num_sentences=5)
print(summary)
```

### `streamlit_app.py`

The `streamlit_app` module provides a Streamlit web app for summarizing and translating YouTube video transcripts. Run the following command to start the app:

```bash
streamlit run streamlit_app.py
```

## Features

- Retrieve YouTube video transcripts using the YouTube Transcript API.
- Translate text to different languages using the Google Translate API.
- Summarize YouTube video transcripts using TF-IDF.
- Web app for interactive transcript summarization and translation.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug fixes, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://github.com/<username>/<repository>/blob/main/LICENSE).

## Contact

For any questions or inquiries, please contact:

- Name: [Your Name]
- Email: [Your Email]