"""it provides tokenization facilities."""
#oggpnson
#hkhr
from subprocess import call
import spacy


def load_spacy_language_module():
    """it loads language module if it's pre-downloaded, else it downloads it."""
    try:
        nlp = spacy.load('en')
        return nlp
    except OSError:
        call(["python", "-m", "spacy", "download", "xx"])
        load_spacy_language_module()

class Tokenizer:
    """it tokenizes raw_text into sentences using spacy's tokenizer."""

    def __init__(self):
        """load the spacy's tokenizer."""
        self.nlp = load_spacy_language_module()

    def sentence_tokenizer(self, text):
        """it returns list of sentences."""
        # process the document using spacy's nlp kit.
        doc = self.nlp(text)
        # convert all the sentences into text.
        sentences = []
        for sentence in doc.sents:
            sentences.append(sentence.text)
        return sentences
