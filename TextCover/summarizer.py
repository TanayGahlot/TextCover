"""it wraps all the disjoint function to create summarizer."""
#oggpnson
#hkhr
from TextCover.tokenizer import Tokenizer
from TextCover.graph import compute_adjacency_matrix, threshold_graph
from TextCover.score import compute_page_rank, compute_text_cover_score, select_top_sentences
from TextCover.vectorizer import Vectorizer


class Summarizer:
    """it summarizes the document."""

    def __init__(self):
        """it initializes ..."""
        self.vectorizer = Vectorizer()
        self.tokenizer = Tokenizer()

    def summarize(self, text, distance_threshold, summary_length=5, verbose=True):
        """magic!"""
        # Step-0: Break the text into sentences.
        sentences = self.tokenizer.sentence_tokenizer(text)
        # Step-1: Vectorize each sentence.
        sentence_vectors = self.vectorizer.vectorize_sentences(sentences)
        # Step-2: Compute distance between each pair of sentence.
        adjacency_matrix = compute_adjacency_matrix(sentence_vectors)
        # Step-3: Threshold the graph using "distance_threshold"
        graph = threshold_graph(adjacency_matrix, distance_threshold)
        # Step-4: Compute node score on the basis of page rank.
        graph = compute_page_rank(graph)
        # Step-5: Compute hybrid TextCover score.
        graph = compute_text_cover_score(graph)
        # Step-6: Select the top-{summary_length} no of sentences.
        sentences = select_top_sentences(graph, summary_length)
        return adjacency_matrix
