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


# # Example usage:
# input_text = "Hello, how are you?"
# target_language = "es"  # Change this to "en", "fr", or "zh-CN" for different languages
# translated_text = translate_text(input_text, target_language)
# print(translated_text)
