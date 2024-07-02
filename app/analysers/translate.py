from deep_translator import GoogleTranslator

def translate_russian_to_english(text):
    translated_text = GoogleTranslator(source='ru', target='en').translate(text)
    return translated_text
