"""it provide utility to vectorize sentences."""
#oggpnosn
#hkhr
import tensorflow_hub as hub
import numpy as np
import scipy
import tensorflow as tf


class Vectorizer:
    """it provides wrapper over our vectorizer."""

    def __init__(self):
        """it initializes tf-hub."""
        # creating a session.
        self.sess = tf.Session()
        # once the session is created load universal encoder.
        self.embed = hub.Module("https://tfhub.dev/google/universal-sentence-encoder/2")
        # intialize global variables.
        self.sess.run([tf.global_variables_initializer(), tf.tables_initializer()])

    def vectorize_sentences(self, sentences):
        """it vectorizes sentences."""
        sentence_vectors = self.embed(sentences)
        sentence_vectors = self.sess.run(sentence_vectors)
        return sentence_vectors
