"""it provides all the functionalities related to graph."""
#oggpnosn #hkhr
import numpy as np
import scipy
import networkx as nx

def compute_similarity(vector_1, vector_2):
    """it computes cosine similarity between two vectors."""
    distance = scipy.spatial.distance.cosine([vector_1], [vector_2])
    similarity = 1-distance
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
            score = compute_similarity(sentence_vectors[index_1],
                                       sentence_vectors[index_2])
            adjacency_matrix[index_1][index_2] = score
            adjacency_matrix[index_2][index_1] = score
    return adjacency_matrix

def threshold_graph(sentences, adjacency_matrix, similarity_threshold):
    """it returns a networkx graph by selecting edges above a threshold."""
    # intialize and undirected graph.
    graph = nx.Graph()
    # iterate through all sentence pair(upper triangular matrix only.)
    no_of_sentences = adjacency_matrix.shape[0]
    for index_1 in range(no_of_sentences):
        for index_2 in range(index_1+1, no_of_sentences):
            # get all the information necessary to form the graph.
            sentence_1 = sentences[index_1]
            sentence_2 = sentences[index_2]
            similarity = adjacency_matrix[index_1][index_2]
            # if similarity > similarity_threshold
            if similarity > similarity_threshold:
                # form an edge with weight as distance
                graph.add_edge(sentence_1, sentence_2,
                               weight=similarity)
            else:
                # just add nodes without edges.
                graph.add_node(sentence_1)
                graph.add_node(sentence_2)
    return graph
