# Translate-Python

Translate-Python is a Python library that provides functionality for translating text and extracting transcripts from YouTube videos. It uses the Google Translate API and the YouTube Transcript API for its operations.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

To use Translate-Python, you need to follow these installation steps:

1. Clone the repository.
2. Navigate to the repository folder.
3. Run the setup.sh script to install the required dependencies:
    ```bash
    ./setup.sh
    ```
4. Create a .env file and provide your Google Translate API access token:
    ```bash
    echo "ACCESS_TOKEN=\"your_access_token_here\"" > .env
    ```
5. Install the Google Cloud Code extension for Visual Studio Code (optional).
6. Install the Google Cloud SDK by running the following command:
    ```bash
    curl https://sdk.cloud.google.com | bash
    ```
7. If you are using Visual Studio Code, reload the VS Code environment by running:
    ```bash
    code .
    ```
8. Install the required Google Cloud CLI components:
    ```bash
    gcloud components install alpha beta skaffold minikube kubectl gke-gcloud-auth-plugin
    ```

## Usage

The Translate-Python library provides the following modules:

1. `get_transcript.py`: This module contains functions for extracting transcripts from YouTube videos.
2. `lang_translator.py`: This module includes functions for translating text to different languages.
3. `streamlit_app.py`: This module implements a Streamlit application for summarizing and translating transcripts.
4. `summarize.py`: This module provides functions for summarizing transcripts using TF-IDF.
5. `using_palm.py`: This module demonstrates the usage of the PALM2 API for text generation.

To use any of the modules, import them into your Python script and call the relevant functions with the appropriate arguments.

## Features

Translate-Python offers the following features:

- Extraction of transcripts from YouTube videos.
- Translation of text to different languages using the Google Translate API.
- Summarization of transcripts using TF-IDF.
- Streamlit application for GUI-based transcript summarization and translation.
- Integration with the PALM2 API for advanced text generation.

## Contributing

Contributions to Translate-Python are welcome! If you have any ideas, improvements, or bug fixes, feel free to create a pull request. Please ensure that your code follows the repository's coding standards and is well-documented.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any inquiries or suggestions, please feel free to reach out to [your_email@example.com](mailto:your_email@example.com).