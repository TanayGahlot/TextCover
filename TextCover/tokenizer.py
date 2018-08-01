"""it provides tokenization facilities."""
#oggpnson
#hkhr
from subprocess import call
import spacy
import en_core_web_sm


def load_spacy_language_module():
    """it loads language module if it's pre-downloaded, else it downloads it."""
    nlp = en_core_web_sm.load()
    return nlp


class Tokenizer:
    """it tokenizes raw_text into sentences using spacy's tokenizer."""

    def __init__(self):
        """load the spacy's tokenizer."""
        self.nlp = load_spacy_language_module()

    def sentence_tokenizer(self, text):
        """it returns list of sentences."""
        # replace the newline with spac.
        text = text.replace("\n", " ")
        # process the document using spacy's nlp kit.
        doc = self.nlp(text)
        # convert all the sentences into text.
        sentences = []
        for sentence in doc.sents:
            sentences.append(sentence.text)
        return sentences
