# Repository Name

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This repository houses a Python application for translating and summarizing YouTube video transcripts. The application utilizes the [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for retrieving the transcripts and leverages the [Streamlit](https://www.streamlit.io/) framework for building a user interface.

## Installation

To run this application, please follow these steps:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/username/repository.git
   ```

2. Setup the Docker development container. Open a terminal or command prompt and navigate to the root folder of the cloned repository. Run the following command:

   ```
   docker-compose up -d
   ```

   This will create a development container using the specified Docker image.

3. Install the required Python packages by running the following command:

   ```
   docker-compose exec app pip install -r requirements.txt
   ```

## Usage

To utilize the application, follow these steps:

1. Run the Streamlit app within the Docker development container:

   ```
   docker-compose exec app streamlit run streamlit_app.py
   ```

   This command will start the Streamlit application and launch it in your web browser.

2. Input the YouTube video URL and select the target language from the dropdown menu.

3. Click the "Translate" button. The app will retrieve the transcript, translate it to the specified language, and display the translated transcript along with a download link.

## Features

- Translates YouTube video transcripts to multiple languages
- Summarizes the translated transcript to a shorter version
- Provides a download link for the translated transcript

## Contributing

Contributions to this repository are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your modifications
4. Commit your changes
5. Push the branch to your forked repository
6. Open a pull request to the main repository

Please ensure that your contributions adhere to the repository's code style and conventions.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

For any questions or inquiries, please contact [email protected]