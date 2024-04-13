import re, string

import nltk
nltk.download('stopwords')

from nltk import word_tokenize
nltk.download('punkt')

from nltk.stem import *
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

from pymystem3 import Mystem
from string import punctuation


class Predictor:
    def __init__(self, model):
        self.model = model

        self.mystem = Mystem()
        self.russian_stopwords = stopwords.words("russian")
        self.russian_stopwords.extend(['…', '«', '»', '...', 'т.д.', 'т', 'д'])

        self.stemmer = SnowballStemmer("russian")
    

    def _remove_stickers(self, text):
        # Паттерн для поиска стикеров в формате [стикер]
        pattern = r"[^\w.!?,:;$\s/\"\']*"
        cleaned_text = re.sub(pattern, "", str(text))
        return cleaned_text

    def _remove_punctuation(self, text):
        return "".join([ch if ch not in string.punctuation else ' ' for ch in text])

    def _remove_numbers(self, text):
        return ''.join([i if not i.isdigit() else ' ' for i in text])

    def _remove_multiple_spaces(self, text):
        return re.sub(r'\s+', ' ', text, flags=re.I)
    
    def _lemmatize_text(self, text):
        tokens = self.mystem.lemmatize(text.lower())
        tokens = [token for token in tokens if token not in self.russian_stopwords and token != " "]
        text = " ".join(tokens)
        return text

    def _remove_stop_words(self, text):
        tokens = word_tokenize(text)
        tokens = [token for token in tokens if token not in self.russian_stopwords and token != ' ']
        return " ".join(tokens)

    def _lemmatize_text(self, text):
        text_lem = self.mystem.lemmatize(text)
        tokens = [token for token in text_lem if token != ' ' and token not in self.russian_stopwords]
        return " ".join(tokens)
    
    def _preprocess_text(self, text):
        text = self._remove_stickers(text)

        text = self._remove_multiple_spaces(self._remove_numbers(self._remove_punctuation(text.lower())))
        
        tokens = word_tokenize(text)
        stemmed_tokens = [self.stemmer.stem(token) for token in tokens if token not in self.russian_stopwords]
        text = " ".join(stemmed_tokens)

        text = self._remove_stop_words(text)

        text = self._lemmatize_text(text)

        return text
    
    def predict(self, texts_list: list) -> list:
        processed_texts_list = texts_list # [self._preprocess_text(text) for text in texts_list]
        return self.model.predict(processed_texts_list)