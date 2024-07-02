import spacy

nlp_ru = spacy.load("ru_core_news_sm")


def extract_company(text: str) -> str:
    doc_ru = nlp_ru(text)
    companies = [ent.text for ent in doc_ru.ents if ent.label_ == "ORG"]
    
    if not companies:
        # company = "Неизвестная компания"
        company = "НН"
    else:
        company = max(companies, key=lambda x: companies.count(x))
    
    return company