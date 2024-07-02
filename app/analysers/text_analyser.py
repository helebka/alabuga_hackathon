from app.analysers.extracter_companies import extract_company
from app.analysers.context_analyser import analyze_emotional_content
from app.analysers.translate import translate_russian_to_english


def text_analyser(text: str) -> dict:
    company = extract_company(text)
    mood = analyze_emotional_content(translate_russian_to_english(text))
    
    return [company, mood]
    