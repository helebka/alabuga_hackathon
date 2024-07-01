import nltk
from textblob import TextBlob

def analyze_emotional_content(file_path):
    with open(file_path, 'r') as file:
        text = file.read()

    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment < 0:
        print("Эмоциональная наполненность текста: грустная")
    elif sentiment == 0:
        print("Эмоциональная наполненность текста: нейтральная")
    else:
        print("Эмоциональная наполненность текста: веселая")

# Пример использования
analyze_emotional_content('input.txt')