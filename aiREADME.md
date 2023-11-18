# Translate Python

Translate Python is a Python package that provides utilities for translating text and retrieving transcripts from YouTube videos. It utilizes the `googletrans` library for text translation and the `youtube_transcript_api` library for extracting video transcripts from YouTube.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This repository contains Python scripts that enable translation of text and retrieval of YouTube video transcripts. The main functionalities are provided by `get_transcript.py` and `lang_translator.py` scripts. The `streamlit_app.py` script offers a user-friendly web interface for utilizing the translation and transcript summarization capabilities.

## Installation

To use this package, make sure you have Python 3.7 or higher installed. Follow the steps below to set up the required dependencies:

1. Clone this repository to your local machine.
2. Navigate to the repository's root directory.
3. Run `pip install -r requirements.txt` to install the necessary Python dependencies.
4. Create a `.env` file and provide an access token by adding the following line: `ACCESS_TOKEN=""`.
5. Install the Google Cloud Code extension for Visual Studio Code by running `code --install-extension GoogleCloudTools.cloudcode` in your terminal.
6. Install the Google Cloud SDK by executing `curl https://sdk.cloud.google.com | bash` in your terminal.
7. If you are using Visual Studio Code, reload the environment by running `code .` in your terminal.
8. Install the necessary Google Cloud CLI components by executing `gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin` in your terminal.

## Usage

To use the translation functionality, import the `translate_text` function from `lang_translator.py`. Provide the input text and the target language code to translate the text. Here's an example:

```python
input_text = "Hello, how are you?"
target_language = "es"  # Change this to "en", "fr", or "zh-CN" for different languages
translated_text = translate_text(input_text, target_language)
print(translated_text)
```

For extracting transcripts from YouTube videos, import the `get_transcript_from_url` function from `get_transcript.py`. Provide the YouTube URL, and the function will return the extracted transcript. Here's an example:

```python
url = "https://www.youtube.com/watch?v=3jGYHuBrYYQ"  # Replace with your YouTube URL
transcript = get_transcript_from_url(url)
print(transcript)
```

To use the `streamlit_app.py` script with the translation and summarization capabilities, navigate to the repository's root directory and run `streamlit run streamlit_app.py` in your terminal.

## Features

- Translation of text to various languages.
- Retrieval of transcripts from YouTube videos.
- Summarization of YouTube video transcripts.
- User-friendly web interface for translation and transcript summarization.

## Contributing

If you have any suggestions, bug reports, or would like to contribute to this project, please open an issue or submit a pull request. Your contributions are greatly appreciated!

## License

This project is licensed under the [MIT License](./LICENSE).

## Contact

For questions or inquiries, please contact [EMAIL] at [EMAIL_ADDRESS].