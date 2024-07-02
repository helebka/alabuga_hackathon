import spacy
import pymorphy3

nlp_ru = spacy.load("ru_core_news_sm")


def extract_company(text: str) -> str:
    analyzer = pymorphy3.MorphAnalyzer()
    doc_ru = nlp_ru(text)
    companies = [ent.text for ent in doc_ru.ents if ent.label_ == "ORG"]
    
    if not companies:
        # company = "Неизвестная компания"
        company = "НН"
    else:
        company = max(companies, key=lambda x: companies.count(x))
        
    company = analyzer.parse(company)[0].normal_form.capitalize()
    
    return company