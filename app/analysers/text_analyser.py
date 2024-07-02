from app.analysers.extracter_companies import extract_company
from app.analysers.context_analyser import analyze_emotional_content


def text_analyser(text: str) -> dict:
    company = extract_company(text)
    mood = analyze_emotional_content(text)
    
    return {"name": company, "estimate": mood}
    