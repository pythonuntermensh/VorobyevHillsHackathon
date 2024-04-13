from keybert import KeyBERT

class KeywordsExtractor:
    def __init__(self) -> None:
        self.kw_model = KeyBERT("paraphrase-multilingual-MiniLM-L12-v2")

    def get_keywords(self, text):
        return self.kw_model.extract_keywords(text, keyphrase_ngram_range=(3, 3), stop_words=None)