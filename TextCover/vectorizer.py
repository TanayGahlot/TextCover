"""it provide utility to vectorize sentences."""
#oggpnosn
#hkhr
import tensorflow_hub as hub
import numpy as np
import scipy
import tensorflow as tf


def similarity(vector_1, vector_2):
  """it computes cosine similarity between two vectors."""
  similarity = scipy.spatial.distance.cosine([vector_1], [vector_2])
  return similarity

def compute_adjacency_matrix(sentence_vectors):
  """it computes distance between every two pair of sentence."""
  # compute no of sentences.
  no_of_sentences = sentence_vectors.shape[0]
  # initialize adjacency_matrix with zeros.
  adjacency_matrix = np.identity(no_of_sentences)
  # for each sentence pair compute distance.
  for index_1 in range(no_of_sentences-1):
    for index_2 in range(index_1 + 1, no_of_sentences):
      score = similarity(sentence_vectors[index_1], sentence_vectors[index_2])
      adjacency_matrix[index_1][index_2] = score
      adjacency_matrix[index_2][index_1] = score
  return adjacency_matrix


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
