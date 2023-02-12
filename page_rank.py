import numpy as np

def page_rank(G, damping_factor=0.85, epsilon=0.0001):
    """
    Compute the PageRank of nodes in the graph.
    
    Parameters
    ----------
    G : numpy matrix
        Adjacency matrix of the graph.
    damping_factor : float
        The damping factor in the PageRank computation.
    epsilon : float
        The tolerance used to determine convergence.
        
    Returns
    -------
    numpy array
        The PageRank of each node in the graph.
    """
    n = G.shape[0]
    M = np.array(G, dtype=float)
    for i in range(n):
        if np.sum(M[i, :]) == 0:
            M[i,:] = np.ones(n) / n
        else:
            M[i,:] /= np.sum(M[i, :])
            
    outbound_link_counts = np.sum(G, axis=1)
    pr = np.ones(n) / n
    damping_value = (1 - damping_factor) / n
    
    while True:
        new_pr = np.zeros(n)
        for i in range(n):
            for j in range(n):
                if outbound_link_counts[j]:
                    new_pr[i] += damping_factor * M[i, j] * pr[j] / outbound_link_counts[j]
                else:
                    new_pr[i] += damping_factor * M[i, j] * pr[j]
                    
        new_pr += damping_value
        delta = np.abs(pr - new_pr).sum()
        if delta <= epsilon:
            return new_pr
        pr = new_pr

def test_page_rank():
    G = np.array([[0, 1, 1, 0],
                  [1, 0, 0, 0],
                  [1, 0, 0, 1],
                  [0, 0, 1, 0]])
    true_pr = np.array([0.2195122, 0.36585366, 0.36585366, 0.14634146])
    pr = page_rank(G, damping_factor=0.85, epsilon=0.0001)
    assert np.allclose(pr, true_pr, rtol=1e-6, atol=1e-6)

if __name__ == "__main__":
    test_page_rank()