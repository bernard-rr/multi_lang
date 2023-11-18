# Translate Python

Translate Python is a Python package that provides utility functions for translating and summarizing text from YouTube videos. It utilizes popular libraries such as youtube_transcript_api, googletrans, and Streamlit to perform tasks like extracting transcripts, translating text, and summarizing content.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To use the Translate Python package, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/{username}/{repository}.git
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API access token:

   ```bash
   echo "ACCESS_TOKEN=\"\"" > .env
   ```

4. Install the Google Cloud Code extension for Visual Studio Code:

   ```bash
   code --install-extension GoogleCloudTools.cloudcode
   ```

5. Install the Google Cloud SDK:

   ```bash
   curl https://sdk.cloud.google.com | bash
   ```

6. Reload the Visual Studio Code environment:

   ```bash
   code .
   ```

7. Install additional Google Cloud CLI components:

   ```bash
   gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin
   ```

## Usage

The Translate Python package provides the following utility functions:

- `get_youtube_video_id(url)`: Extracts the video ID from a YouTube URL.
- `get_transcript_from_url(url)`: Retrieves the transcript of a YouTube video using the video ID.
- `translate_text(input_text, target_language)`: Translates the input text to the specified target language.
- `summarize_transcript(transcript_text, num_sentences)`: Generates a summary of the transcript using TF-IDF scoring.
- `using_palm(text, api_key)`: Uses the PALM2 API to generate a detailed and fun summary of the input text.

To use these functions in your Python script, import the corresponding module as follows:

```python
from get_transcript import get_transcript_from_url
from lang_translator import translate_text
from summarize import summarize_transcript
from using_palm import using_palm
```

Refer to the example usage within each module for sample code and output.

## Features

The Translate Python package offers the following features:

- Extracting YouTube video transcripts using the YouTube transcript API.
- Translating text to various languages using the Google Translate API.
- Summarizing transcripts using the TF-IDF algorithm.
- Generating detailed and fun summaries using the PALM2 API.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions or suggestions, feel free to reach out to me at [email@example.com](mailto:email@example.com).