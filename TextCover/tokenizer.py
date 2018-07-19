"""it provides tokenization facilities."""
#oggpnson
#hkhr
import spacy


class Tokenizer:
  """it tokenizes raw_text into sentences using spacy's tokenizer."""

  def __init__(self):
    """load the spacy's tokenizer."""
    self.nlp = spacy.load('en')

  def sentence_tokenizer(self, text):
    """it returns list of sentences."""
    # process the document using spacy's nlp kit.
    doc = self.nlp(text)
    # convert all the sentences into text.
    sentences = []
    for sentence in doc.sents:
      sentences.append(sentence.text)
    return sentences
